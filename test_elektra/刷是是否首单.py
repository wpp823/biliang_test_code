import requests
from mongoengine import register_connection, connection

from mongo_db.dao.doctor_incomes_orders import DoctorIncomesOrdersDao
from my_log import get_logger

# MONGO_HOST_PART = "mongodb://root:Pzzh4Admin@192.168.1.230"  # 230
MONGO_HOST_PART = "mongodb://root:Pzzh4Admin@dds-wz9db3743e6de5041152-pub.mongodb.rds.aliyuncs.com:3717" # 测试服
# MONGO_HOST_PART  = "mongodb://root:pzzh123456@dds-wz982bab2e6c05b41845-pub.mongodb.rds.aliyuncs.com:3717" # 正式服
MONGO_HOST_AUTH_DB = "admin"
MONGO_HOST_REPLICA_SET = None

MONGO_HOST = MONGO_HOST_PART + "/" + MONGO_HOST_AUTH_DB
MONGO_DB_NAME = 'elektra'

register_connection(db=MONGO_DB_NAME, host=MONGO_HOST_PART, authentication_source=MONGO_HOST_AUTH_DB, replicaset=None, alias=connection.DEFAULT_CONNECTION_NAME)


def get_is_first_order(order_id):
    """
    生成新的类型编码

    :param keyword_name: 二级分类名称
    :param cate_attr_code: 一级分类代码
    :return:
    """

    api = "http://127.0.0.1:18851/in/mnc/api/v1/order/info"
    # param = order_id
    url = f"{api}?order_id={order_id}"
    response = requests.get(url)
    is_first = None
    if response:
        data = response.json().get("data", None)
        if data:
            is_first = data.get("is_first")
            # return is_first

    return is_first


if __name__ == "__main__":
    log = get_logger()
    doc_income_dao = DoctorIncomesOrdersDao(log=log)
    # 获取所有品牌名称
    order_data = doc_income_dao.get_product_order()
    # brands = product_dao.aggregate_type(field_name="brand")

    for order in order_data:
        order_id = order.product_data.order_id
        # 根据品牌名称生成品牌id
        order_is_first = get_is_first_order(order_id)
        # 更新数据mongo品牌id
        if order_is_first is not None:
            res = doc_income_dao.update_order_is_first(wx_order_id=order_id, is_first=order_is_first)
            if res:
                log.info(f"order_id:{order_id},is_first:{order_is_first},更新成功")
            else:
                log.info(f"order_id:{order_id},is_first:{order_is_first},更新失败")
