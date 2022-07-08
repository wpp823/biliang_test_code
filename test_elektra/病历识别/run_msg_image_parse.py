import requests

from my_log import get_logger
from image.form_ocr import FormMedicalRecordOcr
from setting import OCR_SERVER, OCR_PATH, OCR_PORT

log = get_logger()
# DEFAULT_HOSPITAL_NAME = "默认病历医院"
# OCR_SERVER = 'ce.puzhizhuhai.com'
# OCR_PORT = "443"
# # OCR_PATH = "/predict/ocr_system"
# OCR_PATH = "/mpadds/predict/ocr_system"


def run_msg_image_parse(img_url):
    """
    识别图片从识别的文字中新建联系人tag

    :param from_username:
    :param msgSvrId: 原始消息记录
    :param img_url: 图片地址
    :return:
    """
    # mongo_db = get_mongo(host=MONGO_HOST_PART, db=MONGO_DB_NAME, host_uri=MONGO_HOST,
    #                      authentication_source=MONGO_HOST_AUTH_DB, replicaset=MONGO_HOST_REPLICA_SET, log=log)
    log.info("[run_msg_image_parse][begin][img_url:{}]".format(img_url))

    from_medical_record_ocr = FormMedicalRecordOcr(ip=OCR_SERVER, path=OCR_PATH, port=OCR_PORT, log=log)
    all_tags = []  # 所有病历识别对象
    try:
        # 获取图片

        img_res = requests.get(img_url)
        b_image = img_res.content
        ocr_obj, ocr_result = from_medical_record_ocr.recogn(img_data=b_image)

        if ocr_obj and ocr_obj.is_medical_record:
            name = ocr_obj.name  # 病历识别姓名
            age = ocr_obj.age  # 病历识别年龄
            gender = ocr_obj.gender  # 病历识别性别
            cmd = ocr_obj.cmd  # 中医诊断内容
            wmd = ocr_obj.wmd  # 西医诊断内容


    except:
        log.exception("[do_ocr_image_parse_tag][img_url:{}]".format(img_url))

    log.info("[end_do_ocr_image_parse_tag][end][img_url:{}]".format(img_url))


if __name__ == '__main__':
    target_img_url = "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/limit/deeppupil/2022-07-05/wxid_n51dz3t9zqtg22_3300523927608307280_tF9atAKM.jpg"
    run_msg_image_parse(target_img_url)
