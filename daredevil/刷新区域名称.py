from mongoengine import register_connection, connection

from daredevil.mongodb.dao.wx_contacts import WxContactsDao
from my_log import logger

# MONGO_HOST_PART = "mongodb://root:Pzzh4Admin@192.168.1.230"  # 230
MONGO_HOST_PART = "mongodb://root:Pzzh4Admin@dds-wz9db3743e6de5041152-pub.mongodb.rds.aliyuncs.com:3717" # 测试服
# MONGO_HOST_PART  = "mongodb://root:pzzh123456@dds-wz982bab2e6c05b41845-pub.mongodb.rds.aliyuncs.com:3717" # 正式服
MONGO_HOST_AUTH_DB = "admin"
MONGO_HOST_REPLICA_SET = None

MONGO_HOST = MONGO_HOST_PART + "/" + MONGO_HOST_AUTH_DB
MONGO_DB_NAME = 'daredevil'

register_connection(db=MONGO_DB_NAME, host=MONGO_HOST_PART, authentication_source=MONGO_HOST_AUTH_DB, replicaset=None, alias=connection.DEFAULT_CONNECTION_NAME)

# def get_new_、

if __name__ == "__main__":
    log = logger
    wx_contact_dao = WxContactsDao(log=log)

    # 获取所有联系人
    wx_contacts = wx_contact_dao.get_all_list()

    # 地区数据转换

    for wx_contact_obj in wx_contacts:

        region_name = wx_contact_obj.regionName
        country = ''
        province = ''
        city = ''
        if region_name:
            region_data = region_name.split("_")

            if len(region_data) >= 3:
                country = region_data[0]  # 国家
                province = region_data[1]  # 省份
                city = region_data[2]  # 城市
            elif len(region_data) == 2:
                country = region_data[0]  # 国家
                province = region_data[1]  # 省份
            elif len(region_data) == 1:
                country = region_data[0]  # 国家
            region_msg = {
                "country": country,
                "province": province,
                "city": city,
            }

            is_ok = wx_contact_dao.update_region_name(contact_id=wx_contact_obj.contact_id,region_msg=region_msg)

            log.info(f"contact_id:{wx_contact_obj.contact_id}, region_msg:{region_msg} is_ok:{is_ok}")
