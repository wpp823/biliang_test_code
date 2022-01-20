
# from pzutil.tornado.base_app import get_mongo
import pandas as pd

# MONGO_HOST_PART = "mongodb://root:pzzh123456@dds-wz982bab2e6c05b41845-pub.mongodb.rds.aliyuncs.com:3717,dds-wz982bab2e6c05b42390-pub.mongodb.rds.aliyuncs.com:3717"
# MONGO_HOST_REPLICA_SET = "mgset-2388361"
#
# MONGO_HOST_AUTH_DB = "admin"
# MONGO_HOST = MONGO_HOST_PART + "/" + MONGO_HOST_AUTH_DB + "?replicaSet=" + MONGO_HOST_REPLICA_SET
# MONGO_DB_NAME = 'nightcrawler'
# from utils.logger import get_logger
import pymongo

MONGO_HOST_PART = "mongodb://root:Pzzh4Admin@192.168.1.230"
MONGO_HOST_AUTH_DB = "admin"
MONGO_HOST_REPLICA_SET = None

MONGO_HOST = MONGO_HOST_PART + "/" + MONGO_HOST_AUTH_DB
MONGO_DB_NAME = 'nightcrawler'


class Tools:
    def __init__(self):


        query = {'age': {'$lt': 25}}

        self.conn = pymongo.MongoClient(MONGO_HOST)
        self.db = self.conn["nightcrawler"]
        # self._log = get_logger(name='NC_Tool.log')

        # self._db = get_mongo(host=MONGO_HOST_PART,
        #                      db=MONGO_DB_NAME,
        #                      host_uri=MONGO_HOST,
        #                      authentication_source=MONGO_HOST_AUTH_DB,
        #                      replicaset=MONGO_HOST_REPLICA_SET,
        #                      log=self._log
        #                      )
        # self._log.info("[Statics_init]")

    def expect_data_to_files(self):
        # 连接mongodb数据库
        # client = pymongo.MongoClient("localhost")
        # 连接数据库
        # db = self._db["nightcrawler"]
        # # 数据表
        mycol= self.db["products"]
        # 将mongodb中的数据读出

        # my_condition = {"type": 49, "msg_content.desc": "[聊天记录]"}
        data = mycol.find().limit(10)

        data = pd.DataFrame(data)

        # 保存为csv格式
        data.to_csv('data.csv', encoding='utf-8')
        # 保存为xls格式
        data.to_excel('data.xls', encoding='utf-8')

    def get_cates(self):
        db = self.db["nightcrawler"]
        # # 数据表
        mycol = db["products"]
        # conn = pymongo.MongoClient('mongodb://localhost:27017')
        return mycol.find().distinct('kind')

if __name__ == "__main__":
    tools = Tools()
    # tools.expect_data_to_files()
    data = tools.get_cates()

    print(data)