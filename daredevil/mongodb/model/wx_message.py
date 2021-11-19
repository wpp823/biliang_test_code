from datetime import datetime
import shortuuid
from mongoengine import DynamicEmbeddedDocument, DynamicDocument, EmbeddedDocument, EmbeddedDocumentField, StringField, \
    DateTimeField, IntField, DictField, ListField, BooleanField, EmbeddedDocumentListField
# from app.mongo_db.model.wx_chats import WxChatsModel
import arrow


class WxMessageChatFromObj(DynamicEmbeddedDocument):
    meta = {"strict": False}

    user_id = StringField(required=True, help_text='微信id')
    nickname = StringField(help_text='微信nickname')
    remark_name = StringField(help_text='备注名称')
    avatar = StringField(help_text='头像')


class WxMsgForwardContentObj(DynamicEmbeddedDocument):
    """
    转发消息内容
    """
    # meta = {"strict": False}

    desc = StringField(help_text='文本或描述')

    # 图片
    upload_id = StringField(help_text='')
    url = StringField(help_text='')
    type = StringField(help_text='')

    length = IntField()

    image = StringField()

    avatar = StringField()
    sex = StringField()
    city = StringField()
    province = StringField()
    regionCode = StringField()

    # 小程序
    mp_icon = StringField(help_text='')
    mp_name = StringField(help_text='')
    title = StringField(help_text='')
    mp_avatar = StringField(help_text='')
    mp_avatar_type = StringField(help_text='')
    uri = StringField(help_text='')


class WxMessageForwardObj(DynamicEmbeddedDocument):
    # 转发消息
    msg_type = StringField(help_text='消息类型，根据type转换')
    type = IntField(help_text='微信类型')
    msg_desc = StringField(help_text='消息内容简述，如[图片]、[位置]等')
    msg_source_time = DateTimeField(help_text='消息发送时间')
    msg_source_name = StringField(help_text='发送者昵称')
    talker = StringField(help_text='群消息带@chatroom;  其他个人消息， 微信ID')
    # content = StringField(help_text='原始消息内容')
    msg_content_lite = EmbeddedDocumentField(WxMsgForwardContentObj, help_text='消息具体内容')


class WxMessageContentObj(DynamicEmbeddedDocument):
    """
    根据消息类型设置字段值
    """
    meta = {"strict": False}

    desc = StringField(help_text='文本或描述')

    # 图片
    upload_id = StringField(help_text='')
    url = StringField(help_text='')
    type = StringField(help_text='')

    length = IntField()

    image = StringField()

    avatar = StringField()
    sex = StringField()
    city = StringField()
    province = StringField()
    regionCode = StringField()

    # 小程序
    mp_icon = StringField(help_text='')
    mp_name = StringField(help_text='')
    title = StringField(help_text='')
    mp_avatar = StringField(help_text='')
    mp_avatar_type = StringField(help_text='')
    uri = StringField(help_text='')

    # 转发消息
    forward_msg_title = StringField(help_test='消息标题')
    forward_msg_desc = StringField(help_test='整体内容简述')
    forward_msg_content_list = EmbeddedDocumentListField(WxMessageForwardObj, help_text='消息内容列表')

class WxMessageReferObj(DynamicEmbeddedDocument):
    meta = {"strict": False}

    msg_id = StringField(help_text='引用的id')
    chat_from = EmbeddedDocumentField(WxMessageChatFromObj, help_text='消息发送者信息')
    msg_type = StringField(help_text='消息类型')
    content_lite = EmbeddedDocumentField(WxMessageContentObj, help_text='消息内容')
    msg_desc = StringField(help_text='消息简单描述')
    upload_img_record_id = StringField(help_text='上传图片记录id')



class WxMessageModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "wx_message",
        'indexes': [
            {
                "fields": ["from_username", "msgSvrId", "talker", "createTime"],
                'unique': True
            },
            {
                "fields": ["msg_id", "chat_type", "chat_id", "type", "msg_type", "isSend", "talker",
                           "createTime", "create_at", "device_id", "batch_id"],
                'name': '_filter_'
            },
            {
                "fields": ["upload_img_record_id"],
                'name': '_up_img_record_id_'
            },
            {
                "fields": [("createTime", -1), ("create_at", -1)],
                'name': '_sort_'
            },
        ]
    }

    msg_id = StringField(required=True, unique=True, help_text='唯一id')
    from_username = StringField(required=True, help_text='唯一id, 主帐号ID，代表这是谁的微信。微信ID')
    msgSvrId = StringField(required=True, help_text='服务器同步消息id，可能为0')
    # chat_type = StringField(required=True, help_text='聊天类型', choices=WxChatsModel.CHAT_TYPES)
    chat_id = StringField(required=True, help_text='会话id')
    type = IntField(required=True, help_text='微信消息类型')
    msg_type = StringField(required=True, help_text='消息类型，根据type转换')
    isSend = IntField(required=True, help_text='0不是我发送的; 1为本人发送')
    talker = StringField(required=True, help_text='群消息带@chatroom;  其他个人消息， 微信ID')
    content = StringField(help_text='原始消息内容')
    msg_content = EmbeddedDocumentField(WxMessageContentObj, help_text='消息内容，从content提取,小量康康的结构')
    msg_desc = StringField(help_text='消息内容简述，如[图片]、[位置]等')
    imgPath = StringField(help_text='资源数据')
    createTime = IntField(required=True, help_text='聊天时间戳，单位：毫秒')
    chat_from = EmbeddedDocumentField(WxMessageChatFromObj, help_text='消息发送者信息,小量康康的from')
    refer = EmbeddedDocumentField(WxMessageReferObj, help_text='引用消息', default={})
    create_at = StringField(required=True)
    update_at = StringField(required=True)
    create_user_id = StringField(required=True, help_text='操作用户id')
    device_id = StringField(required=True, help_text='设备id')
    batch_id = StringField(required=True, help_text='批次id')
    upload_img_record_id = StringField(help_text='上传图片记录id')

    @property
    def remark_name(self):
        return self.chat_from.remark_name
