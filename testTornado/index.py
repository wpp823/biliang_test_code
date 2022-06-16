#! /usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        lst = ["python", "www.itdiffer.com", "qiwsir@gmail.com"]  # 定义一个list
        self.render("index.html", info=lst)  # 将上述定义的list传给模板


class Testhandler(tornado.web.RequestHandler):
    def get(self):
        data_items = [{'product_id': '芙清密钥丝揉控油持装粉底液', 'sku_id': '通用', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id', 'compare_price': 19800},
                      {'product_id': '芙清医用促愈功能性敷料综合治疗凝胶', 'sku_id': '芙清凝胶（30g装）', 'code': 1101, 'ext_url': 'https://detail.tmall.com/item.htm?id=587053192746',
                       'error_msg': 'ext_url地址中缺失淘宝商品skuid', 'compare_price': 19800},
                      {'product_id': '百植萃舒缓清透防晒乳', 'sku_id': '40g', 'code': 200, 'ext_url': 'https://detail.tmall.com/item.htm?id=638596607382', 'error_msg': '对比淘宝/天猫 1000',
                       'compare_price': 14800},
                      {'product_id': '百植萃维B5烟酰胺护手霜', 'sku_id': '40g', 'code': 200, 'ext_url': 'https://detail.tmall.com/item.htm?id=629322805063', 'error_msg': '对比淘宝/天猫 1000',
                       'compare_price': 5800},
                      {'product_id': '百植萃维B5烟酰胺保湿修护身体乳', 'sku_id': '190g', 'code': 200, 'ext_url': 'https://detail.tmall.com/item.htm?id=628985420585', 'error_msg': '对比淘宝/天猫 1000',
                       'compare_price': 17800},
                      {'product_id': '百植萃维生素B5富勒烯保湿面霜', 'sku_id': '50g', 'code': 200, 'ext_url': 'https://detail.tmall.com/item.htm?id=610298426180', 'error_msg': '对比淘宝/天猫 1000',
                       'compare_price': 38800},
                      {'product_id': '百植萃复合果酸精华水', 'sku_id': '200ml', 'code': 200, 'ext_url': 'https://detail.tmall.com/item.htm?id=613619288368', 'error_msg': '对比淘宝/天猫 1000',
                       'compare_price': 17800},
                      {'product_id': '百植萃玻色因塑颜紧致面部精华液', 'sku_id': '30ml', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id', 'compare_price': 17800},
                      {'product_id': '浅草川水光防晒喷雾', 'sku_id': '一盒装', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id', 'compare_price': 17800},
                      {'product_id': '薇诺娜舒敏保湿特护霜', 'sku_id': '敏感性肤质,50g', 'code': 200, 'ext_url': 'https://detail.tmall.com/item.htm?id=17289238843&skuId=37155583560',
                       'error_msg': '对比淘宝/天猫 26800', 'compare_price': 17800},
                      {'product_id': '薇诺娜清透防晒乳50g SPF48 PA+++ ', 'sku_id': '基本款,50g', 'code': 1102, 'ext_url': 'https://detail.tmall.com/item.htm?id=2453766859',
                       'error_msg': '优客api返回数据中,匹配价格数据失败', 'compare_price': 18800},
                      {'product_id': '芙清卡波姆湿性修复功能性敷料', 'sku_id': '祛痘清洁黑膜1盒/5片', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id', 'compare_price': 55200},
                      {'product_id': '百植萃鱼子精华紧致眼霜', 'sku_id': '14g', 'code': 200, 'ext_url': 'https://detail.tmall.com/item.htm?id=622247786852', 'error_msg': '对比淘宝/天猫 4000',
                       'compare_price': 28800},
                      {'product_id': '小银罐修复膏·肌肤治愈专家 植物配方中药制作去痒消红抑制炎症', 'sku_id': '10g', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id', 'compare_price': 26800},
                      {'product_id': '激素依赖性皮炎屏障修复护理套装', 'sku_id': '激素依赖性皮炎护理套装（敷料+特护霜+洁面乳）', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id',
                       'compare_price': 28300},
                      {'product_id': '过敏性皮炎补水消炎舒缓套装', 'sku_id': '过敏性皮炎护理套装（敷料+喷雾+特护霜）', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id', 'compare_price': 15800},
                      {'product_id': '黄褐斑改善皮肤屏障抗炎修护套装', 'sku_id': '黄褐斑护理套装（精华液+面膜+防晒乳+面霜+修护水）', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id',
                       'compare_price': 26800}, {'product_id': '黄褐斑改善皮肤屏障抗炎修护套装', 'sku_id': '百植萃舒缓清透防晒乳1支（40g）', 'code': 200,
                                                 'ext_url': 'https://detail.tmall.com/item.htm?id=638596607382&skuId=4750921755750', 'error_msg': '对比淘宝/天猫 1000',
                                                 'compare_price': 14800}, {'product_id': '黄褐斑改善皮肤屏障抗炎修护套装', 'sku_id': '百植萃维生素B5富勒烯保湿面霜1罐（50g）', 'code': 200,
                                                                           'ext_url': 'https://detail.tmall.com/item.htm?id=610298426180&skuId=4462577855874',
                                                                           'error_msg': '对比淘宝/天猫 1000', 'compare_price': 38800},
                      {'product_id': '皮肤干燥补水保湿防晒润肤护理套装', 'sku_id': '皮肤干燥护理套装（面膜+精华水+面霜+面乳+防晒霜）', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id',
                       'compare_price': 26800}, {'product_id': '皮肤干燥补水保湿防晒润肤护理套装', 'sku_id': '百植萃维生素B5富勒烯保湿面霜1罐（50g）', 'code': 200,
                                                 'ext_url': 'https://detail.tmall.com/item.htm?id=610298426180&skuId=4462577855874', 'error_msg': '对比淘宝/天猫 1000',
                                                 'compare_price': 38800},
                      {'product_id': '痤疮抑菌消毒控油防痘护理套装', 'sku_id': '痤疮护理套装（除菌水+修护膏+敷料）', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id', 'compare_price': 13800},
                      {'product_id': '痤疮抑菌消毒控油防痘护理套装', 'sku_id': '小银罐修护膏1罐（10g）', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id', 'compare_price': 13800},
                      {'product_id': '雅清芙姿医用冷敷贴', 'sku_id': '25ml*6片【院线正品】', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id', 'compare_price': 12800},
                      {'product_id': '雅清芙姿金胚癢敏舒液体敷料', 'sku_id': '120ml【院线正品】', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id', 'compare_price': 6800},
                      {'product_id': '舒缓控油凝露', 'sku_id': '50g', 'code': 1100, 'ext_url': '', 'error_msg': 'ext_url地址中缺失淘宝商品id', 'compare_price': 6800}]
        self.render("nightcrawler_product_price.html", data_items=data_items)  # 将上述定义的list传给模板


class Demo2handler(tornado.web.RequestHandler):
    def get(self):
        data_items = [{
            "order_id": 3203261565093544192,
            "create_time": "2022-05-12 00:00:01",
            "start_time": "2022-05-12 00:00:01",
            "end_time": "2022-05-12 00:00:01",
            "products": [
                {
                    "product_name": "森花泉古方草本护肤系列 天门冬面膜45分钟直达真皮银耳深度补水",
                    "sku_name": "润泽补水面膜5片",
                    "sku_num": 1,
                }
            ],
            "order_price": float(16800 / 100)
        },
            {
                "order_id": 3203261884760589568,
                "create_time": "2022-05-12 00:00:01",
                "start_time": "2022-05-12 00:00:01",
                "end_time": "2022-05-12 00:00:01",
                "products": [
                    {
                        "product_name": "可预类人胶原蛋白修复敷料",
                        "sku_name": "50g【院线正品】",
                        "sku_num": 1,
                    },
                    {
                        "product_name": "可复美类人胶原蛋白敷料（蓝色非面膜5片）",
                        "sku_name": "类人胶原蛋白敷料1盒（5片装)【院线正品】",
                        "sku_num": 2,
                    },
                ],

                "order_price": float(48400 / 100)
            },

            {
                "order_id": 3203262659680010752,
                "create_time": "2022-05-12 00:00:01",
                "start_time": "2022-05-12 00:00:01",
                "end_time": "2022-05-12 00:00:01",
                "products": [
                    {
                        "product_name": "雅清芙姿金胚去屑止痒洗发液",
                        "sku_name": "200ml【院线正品】",
                        "sku_num": 1,
                    }
                ],

                "order_price": float(5900 / 100)
            },
            {
                "order_id": 3203263674119358464,
                "create_time": "2022-05-12 00:00:01",
                "start_time": "2022-05-12 00:00:01",
                "end_time": "2022-05-12 00:00:01",
                "products": [
                    {
                        "product_name": "优斐斯传明酸修护精华液",
                        "sku_name": "30mL",
                        "sku_num": 1,
                    }
                ],
                "order_price": float(28900 / 100)
            },
        ]

        self.render("nightcrawler_wx_order.html", data_items=data_items)  # 将上述定义的list传给模板


handlers = [(r"/", IndexHandler),
            (r"/test", Testhandler),
            (r"/demo2", Demo2handler),

            ]

# template_path = os.path.join(os.path.dirname(__file__), "temploop")  # 模板路径
template_path = '/Users/wyy/Desktop/codes/mytest/testTornado/temploop'  # 模板路径

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers, template_path)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
