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
        # res_data = {'code': 200, 'msg': '',
        #             'request_id': 'MTY0NDQ2MzgzMS43MDIzNzM=',
        #             'data': {'version': 'derms-v1.2.1', 'request_id': 'MTY0NDQ2MzgzMS43MDIzNzM=',
        #                      'face_box': {'x0': 174, 'y0': 132, 'x1': 589, 'y1': 711},
        #                      'skin_age': 31,
        #                      'original_image': 'https://wechat-skin-v1-prod.oss-cn-shanghai.aliyuncs.com/results%2F2022-02-10%2FMTY0NDQ2MzgzMS43MDIzNzM%3D%2Forigin_image.jpg?OSSAccessKeyId=LTAI4G8HUwXM84nxSgadaVLP&Expires=1644464134&Signature=iSZ2vEfmt5cJLPOpXyThJKhaJ5o%3D',
        #                      'face_crop': 'https://wechat-skin-v1-prod.oss-cn-shanghai.aliyuncs.com/results%2F2022-02-10%2FMTY0NDQ2MzgzMS43MDIzNzM%3D%2Fface_crop.jpg?x-oss-process=image%2Fresize%2Cm_fill%2Ch_240%2Cw_240%2Climit_0&OSSAccessKeyId=LTAI4G8HUwXM84nxSgadaVLP&Expires=1644464134&Signature=eHGFy4Y%2BROakyuXZ66meawpU1e8%3D',
        #                      'overall_score': 91,
        #                      'color': {'result': 'baixi',
        #                                'wiki': '人的肤色主要由两个因素决定：皮肤内各种色素的含量；表皮的厚度和光线在皮肤表面的散射情况。只有从这两个因素着手，才可以让皮肤呈现白皙、细腻、完美无瑕的肤色。皮肤血液循环状态、皮肤表面光线反射、不良生活习惯及精神神经因素都会影响皮肤颜色。“白里透红”是亚洲人理想和健康的皮肤颜色。',
        #                                'tips': '你拥有较为白皙的肤色。穿衣搭配对大多数风格都能hold住，真令人羡慕呢。不过肤色越白意味着皮肤黑色素含量越低。黑色素的主要作用是吸收紫外线，因此你对紫外线抵抗能力较弱，平时一定要注意做好防晒，保持充足的睡眠，适度的运动。'},
        #                      'skin_type': {'score': 62,
        #                                    'category': [{'cls': 'forehead', 'type': 'mid', 'score': 65},
        #                                                 {'cls': 'nose', 'type': 'oil', 'score': 66},
        #                                                 {'cls': 'left_cheek', 'type': 'oil', 'score': 70},
        #                                                 {'cls': 'right_cheek', 'type': 'mid', 'score': 48},
        #                                                 {'cls': 'chin', 'type': 'oil', 'score': 66}],
        #                                    'type': 'oil',
        #                                    'wiki': '干性、中性和油性皮肤的分法，主要来自于皮脂分泌量的区别。\n中性皮肤：皮脂分泌量正常，皮肤角质层水含量正常（10-20%），皮肤紧致，有弹性，表面光滑润泽，细腻，是最理想的皮肤状态，一般只有婴幼儿和青少年才能拥有该类肤质。\n干性皮肤：皮脂分泌量低，皮肤角质层水含量低（<10%）,皮肤干燥脱屑，细腻但无光泽，肤色晦暗，易出现细小皱纹，色素沉着。\n油性皮肤：皮脂分泌量大，皮肤角质层含水量正常或者偏低，皮肤表面油腻，有光泽，毛孔粗大，易发生痤疮、毛囊炎。\n中性肌肤：皮肤皮脂腺和汗腺分泌较平衡，皮肤可以形成健康的皮脂末角质层保存适量的水分。但皮肤容易受到季节、环境、身体状况的影响而发生变化。\n混合性肌肤：在脸部的不同部位出现干性和油性的双重特征，皮肤虽也会出现夏季偏油、冬季偏干的状况，但T字区(前额、鼻翼和下巴)偏油，两颊偏干。',
        #                                    'tips': '你属于中性偏油的皮肤。平时用35°的温水清洁，使用产品的清洁力略高，每2周可以做一次去角质。选用收敛控油的化妆水，选择带有控油功能的保湿乳液或者啫喱，尽量选择防晒乳液（防晒霜过于厚重），适当使用防晒喷雾，结合稍微控油的保湿，是你这类肤质的工作重点。'},
        #                      'sensitive': {'score': 1, 'type': 'tolerance',
        #                                    'wiki': '敏感性肌肤的特征\n1.皮肤表皮薄，皮脂分泌少，较干燥，微血管明显，皮肤呈现干燥机能减退，角质层保持水分的能力降低，肌肤表面的皮脂膜形成不完全。  \n2.接触化妆品或季节过敏后易引起皮肤过敏，出现红、肿、 痒。皮肤缺乏光泽，脸颊易充血红肿。  \n3.因季节变化而使皮肤容易呈现不稳定的状态。主要症状是搔痒、烧灼感、刺痛、皮肤发痒和出小疹子。  \n4.容易受冷风、食物、水质、紫外线、合成纤维、香味等外在环境或物质的影响。  \n5.单接触到刺激性物质就会引发肌肤的问题。对阳光、气候、水、植物（花粉）、化妆品、香水、蚊虫叮咬及高蛋白食物都有可能导致过敏。 ',
        #                                    'tips': '无敏感情况，皮肤屏障功能良好，对寒冷、炎热、化妆品、酒精或药物等外界刺激无反应。平时合理清洁、适度保湿、加强防晒、保持合理水分即可。'},
        #                      'dark_circle': {'problem_score': 66,
        #                                      'type': 'HHX',
        #                                      'wiki': '黑眼圈有三种：色素型，血管型、阴影型。\n色素型黑眼圈：日晒、眼周皮肤病、皮肤损伤、化妆品沉积等黑色素过度沉积引起眼圈周围颜色加深。\n血管型黑眼圈：眼睛周围的皮肤很薄，如果局部血液循环不好，血液中去氧的血红蛋白增多，血管通过眼睑皮肤透出青紫色，造成颜色黯淡。\n阴影型黑眼圈：眼睛周围的皮肤下垂、肌肉松弛、导致眼袋突出，造成局部阴影，让人看起来好像有很重的黑眼圈，其实是眼睛周围的结构发生变化，形成阴影，造成黑眼圈。',
        #                                      'tips': '你有混合型黑眼圈，平时可以通过在眼睛周围涂抹维生素E、K1和视黄醇混合物或者热敷来改善眼部血液循环。平时还要注意防晒，出门戴太阳镜、涂防晒霜，使用柔和的眼部化妆品，及时卸妆等来预防。还有注意不要熬夜、不要过度用眼，保证足够的睡眠，平时仰睡和不要用力揉眼都有利于缓解混合型黑眼圈。'},
        #                      'pore': {'problem_score': 0, 'wiki': '毛孔粗大的原因来自于皮脂分泌旺盛，多余的油脂不能及时清除，进而堵塞毛孔，使毛孔膨胀，造成皮肤弹性松弛，最后毛囊粗大。此外，慢性复发性痤疮、性激素、抽烟喝酒、睡眠不足和不当皮肤护理都可影响毛孔大小。',
        #                               'tips': '没有毛孔粗大的情况。以预防为主，平时坚持运动（如跑步、快走一类的有氧运动），减少糖分及牛奶的摄入，减少熬夜，保持规律作息，降低工作压力，饮食均衡即可。'},
        #                      'wrinkle': {'problem_score': 15,
        #                                  'filename': 'https://wechat-skin-v1-prod.oss-cn-shanghai.aliyuncs.com/results%2F2022-02-10%2FMTY0NDQ2MzgzMS43MDIzNzM%3D%2Fwrinkle_image.jpg?OSSAccessKeyId=LTAI4G8HUwXM84nxSgadaVLP&Expires=1644464135&Signature=Z50SmAgbRe8YMDygGvJZBw448E4%3D',
        #                                  'category': [{'cls': 'forehead',
        #                                                'problem_score': 0,
        #                                                'level': 'none'},
        #                                               {'cls': 'eyecorner',
        #                                                'problem_score': 10,
        #                                                'level': 'lightly'},
        #                                               {'cls': 'crowfeet',
        #                                                'problem_score': 0,
        #                                                'level': 'none'},
        #                                               {'cls': 'glabella',
        #                                                'problem_score': 0,
        #                                                'level': 'none'},
        #                                               {'cls': 'nasolabial',
        #                                                'problem_score': 84,
        #                                                'level': 'lightly'}],
        #                                  'wiki': '皱纹的形成：皮肤的正常衰老、皮肤附属器官功能的自然衰退、皮肤的新陈代谢减慢，使得真皮层的弹性纤维和胶原纤维逐渐老化，使皮肤的张力和弹力减弱；丰富的面部表情；长期的睡眠不足、皮肤缺水、不当的减肥、缺乏体育锻炼；化妆品的使用不当、烟酒的刺激。\n皱纹分为真性皱纹和假性皱纹。真性皱纹是面部形成的非手术或注射不能祛除的稳定性皱纹，此种皮肤的胶原纤维和弹力纤维性能下降，导致皮肤失去韧性和弹性；假性皱纹是面部出现的不稳定性的皱纹，是由于皮肤暂时性的缺水或缺乏油脂滋润引起的，这类皱纹可以通过皮肤弹性的自我调节或通过皮肤护理在一定时间内自行消退。\n\n',
        #                                  'tips': '你有轻微的眼下细纹，表现为皮纹加深，刚可辨认，似折痕虚。如因水份不足引起，请使用滋润眼霜轻轻按摩；如因眼过度引起，请不要过度使用眼睛，要经常放松，眺望远方；如因血液循环不佳引起，可以多运动，或者用发热眼罩等热敷。'},
        #                      'blackhead': {'problem_score': 0,
        #                                    'wiki': '黑头称开放性粉刺 ，主要是由皮脂、细胞屑和细菌组成的一种“栓”样物，阻塞在毛囊开口处而形成的，加上空气中的尘埃、污垢和氧化作用，使其接触空气的一头逐渐变黑，经氧化后成为黑色的小点，这些小点就是被称作黑头的油脂阻塞物。',
        #                                    'tips': '没有黑头，以预防为主。 少吃糖，少喝含糖饮料，比如奶茶，可乐；少吃盐，不要吃盐含量太高的食物；减轻自身压力，增加运动，调节工作节奏。'},
        #                      'roughness': {'problem_score': 5,
        #                                    'wiki': '影响皮肤表面状态的粗燥与平滑度的因素很多，常见的有皮肤水分油分、斑点、纹理（皱纹）等。皮肤表面纹理细小、表浅，且走向柔和是青春美丽的皮肤外观。但随着年龄的增加和环境因素的影响，皮肤纹理会逐渐增大、增粗，皱纹形成并逐渐加深。',
        #                                    'tips': '你的皮肤非常光滑，请继续保持哟。'},
        #                      'problem_bubbles': [{'name': 'dark_circle', 'score': 66},
        #                                          {'name': 'wrinkle', 'score': 15},
        #                                          {'name': 'roughness', 'score': 5},
        #                                          {'name': 'pore', 'score': 0},
        #                                          {'name': 'blackhead', 'score': 0}]
        #                      }
        #             }
        try:
            # requests = self.request
            img_files = self.request.files.get("file", [])
            img_buf = img_files[0].get("body")
            img_base64 = "data:image/jpg;base64," + base64.b64encode(img_buf).decode()
            res_data = tisu_api.post_base64_img(img_base64=img_base64)
            if res_data:
                res_data = FaceSkinItem(**res_data["data"])
                log.info("[IndexHandler.post][get_img_ret_data_ok][res_data:{}]".format(res_data))
                face_skin_dao.add(res_data)
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
