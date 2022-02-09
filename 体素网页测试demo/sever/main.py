import tornado.ioloop
import tornado.web


# 定义处理类型
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
    app = tornado.web.Application([(r'/', IndexHandler)])
    # 绑定一个监听端口
    app.listen(8888)
    # 启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()
