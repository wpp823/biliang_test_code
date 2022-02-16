from mongoengine import *


class WikiObj(EmbeddedDocumentField):
    meta = {'strict': False}
    heading = StringField(help_text="标题")
    contents = StringField(help_text="内容")


class ClassificationObj(EmbeddedDocumentField):
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


class DataObj(EmbeddedDocumentField):
    meta = {'strict': False}
    SERVICE_VERSION = "dermx-1.2.1"

    version = StringField(help_text="服务版本")
    classification = EmbeddedDocumentListField(ClassificationObj, help_text="预测列表按模型概率排序")
    relevant = BooleanField(help_test="图片是否包含足够的皮肤")
    detected = BooleanField(help_test="是否检测到显着损伤")
    confidence = StringField(help_text="匹配程度")


class SkinTestResult(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "robot_chat_messages",
        'indexes': [
            {
                "fields": ["request_id"],
                "name": "_request_id_",
            },
        ]
    }
    code = StringField(help_text="状态码")
    msg = StringField(help_text="消息内容")
    request_id = StringField(help_text="请求id")
    data = DynamicEmbeddedDocument(DataObj, help_text="具体数据")

