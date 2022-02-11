import base64
import re

import tornado.ioloop
import tornado.web
from mongoengine import register_connection, connection

from mongodb.dao.face_skins import FaceSkinsDao
from my_log import get_logger
from utils.skinanalysis import SkinAnalysis, FaceSkinItem

log = get_logger()

MONGO_HOST_PART = "mongodb://root:Pzzh4Admin@192.168.1.230"  # 230
# MONGO_HOST_PART  = "mongodb://root:Pzzh4Admin@dds-wz9db3743e6de5041152-pub.mongodb.rds.aliyuncs.com:3717" # 测试服
# MONGO_HOST_PART  = "mongodb://root:pzzh123456@dds-wz982bab2e6c05b41845-pub.mongodb.rds.aliyuncs.com:3717" # 正式服
MONGO_HOST_AUTH_DB = "admin"
MONGO_HOST_REPLICA_SET = None

MONGO_HOST = MONGO_HOST_PART + "/" + MONGO_HOST_AUTH_DB
MONGO_DB_NAME = 'elektra'

SECRET_KEY = 'FEaPlMdDr9bLcIo2'
ACCESSKEY_SECRET = 'jdr9Z9sicCDbwbMXSq0QRAAsvTH0G6'


class BaseHandler(tornado.web.RequestHandler):
    #  允许跨域访问的地址

    def allowMyOrigin(self):
        allow_list = [
            'http://127.0.0.1:63342',
        ]
        if 'Origin' in self.request.headers:
            Origin = self.request.headers['Origin']
            # 域名
            re_ret = re.match(r".{1,}\.(xixi.com|haha.com)", Origin)
            # 内网和本地
            re_ret2 = re.match(r"^(192.168.1.*|127.0.0.1.*|192.168.2.*)", Origin)
            if re_ret or re_ret2 or Origin in allow_list:
                self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名也可以是*
                self.set_header("Access-Control-Allow-Headers", "x-requested-with,content-type")
                self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')


# 定义处理类型
class TestHandler(BaseHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名也可以是*
        self.set_header("Access-Control-Allow-Headers", "x-requested-with,content-type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    # 添加一个处理get请求方式的方法
    def get(self):
        print(self.request.body)
        # 向响应中，添加数据
        self.write('好看的皮囊千篇一律，有趣的灵魂万里挑一。')

    def post(self):
        # self.set_default_headers()
        print(len(self.request.body))
        self.write('好看的皮囊千篇一律，有趣的灵魂万里挑一。')


class IndexHandler(tornado.web.RequestHandler):
    # 添加一个处理get请求方式的方法

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名也可以是*
        self.set_header("Access-Control-Allow-Headers", "x-requested-with,content-type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        result = self.get_img_ret_data()
        log.info(result)
        self.write(result)

    def get_img_ret_data(self):
        """
            获取到体素肤质识别结果存入mongo，返回前端
        :return:
        """
        code = 'fail'
        face_skin_dao = FaceSkinsDao(log=log)
        tisu_api = SkinAnalysis(secret_key='jdr9Z9sicCDbwbMXSq0QRAAsvTH0G6', access_key='FEaPlMdDr9bLcIo2', log=log)
        res_data = None

        try:
            # requests = self.request
            img_files = self.request.files.get("file", [])
            img_buf = img_files[0].get("body")
            img_base64 = "data:image/jpg;base64," + base64.b64encode(img_buf).decode()
            res_data = tisu_api.post_base64_img(img_base64=img_base64)
            if res_data:
                # res_data = FaceSkinItem(**data) # fixme
                log.info("[IndexHandler.post][get_img_ret_data_ok][res_data:{}]".format(res_data))
                res = face_skin_dao.add(res_data)
                if res:
                    log.info("[IndexHandler.post][face_skin_dao.add][res:{}]".format(res))
                else:
                    log.error("[IndexHandler.post][face_skin_dao.add_fail][res:{}]".format(res))
                code = 'ok'
            else:
                log.error("[IndexHandler.post][get_img_ret_data_ok][res_data:{}]".format(res_data))
        except:
            log.exception("[IndexHandler.post]")
        ret_data = {
            "code": code,
            "data": res_data
        }
        return ret_data


if __name__ == '__main__':
    # 创建一个应用对象

    register_connection(db=MONGO_DB_NAME, host=MONGO_HOST_PART, authentication_source=MONGO_HOST_AUTH_DB, replicaset=None, alias=connection.DEFAULT_CONNECTION_NAME)

    app = tornado.web.Application([(r'/test', TestHandler),
                                   (r'/upload', IndexHandler)])
    # 绑定一个监听端口
    app.listen(8888)
    # 启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()
