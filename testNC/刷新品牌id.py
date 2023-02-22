import pymongo
import pypinyin
import shortuuid
from mongoengine import register_connection, connection

from my_log import logger
from mongo_db.dao.products import ProductDao

MONGO_HOST_PART = "mongodb://root:@192.168.1.230" # 230
# MONGO_HOST_PART  = "mongodb://root:@dds-wz9db3743e6de5041152-pub.mongodb.rds.aliyuncs.com:3717" # 测试服
# MONGO_HOST_PART  = "mongodb://root:@dds-wz982bab2e6c05b41845-pub.mongodb.rds.aliyuncs.com:3717" # 正式服
MONGO_HOST_AUTH_DB = "admin"
MONGO_HOST_REPLICA_SET = None

MONGO_HOST = MONGO_HOST_PART + "/" + MONGO_HOST_AUTH_DB
MONGO_DB_NAME = 'nightcrawler'

register_connection(db=MONGO_DB_NAME, host=MONGO_HOST_PART, authentication_source=MONGO_HOST_AUTH_DB, replicaset=None, alias=connection.DEFAULT_CONNECTION_NAME)


def get_new_keyword_code(cate_attr_code, keyword_name):
    """
    生成新的类型编码

    :param keyword_name: 二级分类名称
    :param cate_attr_code: 一级分类代码
    :return:
    """
    dict_type = {
        "kind": "KI_",
        "function": "FN_",
        "disease": "DI_",
        "brand": "BR_",
    }
    head_code = dict_type.get(cate_attr_code, None)
    body_str = shortuuid.random(length=10)
    if cate_attr_code == "brand":
        body_str = yinjie(keyword_name)

    return head_code + str(body_str)


# 带声调的(默认)
def yinjie(word):
    """
    返还带声调的拼音字符

    :param word:
    :return: 例如 xia3oyi2ngua4n
    """
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.Style.TONE2):
        s = s + ''.join(i)
    return f"{s}_{shortuuid.random(length=5)}"

def get_new_brand_id(brand_name):
    return f"BR_{yinjie(brand_name)}"


if __name__ == "__main__":
    log = logger
    product_dao = ProductDao(log=log)
    # 获取所有品牌名称
    brands = product_dao.aggregate_type(field_name="brand")
    for brand in brands:
        brand_name = brand.get("name")
        # 根据品牌名称生成品牌id
        new_brand_id = get_new_brand_id(brand_name)
        # 更新数据mongo品牌id
        res = product_dao.update_brand_id(brand_name=brand_name,new_brand_id=new_brand_id)
        if res:
            log.info(f"brand_name:{brand_name},new_brand_id:{new_brand_id},更新成功")
        else:
            log.info(f"brand_name:{brand_name},new_brand_id:{new_brand_id},更新失败")





