import re

import tornado.ioloop
import tornado.web

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
                self.set_header("Access-Control-Allow-Origin", Origin)  # 这个地方可以写域名也可以是*
                self.set_header("Access-Control-Allow-Headers", "x-requested-with")
                self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
# 定义处理类型
class TestHandler(BaseHandler):

    def set_default_headers(self):
        self.allowMyOrigin()
    # 添加一个处理get请求方式的方法
    def get(self):
        print(self.request.body)
        # 向响应中，添加数据
        self.write('好看的皮囊千篇一律，有趣的灵魂万里挑一。')

    def post(self):
        print(self.request.body)
        self.write('好看的皮囊千篇一律，有趣的灵魂万里挑一。')



class IndexHandler(tornado.web.RequestHandler):
    # 添加一个处理get请求方式的方法
    def get(self):
        # 向响应中，添加数据
        self.write('好看的皮囊千篇一律，有趣的灵魂万里挑一。')

    def post(self):
        result = self.get_img_ret_data()

        self.write(result)

    def get_img_ret_data(self):
        """

        :return:
        """
        ret_data = {
            "code": ""
        }

        return ret_data


if __name__ == '__main__':
    # 创建一个应用对象
    app = tornado.web.Application([(r'/test', TestHandler),(r'/upload/img',IndexHandler)])
    # 绑定一个监听端口
    app.listen(8888)
    # 启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()
