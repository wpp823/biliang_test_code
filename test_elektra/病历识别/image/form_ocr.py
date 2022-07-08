# import cv2
# import numpy as np

# class MedicalRecord(BaseModel):
#     hospital_name : Optional[str]     # 医院名称
#
#     name:Optional[str]
#     gender:Optional[str]
#     age:Optional[int]
#     inquiry_at:Optional[str]      #就诊时间  2021-03-23 09:34
#     department_name:Optional[str] #就诊科室
#
#     regist_no:Optional[str]       #登陆号
#     patient_tells:Optional[str]   #主诉
#     medical_allergy:Optional[str]     # 过敏史
#     cmd:Optional[str]     #中医诊断
#     wmd:Optional[str]     #西医诊断
#
#     doctor_name:Optional[str]         # 医生名称
#     other_history:Optional[str]       # 其他病史
#
#     treatment_plan:Optional[str]      # 治疗方案
#     physical_examination:Optional[str]  # 体检
#
#     pass
import base64
import json
import logging  # noqa
import math
import os  # noqa
import random
import string
import time
import typing  # noqa

import requests
from PIL import Image, ImageDraw, ImageFont

from modal import MedicalRecord
from parse_base import get_hospital_schedular_class_name
# from app.util.ocr_tools.image.ocr_cache import OcrCache


# from PIL import Image


def cv2_to_base64(image):
    return base64.b64encode(image).decode('utf8')


class FormMedicalRecordOcr:
    '''
    病历表单识别
    '''

    def __init__(self, log, ip, port="8868", path="/predict/ocr_system"):
        '''
        
        :param log:
        :param ip:
        :param port:
        :param path:
        :param cache_tool:  是否有cache工作。
        '''

        self._log = log

        if port == "80":
            self._url = "http://{ip}{path}".format(ip=ip, path=path)
        elif port == "443":
            self._url = "https://{ip}{path}".format(ip=ip, path=path)
        else:
            self._url = "http://{ip}:{port}{path}".format(ip=ip, port=port, path=path)
        # self._cache = cache_tool

        self._log.info("[FormMedicalRecordOcr][url: {}]".format(self._url))
        self._sess: requests.Session = None

    def recogn_raw_from_url(self, img_url):
        '''
        从url获取图片数据来进行相应的识别，并返回原始识别结果。
        :param img_url:
        :return:v[list(item)], item的结构为{'confidence': 0.9973363280296326, 'text': '深圳市中医院',
                           'text_region': [[307, 277], [815, 240], [820, 300], [311, 337]]},
        '''

        res_obj = None
        ocr_raw = None
        try:
            # 此URL应该为内部URL，不要是外部URL
            #  1. 将OSS的URL换成内部URL，
            sz_img_url = img_url
            ali_pos = img_url.find(".aliyuncs.com")
            if ali_pos != -1:
                # 将其转成ali云内部地址
                sz_img_url = "{}-internal{}?x-oss-process=image/resize,l_1000,m_mfit".format(img_url[:ali_pos], img_url[ali_pos:])
                # sz_img_url = "{}{}?x-oss-process=image/resize,l_1000,m_mfit".format(img_url[:ali_pos], img_url[ali_pos:])
            # 此oss处理过程为见文档   https://help.aliyun.com/document_detail/44688.html?spm=a2c4g.11186623.6.749.4dc04981v7CskE#title-y1e-xd2-5oo
            # 这是按长短边待比缩放
            self._log.info("[recogn_raw_from_url][url:{}]".format(sz_img_url))
            res_obj = requests.get(sz_img_url, timeout=20)
        except:
            self._log.exception("[recogn_raw_from_url][get_image_failed][img_url:{}]".format(img_url))
            res_obj = None

        if res_obj:
            ocr_raw = self.recogn_origin(img_data=res_obj.content)

        return ocr_raw

    def recogn_from_url(self, img_url, ocr_hostpital_name=None):
        '''
        
        :param img_url:
        :param  ocr_hostpital_name:     [str]OCR医院名称。
        :return: MedicalRecord, list()    MedicalRecord为结构化后的数据，list为ocr识别的原始数据。
        '''

        ocr_obj = None
        ocr_raw = None
        try:
            ocr_raw = self.recogn_raw_from_url(img_url=img_url)
            if ocr_raw:
                ocr_obj = self._to_medical_record_obj(recogn_result=ocr_raw, ocr_hostpital_name=ocr_hostpital_name)
        except:
            self._log.exception("[recogn_from_url][img_url:{}]".format(img_url))

        return ocr_obj, ocr_raw

    def recogn_origin(self, img_data) -> typing.List:
        '''
        返回识别的原始结构
        :param img_data:
        :return:    [list(item)], item的结构为{'confidence': 0.9973363280296326, 'text': '深圳市中医院',
                           'text_region': [[307, 277], [815, 240], [820, 300], [311, 337]]},
        '''

        rec_result = None

        # if self._cache:
        #     rec_result = self._cache.get_ocr_result(img_data=img_data)  # 判断缓存是否存在。
        if not rec_result:
            rec_result = self._recognition(img_data=img_data)
            # if self._cache:
            #     self._cache.set_ocr_result(img_data=img_data, ocr_result=rec_result)  # 写入缓存

        return rec_result

    def recogn(self, img_data):
        '''
        返回识别的结构化数据。
        :param img_data: [data]数据数据data,直接从文件中读出来的如：  img_data = open(image_file, 'rb').read()
        :return: MedicalRecord, list()    MedicalRecord为结构化后的数据，list为ocr识别的原始数据。
        '''

        ocr_obj = None
        ocr_result = []

        try:

            ocr_result = self.recogn_origin(img_data=img_data)
            ocr_obj = self._to_medical_record_obj(recogn_result=ocr_result)

        except:
            self._log.exception("[recogn]")

        return ocr_obj, ocr_result

    def _recognition(self, img_data):
        '''
        识别
        :param img_data:    [data]数据数据data,直接从文件中读出来的如：  img_data = open(image_file, 'rb').read()
        :return:
        '''

        starttime = time.time()

        headers = {"Content-type": "application/json"}
        data = {'images': [cv2_to_base64(img_data)]}

        if self._sess is None:
            self._sess = requests.Session()

        with self._sess as session:
            r = session.post(url=self._url, headers=headers, data=json.dumps(data), timeout=40)
        res = []
        try:

            elapse = time.time() - starttime

            # r_dict = r.json()
            # result_list = r_dict.get("results",[])

            res = r.json()["results"][0]
            self._log.info("[FormMedicalRecordOcr_recognition][len:{}, result:{}]".format(elapse, res))
        except:
            self._log.exception("[FormMedicalRecordOcr_recognition_error][{}]".format(r.content))

        return res

    def _to_medical_record_obj(self, recogn_result, ocr_hostpital_name=None) -> MedicalRecord:
        '''
        转成病历对象输出。
        :param recogn_result:   []_recognition识别结果，
        :param ocr_hostpital_name:  [str]医院的OCR名称。
        :return:
        '''

        # base_parse = ParseBase(log=self._log, recogn_result=recogn_result)
        # hostpital_name = base_parse.parse_hospital_name(recogn_result=recogn_result)
        # hostpital_class_name = hospital_map.get(hostpital_name,DEFAULT_HOSTPITAL_CLASS_NAME)      # 先找到相应的医院解析类名。
        hostpital_class_name = get_hospital_schedular_class_name(log=self._log, recogn_result=recogn_result, ocr_hostpital_name=ocr_hostpital_name)

        # 识别是否
        med_obj = None
        if hostpital_class_name:

            class_pos = hostpital_class_name.rfind(".")

            # 动态加载模块
            package = __import__(hostpital_class_name[:class_pos], fromlist=[hostpital_class_name[class_pos + 1:]])
            hostpital_class = getattr(package, hostpital_class_name[class_pos + 1:])

            hostpital_obj = hostpital_class(log=self._log, recogn_result=recogn_result)
            parse_obj = hostpital_obj.get_parse_obj()
            if parse_obj:
                self._log.info("[_to_medical_record_obj][user_parse_obj, classname:{}]".format(type(parse_obj).__name__))
                med_obj = parse_obj.get_medica_record_obj()

            else:
                self._log.warning("[_to_medical_record_obj_failed][no support form in hosiptal({})]".format(hostpital_class_name))
        else:
            self._log.warning("[_to_medical_record_obj_failed][no support hosiption({})]".format(hostpital_class_name))

        return med_obj


def draw_text_det_res(dt_boxes, img_path):
    import cv2
    import numpy as np
    src_im = cv2.imread(img_path)
    for box in dt_boxes:
        box = np.array(box).astype(np.int32).reshape(-1, 2)
        cv2.polylines(src_im, [box], True, color=(255, 255, 0), thickness=2)
    return src_im


def resize_img(img, input_size=600):
    """
    resize img and limit the longest side of the image to input_size
    """
    import cv2
    import numpy as np
    img = np.array(img)
    im_shape = img.shape
    im_size_max = np.max(im_shape[0:2])
    im_scale = float(input_size) / float(im_size_max)
    img = cv2.resize(img, None, None, fx=im_scale, fy=im_scale)
    return img


def draw_ocr(image,
             boxes,
             txts=None,
             scores=None,
             drop_score=0.5,
             font_path="./doc/simfang.ttf"):
    """
    Visualize the results of OCR detection and recognition
    args:
        image(Image|array): RGB image
        boxes(list): boxes with shape(N, 4, 2)
        txts(list): the texts
        scores(list): txxs corresponding scores
        drop_score(float): only scores greater than drop_threshold will be visualized
        font_path: the path of font which is used to draw text
    return(array):
        the visualized img
    """
    import cv2
    import numpy as np
    if scores is None:
        scores = [1] * len(boxes)
    box_num = len(boxes)
    for i in range(box_num):
        if scores is not None and (scores[i] < drop_score or
                                   math.isnan(scores[i])):
            continue
        box = np.reshape(np.array(boxes[i]), [-1, 1, 2]).astype(np.int64)
        image = cv2.polylines(np.array(image), [box], True, (255, 0, 0), 2)
    if txts is not None:
        img = np.array(resize_img(image, input_size=600))
        txt_img = text_visual(
            txts,
            scores,
            img_h=img.shape[0],
            img_w=600,
            threshold=drop_score,
            font_path=font_path)
        img = np.concatenate([np.array(img), np.array(txt_img)], axis=1)
        return img
    return image


def draw_ocr_box_txt(image,
                     boxes,
                     txts,
                     scores=None,
                     drop_score=0.5,
                     font_path="./doc/simfang.ttf",
                     font_size_safe: bool = False,
                     ):
    import numpy as np
    h, w = image.height, image.width
    img_left = image.copy()
    img_right = Image.new('RGB', (w, h), (255, 255, 255))

    random.seed(0)
    draw_left = ImageDraw.Draw(img_left)
    draw_right = ImageDraw.Draw(img_right)
    for idx, (box, txt) in enumerate(zip(boxes, txts)):
        if scores is not None and scores[idx] < drop_score:
            continue
        color = (random.randint(0, 255), random.randint(0, 255),
                 random.randint(0, 255))
        draw_left.polygon(box, fill=color)
        draw_right.polygon(
            [
                box[0][0], box[0][1], box[1][0], box[1][1], box[2][0],
                box[2][1], box[3][0], box[3][1]
            ],
            outline=color)
        box_height = math.sqrt((box[0][0] - box[3][0]) ** 2 + (box[0][1] - box[3][
            1]) ** 2)
        box_width = math.sqrt((box[0][0] - box[1][0]) ** 2 + (box[0][1] - box[1][
            1]) ** 2)
        if box_height > 2 * box_width:
            font_size = max(int(box_width * 0.9), 10)
            font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
            cur_y = box[0][1]
            for c in txt:
                char_size = font.getsize(c)
                draw_right.text(
                    (box[0][0] + 3, cur_y), c, fill=(0, 0, 0), font=font)
                cur_y += char_size[1]
        else:
            if font_size_safe:
                font_size = min(max(int(box_height * 0.8), 10), max(int(box_width * 0.95 / len(txt)), 10))
            else:
                font_size = max(int(box_height * 0.8), 10)
            font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
            draw_right.text(
                [box[0][0], box[0][1]], txt, fill=(0, 0, 0), font=font)
    img_left = Image.blend(image, img_left, 0.5)
    img_show = Image.new('RGB', (w * 2, h), (255, 255, 255))
    img_show.paste(img_left, (0, 0, w, h))
    img_show.paste(img_right, (w, 0, w * 2, h))
    return np.array(img_show)


class OcrRes(typing.NamedTuple):
    name: str
    boxes: typing.List[typing.List[typing.List[int]]]
    txts: typing.List[str]


def draw_ocr_box_txt_v2(image,
                        res_list: typing.List[OcrRes],
                        scores=None,
                        drop_score=0.5,
                        font_path="./doc/simfang.ttf",
                        font_size_safe: bool = False,
                        ):
    import numpy as np

    h, w = image.height, image.width
    img_top = image.copy()
    name_h = 20
    img_show = Image.new('RGB', (w, h * (1 + len(res_list)) + name_h * len(res_list)), (255, 255, 255))
    img_show.paste(img_top, (0, 0, w, h))

    for res_i, res in enumerate(res_list):

        # name
        img_name = Image.new('RGB', (w, name_h), (127, 255, 255))
        font = ImageFont.truetype(font_path, int(name_h / 2), encoding="utf-8")
        ImageDraw.Draw(img_name).text([int(w / 2), int(name_h / 4)], res.name, fill=(0, 0, 0), font=font)
        _height = h + res_i * (h + name_h)
        img_show.paste(img_name, (0, _height, w, _height + name_h))

        # result
        img_bottom = Image.new('RGB', (w, h), (255, 255, 255))
        random.seed(0)
        draw_bottom = ImageDraw.Draw(img_bottom)

        for idx, (box, txt) in enumerate(zip(res.boxes, res.txts)):
            if scores is not None and scores[idx] < drop_score:
                continue
            color = (random.randint(0, 255), random.randint(0, 255),
                     random.randint(0, 255))
            draw_bottom.polygon(
                [
                    box[0][0], box[0][1], box[1][0], box[1][1], box[2][0],
                    box[2][1], box[3][0], box[3][1]
                ],
                outline=color)
            box_height = math.sqrt((box[0][0] - box[3][0]) ** 2 + (box[0][1] - box[3][
                1]) ** 2)
            box_width = math.sqrt((box[0][0] - box[1][0]) ** 2 + (box[0][1] - box[1][
                1]) ** 2)
            if box_height > 2 * box_width:
                font_size = max(int(box_width * 0.9), 10)
                font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
                cur_y = box[0][1]
                for c in txt:
                    char_size = font.getsize(c)
                    draw_bottom.text(
                        (box[0][0] + 3, cur_y), c, fill=(0, 0, 0), font=font)
                    cur_y += char_size[1]
            else:
                if font_size_safe:
                    if txt:
                        font_size = min(max(int(box_height * 0.8), 10), max(int(box_width * 0.95 / len(txt)), 10))
                    else:
                        font_size = max(int(box_height * 0.8), 10)
                else:
                    font_size = max(int(box_height * 0.8), 10)
                font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
                draw_bottom.text(
                    [box[0][0], box[0][1]], txt, fill=(0, 0, 0), font=font)

        _height = h + res_i * (h + name_h) + name_h
        img_show.paste(img_bottom, (0, _height, w, _height + h))

    return np.array(img_show)


def str_count(s):
    """
    Count the number of Chinese characters,
    a single English character and a single number
    equal to half the length of Chinese characters.
    args:
        s(string): the input of string
    return(int):
        the number of Chinese characters
    """
    count_zh = count_pu = 0
    s_len = len(s)
    en_dg_count = 0
    for c in s:
        if c in string.ascii_letters or c.isdigit() or c.isspace():
            en_dg_count += 1
        elif c.isalpha():
            count_zh += 1
        else:
            count_pu += 1
    return s_len - math.ceil(en_dg_count / 2)


def text_visual(texts,
                scores,
                img_h=400,
                img_w=600,
                threshold=0.,
                font_path="./doc/simfang.ttf"):
    """
    create new blank img and draw txt on it
    args:
        texts(list): the text will be draw
        scores(list|None): corresponding score of each txt
        img_h(int): the height of blank img
        img_w(int): the width of blank img
        font_path: the path of font which is used to draw text
    return(array):
    """
    import numpy as np
    if scores is not None:
        assert len(texts) == len(
            scores), "The number of txts and corresponding scores must match"

    def create_blank_img():
        blank_img = np.ones(shape=[img_h, img_w], dtype=np.int8) * 255
        blank_img[:, img_w - 1:] = 0
        blank_img = Image.fromarray(blank_img).convert("RGB")
        draw_txt = ImageDraw.Draw(blank_img)
        return blank_img, draw_txt

    blank_img, draw_txt = create_blank_img()

    font_size = 20
    txt_color = (0, 0, 0)
    font = ImageFont.truetype(font_path, font_size, encoding="utf-8")

    gap = font_size + 5
    txt_img_list = []
    count, index = 1, 0
    for idx, txt in enumerate(texts):
        index += 1
        if scores[idx] < threshold or math.isnan(scores[idx]):
            index -= 1
            continue
        first_line = True
        while str_count(txt) >= img_w // font_size - 4:
            tmp = txt
            txt = tmp[:img_w // font_size - 4]
            if first_line:
                new_txt = str(index) + ': ' + txt
                first_line = False
            else:
                new_txt = '    ' + txt
            draw_txt.text((0, gap * count), new_txt, txt_color, font=font)
            txt = tmp[img_w // font_size - 4:]
            if count >= img_h // gap - 1:
                txt_img_list.append(np.array(blank_img))
                blank_img, draw_txt = create_blank_img()
                count = 0
            count += 1
        if first_line:
            new_txt = str(index) + ': ' + txt + '   ' + '%.3f' % (scores[idx])
        else:
            new_txt = "  " + txt + "  " + '%.3f' % (scores[idx])
        draw_txt.text((0, gap * count), new_txt, txt_color, font=font)
        # whether add new blank img or not
        if count >= img_h // gap - 1 and idx + 1 < len(texts):
            txt_img_list.append(np.array(blank_img))
            blank_img, draw_txt = create_blank_img()
            count = 0
        count += 1
    txt_img_list.append(np.array(blank_img))
    if len(txt_img_list) == 1:
        blank_img = np.array(txt_img_list[0])
    else:
        blank_img = np.concatenate(txt_img_list, axis=1)
    return np.array(blank_img)


def base64_to_cv2(b64str):
    import cv2
    import numpy as np
    data = base64.b64decode(b64str.encode('utf8'))
    data = np.fromstring(data, np.uint8)
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)
    return data


def draw_boxes(image, boxes, scores=None, drop_score=0.5):
    import cv2
    import numpy as np
    if scores is None:
        scores = [1] * len(boxes)
    for (box, score) in zip(boxes, scores):
        if score < drop_score:
            continue
        box = np.reshape(np.array(box), [-1, 1, 2]).astype(np.int64)
        image = cv2.polylines(np.array(image), [box], True, (255, 0, 0), 2)
    return image
