import arrow
from mongoengine import *


class LastChat(DynamicEmbeddedDocument):
    last_msg_id = IntField()  # 最后聊天消息id
    last_chat_at = StringField()  # 最后聊天时间
    last_chat_msg = StringField()  # 最后聊天内容


class UserShowLastMsg(DynamicEmbeddedDocument):
    """
    记录用户浏览消息位置，用于小红点显示
    """
    user_id = StringField()
    msg_id = IntField()  # 消息id
    msg_at = StringField()  # 聊天时间

class TeamChatPostModel(DynamicDocument):
    """
    团队贴
    """
    meta = {
        'strict': False,
        "collection": "team_chat_post",
        'indexes': [
            {
                "fields": ["post_id", 'doctor_id', "user_id", "create_at"],
                'name': '_fit2_'
            }
        ]
    }
    POST_TYPE = 'team_chat'

    post_id = StringField(help_text='帖子id')
    doctor_id = StringField(help_text='医生id')
    # doctor_name = StringField(help_text='医生名')
    # doctor_avatar = StringField(help_text='医生头像')
    # user_avatar = StringField(help_text='用户头像')
    user_id = StringField(help_text='用户id')
    qa_thread_id = StringField(help_text='问答会话id')

    last_chat_at = StringField(help_text='最后聊天时间，包含图文咨询和门诊')
    last_user_chat = EmbeddedDocumentField(LastChat)  # 患者端
    last_doctor_chat = EmbeddedDocumentField(LastChat)  # 医生端
    create_at = DateTimeField()


class InquiryPostModel(DynamicDocument):
    """
    随访贴
    """
    meta = {
        'strict': False,
        "collection": "inquiry_post",
        'indexes': [
            {
                "fields": ["post_id", "note_id", "user_id", "doctor_id", "status", "inquiry_at"],
                'name': '_fit_'
            }
        ]
    }

    STATUS_NORMAL = 'normal'
    STATUS_CLOSE = 'close'

    POST_TYPE = 'inquiry'

    TIME_MAP = {
        'today': arrow.now().datetime,
        'yesterday': arrow.now().shift(days=-1).datetime,
        '3days': arrow.now().shift(days=-3).datetime,
        '7days': arrow.now().shift(days=-7).datetime,
        '30days': arrow.now().shift(days=-30).datetime,
    }

    doctor_id = StringField(help_text='医生id')
    user_id = StringField(help_text='用户id')
    user_name = StringField(help_text='用户名')
    patient_id = StringField(help_text='就诊人id')
    patient_name = StringField(help_text='就诊人名')
    note_id = StringField(help_text='笔记id')
    post_id = StringField(help_text='帖子id')
    status = StringField(help_text='帖子状态', default=STATUS_NORMAL)
    inquiry_at = StringField(help_text='就诊时间')
    create_at = DateTimeField()
    # last_chat_at = IntField(help_text='最后聊天时间')
    # last_chat_msg = IntField(help_text='最后聊天内容')
    last_user_chat = EmbeddedDocumentField(LastChat)  # 用户
    last_doctor_chat = EmbeddedDocumentField(LastChat)  # 医生
    qa_thread_id = StringField(help_text='问答会话id')
    user_show_last_msg = EmbeddedDocumentListField(UserShowLastMsg, help_text='记录用户浏览消息位置，用于小红点显示')

class ConsultPostModel(DynamicDocument):
    """
    图文咨询帖
    """
    meta = {
        'strict': False,
        "collection": "consult_post",
        'indexes': [
            {
                "fields": ["post_id", "note_id", "doctor_id", "user_id", "create_st", "status"],
                'name': '_fit_'
            }
        ]
    }

    STATUS_NORMAL = 'normal'
    STATUS_CLOSE = 'close'

    POST_TYPE = 'consult'

    SERVICE_CODE_CONSULT = 'consult'    # 图文咨询
    SERVICE_CODE_PRETATION = 'pretation'    # 报告解读
    SERVICE_CODES = [
        SERVICE_CODE_CONSULT,
        SERVICE_CODE_PRETATION
    ]

    doctor_id = StringField(required=True, help_text='医生id')
    user_id = StringField(required=True, help_text='用户id')
    patient_id = StringField(help_text='患者id')
    patient_name = StringField(help_text='患者人名')
    post_id = StringField(help_text='帖子id')
    service_code = StringField(help_text='业务类型', choices=SERVICE_CODES)
    status = StringField(help_text='帖子状态', default=STATUS_NORMAL)
    qa_thread_id = StringField(help_text='问答会话id')
    create_at = DateTimeField()

    last_user_chat = EmbeddedDocumentField(LastChat)  # 用户
    last_doctor_chat = EmbeddedDocumentField(LastChat)  # 医生最后回复数据

    user_show_last_msg = EmbeddedDocumentListField(UserShowLastMsg, help_text='记录用户浏览消息位置，用于小红点显示')

    doctor_first_chat_at = StringField()  # 医生首次回复时间

