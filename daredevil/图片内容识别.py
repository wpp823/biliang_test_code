import base64
import json
import logging  # noqa
import os  # noqa
import re
import typing  # noqa
import unittest  # noqa

import requests
from white_queen_nlp import jieba_utils
from white_queen_nlp.jieba_utils import DiseaseCutV3, load_word_cls

OCR_SERVER = 'ce.puzhizhuhai.com'
OCR_PORT = "443"
# OCR_PATH = "/predict/ocr_system"
OCR_PATH = "/mpadds/predict/ocr_system"


def load_0_medicine_word_upper(min_word_count: int = 2) -> typing.Set[str]:
    """  """
    tmp_dict = load_word_cls()
    word_set = set()
    cls_index_set = {0, }
    for word, cls_index in tmp_dict.items():
        if cls_index not in cls_index_set:
            continue
        if len(word) < min_word_count:
            continue
        word_set.add(word.upper())
    return word_set


class MyDiseaseCut(DiseaseCutV3):
    def __init__(self, logger: logging.Logger, jieba=None):
        super(DiseaseCutV3, self).__init__(logger=logger, jieba=jieba)
        self.disease_word_set = load_0_medicine_word_upper()

    def parse_disease_words(self, sentence_list: typing.List[str]) -> typing.List[typing.List[str]]:
        """ """
        result_list = []
        for q in sentence_list:
            _disease_word_set = set()
            try:
                word_list = self.jieba.cut(q)
                for word in word_list:
                    if word in self.stop_word_set:
                        continue
                    if word.upper() in self.disease_word_set:
                        _disease_word_set.add(word)
            except Exception as e:
                self.logger.error(f"[parse_disease_words] sentence {q}, error is {e}", exc_info=True)
                raise
            if list(_disease_word_set):
                result_list.append(list(_disease_word_set))

        return result_list


def do_ocr_image_parse_tag(image_path):
    """
    识别图片从识别的文字中新建联系人tag

    :param image_path:
    :return:
    """

    # med_ocr = FormMedicalRecordOcr(log=self.log, ip=OCR_SERVER, port=OCR_PORT, path=OCR_PATH)
    with open(image_path, 'rb') as im:
        b_image = im.read()
    headers = {"Content-type": "application/json"}
    data = {"images": [base64.b64encode(b_image).decode('utf8')]}

    url = "https://{ip}{path}".format(ip=OCR_SERVER, path=OCR_PATH)
    response = requests.post(url=url, headers=headers, data=json.dumps(data), timeout=40)
    res = response.json()["results"][0]

    text = ''.join([item.get("text", None) for item in res])
    # import re
    pattern_bl = re.compile(r'.+病历.*')
    pattern_yy = re.compile(r'.+医院.*|.+医学院.*')


    print(text)
    # match_yy = re.search(r'.+医院.*|.+医学院.*', text)
    #
    match_bl = pattern_bl.search(text)
    match_yy = pattern_yy.search(text)

    # print(match_yy)
    print(match_bl)
    if match_yy and match_bl:
        print('是病例')
    else:
        print("不是")
    jieba_obj = jieba_utils.load_jieba()
    # word_filder =(?=[B])[A]
    d = MyDiseaseCut(logger=logging.getLogger(), jieba=jieba_obj)
    # load_all_medicine_word_v3_upp()
    # s_list = [
    #     # "怎么办",
    #     "高血压和高血脂, 要注意什么"
    # ]
    cls_index_set = {0}
    print(d.parse_disease_words([text]))
    # for d_w_list in d.parse_disease_words_disease_words(text_list):
    #     print(d_w_list_list)


if __name__ == "__main__":
    # do_ocr_image_parse_tag('forward_0/forward_8599071251638979422_d033118d0470da34f3490d634b8e1473.jpg')
    # do_ocr_image_parse_tag('forward_0/forward_8599071251638979422_a835839d7f0e20f78e28006630b05839.jpg')
    do_ocr_image_parse_tag('病例/4800519822844248230.jpg')
