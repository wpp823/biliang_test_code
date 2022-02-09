from mongoengine import *


class WikiObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    heading = StringField(help_text="标题")
    contents = StringField(help_text="内容")


class ClassificationObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    cn_dx = StringField(help_text="模型预测中文疾病名称")
    probability = FloatField(help_text="模型预测的概率")
    en_dx = StringField(help_text="模型预测英文疾病名称")
    cn_category = StringField(help_text="中文疾病分类")
    lesion_specs = StringField(help_text="皮肤损伤类型")
    cause = StringField(help_text="疾病的原因")
    abstract = StringField(help_text="疾病摘要")
    urgency_level = IntField(help_text="推荐的医疗紧急程度。1 表示不紧急，3 表示非常紧急")
    wiki = EmbeddedDocumentListField(WikiObj, help_text="中文疾病详细wiki,可能为空列表")


class FaceBoxObj(DynamicEmbeddedDocument):
    """
    脸部区域位置
    """
    x0 = IntField()
    y0 = IntField()
    x1 = IntField()
    y1 = IntField()


class CategoryObj(DynamicEmbeddedDocument):
    """
    mid（中性）
    dry（干性）
    oil（油性）
    """
    cls = StringField(help_text="面部区域")
    type = StringField(help_text="区域皮肤类型")
    level = StringField(help_text="程度")
    score = IntField(help_text="分数")


class SkinTypeObj(DynamicEmbeddedDocument):
    """
    面部区域
    forehead（额头）
    chin（下巴）
    left_cheek（左脸）
    right_cheek（右脸）
    nose（鼻梁）
    整体皮肤类型
    dry(干性) [0, 40)
    mid(中性) [40, 60)
    oil(油性) [60, 100]
    """
    score = IntField(help_text="总分")
    category = EmbeddedDocumentListField(CategoryObj, help_text="区域结果")
    type = StringField(help_text="整体皮肤类型")
    wiki = StringField(help_text="通用维基")
    tips = StringField(help_text="提示")


class ColorObj(DynamicEmbeddedDocument):
    """
    肤色结果

    - toubai（透白）色值：#f9e5d9
    - baixi（白皙）色值：#f2d5c3
    - ziran（自然）色值：#efc2a7
    - xiaomai（小麦）色值：#c19b88
    - anchen（暗沉）色值：#99715f
    - youhei（黝黑）色值：#684a4
    """
    result = StringField(help_text="肤色结果")
    wiki = StringField(help_text="通用描述")
    tips = StringField(help_text="肤色结果提示")


class SensitiveObj(DynamicEmbeddedDocument):
    """
    sensitive（敏感）
    tolerance（耐受）
    normal（中性）
    """

    score = StringField(help_text="分数")
    type = StringField(help_text="类型")
    tips = StringField(help_text="提示")
    wiki = StringField(help_text="通用描述")


class ProblemBubblesObj(DynamicEmbeddedDocument):
    name = StringField(help_text="气泡名称")
    score = IntField(help_text="气泡分数，越低越好 ")


class ProblemObj(DynamicEmbeddedDocument):
    problem_score = IntField(help_test="问题评分,越低越好")
    tips = StringField(help_text="提示")
    wiki = StringField(help_text="通用描述")


class WrinkleCarteObj(DynamicEmbeddedDocument):
    cls = StringField(help_text="皱纹区域")
    problem_score = IntField(help_text="问题评分，越低越好 ")


class WrinkleObj(DynamicEmbeddedDocument):
    problem_score = IntField(help_test="问题评分,越低越好")
    tips = StringField(help_text="提示")
    wiki = StringField(help_text="通用描述")
    filename = StringField(help_text="带有皱纹注释的图像的网址")
    category = EmbeddedDocumentListField(WrinkleCarteObj, help_text="皱纹类别")


class RoughnessObj(ProblemObj):
    score = IntField(help_test="整体问题得分,越低越好")
    # problem_score = IntField(help_test="问题评分,越低越好")
    # tips = StringField(help_text="提示")
    # wiki = StringField(help_text="通用描述")


class InflammationDxObj(DynamicEmbeddedDocument):
    problem_score = IntField(help_test="问题评分,越低越好")
    cn_dx = StringField(help_text="名称")
    formal_dx = StringField(help_text="医生提供的dx名称，选择oen显示 ")
    wiki = StringField(help_text="通用描述")
    treatment = ListField(help_text="治疗清单")
    reference_image = ListField(help_text="参考图像")


class InflammationObj(DynamicEmbeddedDocument):
    problem_score = IntField(help_test="问题评分,越低越好")
    dx_list = EmbeddedDocumentListField(InflammationDxObj, help_text="按问题分数降序排列的面部状况列表")


class AcneObj(WrinkleObj):
    stage = IntField(help_test="阶段")  # 0: 轻度, 1: 中度, 2: 重度


class SkinTestDataResult(DynamicEmbeddedDocument):
    meta = {
        'strict': False,
        "collection": "skin_test_result",
        'indexes': [
            {
                "fields": ["request_id"],
                "name": "_request_id_",
            },
        ]
    }

    SERVICE_VERSION = "dermx-1.2.1"
    request_id = StringField(help_text="请求id")
    version = StringField(help_text="服务版本")

    skin_age = IntField(help_text="肤龄")
    original_image = StringField(help_text="原始图片的网址")
    face_crop = StringField(help_text="面部裁剪图片地址")
    overall_score = IntField(help_text="总分")

    face_box = EmbeddedDocumentField(FaceBoxObj, help_text="脸部位置,绝对坐标")
    color = EmbeddedDocumentField(ColorObj, help_text="肤色")
    skin_type = EmbeddedDocumentField(SkinTypeObj, help_text="肤质")
    sensitive = EmbeddedDocumentField(SensitiveObj, help_text="敏感度")
    dark_circle = EmbeddedDocumentField(ProblemObj, help_text="黑眼圈")
    pore = EmbeddedDocumentField(ProblemObj, help_text="毛孔")
    wrinkle = EmbeddedDocumentField(WrinkleObj, help_text="皱纹")
    blackhead = EmbeddedDocumentField(ProblemObj, help_text="黑头")
    roughness = EmbeddedDocumentField(RoughnessObj, help_text="粗糙度")
    hyperpigmentations = EmbeddedDocumentField(InflammationObj, help_text="色素沉着过度")
    problem_bubbles = EmbeddedDocumentField(ProblemBubblesObj, help_text="肤质问题气泡")
    acne = EmbeddedDocumentField(AcneObj, help_text="粉刺")
    inflammations = EmbeddedDocumentField(InflammationObj, help_text="面部炎症")


# class SkinTestResult(DynamicDocument):
#     meta = {
#         'strict': False,
#         "collection": "skin_test_result",
#         'indexes': [
#             {
#                 "fields": ["request_id"],
#                 "name": "_request_id_",
#             },
#         ]
#     }
#     code = StringField(help_text="状态码")
#     msg = StringField(help_text="消息内容")
#     request_id = StringField(help_text="请求id")
#     data = EmbeddedDocumentField(DataObj, help_text="具体数据")
