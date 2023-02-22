import pymongo

from my_log import get_logger

# from my_log import logger

MONGO_HOST_PART = ""  # 230
# MONGO_HOST_PART  = "" # 测试服
# MONGO_HOST_PART  = "" # 正式服
MONGO_HOST_AUTH_DB = "admin"
MONGO_HOST_REPLICA_SET = None

MONGO_HOST = MONGO_HOST_PART + "/" + MONGO_HOST_AUTH_DB
MONGO_DB_NAME = 'nightcrawler'

# register_connection(db=MONGO_DB_NAME, host=MONGO_HOST_PART, authentication_source=MONGO_HOST_AUTH_DB, replicaset=None, alias=connection.DEFAULT_CONNECTION_NAME)

# def get_new_data_type():
#

if __name__ == "__main__":
    log = get_logger()

    my_client = pymongo.MongoClient(host=MONGO_HOST_PART)
    my_db = my_client['nightcrawler']
    products = my_db['products']
    data = products.find()

    for product in data:
        brand = product.get("brand")
        log.info(brand)
        product_id = product.get("product_id")
        if type(brand) is dict:
            log.info(brand)
            products.update_one(
                filter={
                    "product_id": product_id
                },
                update={"$set": {"brand": [brand]}}
            )

    # product_dao = ProductDao(log=log)
    # # 获取所有品牌名称
    # fields = [ProductModel.product_id.name, ProductModel.brand.name]
    # brands_data = product_dao.get_product_list(fields=fields)
    # try:
    #     for brand in brands_data:
    #
    #         log.info(type(brand.brand))
    #         if type(brand.brand) is not EmbeddedDocumentList:
    #             product_id = brand.product_id
    #             new_data = [brand.brand]
    #             # 根据品牌名称生成品牌id
    #             # 更新数据mongo品牌id
    #             res = product_dao.update_brand_type(product_id=product_id, new_data=new_data)
    #             if res:
    #                 log.info(f"product_id:{product_id},new_data:{new_data},更新成功")
    #             else:
    #                 log.info(f"product_id:{product_id},new_data:{new_data},更新失败")
    # except InvalidDocumentError:
    #     log.info(type(brand.brand))
