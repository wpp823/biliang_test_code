from datetime import datetime
import shortuuid
from mongoengine import *
import arrow


class LastChat(DynamicEmbeddedDocument):
    last_msg_id = IntField()  # 最后聊天消息id
    last_chat_at = StringField()  # 最后聊天时间
    last_chat_msg = StringField()  # 最后聊天内容


class ImageObj(DynamicEmbeddedDocument):
    meta = {"strict": False}

    type = StringField()  # 图片类型
    url = StringField()  # 图片链接
    ocr_results = ListField()
    upload_id = StringField()  # 资源id
    create_at = StringField()


class NoteTargetUserObj(DynamicEmbeddedDocument):
    meta = {"strict": False}

    username = StringField()  # 微信用户id
    nickname = StringField()  # 微信用户昵称
    telephone = StringField()  # 手机号
    wx_chat_id = StringField()  # 微信会话id


class NoteConsultObj(DynamicEmbeddedDocument):
    """
    图文咨询信息
    """
    meta = {"strict": False}

    disease = StringField()  # 咨询疾病
    content = StringField()  # 咨询内容


class NoteWxChatMsgObj(DynamicEmbeddedDocument):
    meta = {"strict": False}

    from_username = StringField()  # 来源微信用户id
    from_nickname = StringField()  # 来源微信用户昵称
    work_telephone = StringField()  # 来源微信工作手机号
    img_url = StringField()  # 图片链接
    upload_id = StringField()  # 资源id
    msg_id = StringField()  # 消息Id
    msgSvrId = StringField()  # 微信消息Id


class NoteModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "note",
        'indexes': [
            {
                "fields": ["note_id", "user_id", "thread_id", "doctor_id", "age", "sex", "create_from", "note_type",
                           "wx_chat_msg.msg_id", "pay_at", "last_user_chat.last_chat_at",
                           "last_user_chat.last_chat_msg_id", "last_doctor_chat.last_chat_at",
                           "last_doctor_chat.last_chat_msg_id", "first_reply_at"],
                'name': '_fit_'
            }
        ]
    }

    TIME_MAP = {
        'today': arrow.now().format('YYYY-MM-DD HH:mm:ss'),
        'yesterday': arrow.now().shift(days=-1).format('YYYY-MM-DD HH:mm:ss'),
        '3days': arrow.now().shift(days=-3).format('YYYY-MM-DD HH:mm:ss'),
        '7days': arrow.now().shift(days=-7).format('YYYY-MM-DD HH:mm:ss'),
        '30days': arrow.now().shift(days=-30).format('YYYY-MM-DD HH:mm:ss'),
    }

    CREATE_FROM_CHAR = 'from_chat'
    CREATE_FROM_NORMAL = 'from_normal'
    CREATE_FROM_WX_CHAT = 'from_wx_chat'  # 微信聊天, 同步数据时创建
    CREATE_FROM_CONSULT = 'from_consult'  # 图文咨询
    CREATE_FROM_WEWORK = 'from_wework'  # 来源企业微信，客服创建

    NOTE_TYPE_OUTPATIENT = 'outpatient'  # 门诊
    NOTE_TYPE_CONSULT = 'consult'  # 图文咨询
    NOTE_TYPE_PRETATION = 'pretation'  # 报告解读
    NOTE_TYPES = [
        NOTE_TYPE_OUTPATIENT,
        NOTE_TYPE_CONSULT,
        NOTE_TYPE_PRETATION
    ]

    STATUS_NORMAL = 'normal'  # 咨询中
    STATUS_CLOSE = 'close'  # 已完成
    STATUS_PRE_COMPLETE = 'pre_complete'  # 待完善
    STATUS_PRE_REQUEST = 'pre_request'  # 待咨询
    STATUS_PAY_PENDING = 'pay_pending'  # 待支付
    STATUS_REFUND_PENDING = 'refund_pending'  # 待退款
    STATUS_REFUND_SUCCESS = 'refund_success'  # 退款成功
    NOTE_STATUS = [
        STATUS_NORMAL,
        STATUS_CLOSE,
        STATUS_PRE_COMPLETE,
        STATUS_PRE_REQUEST,
        STATUS_PAY_PENDING,
        STATUS_REFUND_PENDING,
        STATUS_REFUND_SUCCESS
    ]

    image_types = ['normal', 'medical_record', 'medical_imaging', 'inspection_report', 'disorder_appearance',
                   'otc_image',
                   'pay_slip']

    AGE_MAP = {
        'young': [0, 14],
        'middle': [15, 60],
        'old': [61, 200]
    }

    note_id = StringField(unique=True, help_text='')
    user_id = StringField(help_text='用户id')
    thread_id = StringField(help_text='帖子id')  #
    create_from = StringField(help_tex='从哪创建')
    note_type = StringField(help_tex='笔记类型', choices=NOTE_TYPES)
    status = StringField(help_tex='笔记状态', choices=NOTE_STATUS)
    patient_id = StringField(help_text='就诊人id')
    patient_name = StringField(help_text='就诊人')
    sex = IntField(help_text='性别')
    age = FloatField(help_text='年龄')
    inquiry_type = StringField(help_text='就诊类型')
    hospital_name = StringField(help_text='医院')
    department_name = StringField(help_text='科室')
    doctor = StringField(help_text='医生')
    title_name = StringField(help_text='医生职称')
    chief_complaint = StringField(help_text='主诉')
    medical_history = StringField(help_text='病史')
    physical_exa = StringField(help_text='体检')
    diagnosis = StringField(help_text='诊断')
    handle = StringField(help_text='处理')

    image_list = EmbeddedDocumentListField(ImageObj)  #
    # image_results = ListField()  # 保存图片识别结果

    # post_id = StringField(help_text='帖子id')
    doctor_id = StringField(help_text='随访帖对应医生id')
    create_at = DateTimeField()
    inquiry_at = StringField()  # 问诊时间

    target_user = EmbeddedDocumentField(NoteTargetUserObj, help_text='目标粉丝，当create_from==from_wx_chat|from_wework时有效')
    wx_chat_msg = EmbeddedDocumentField(NoteWxChatMsgObj, help_text='创建来源微信聊天消息信息，当create_from==from_wx_chat时有效')

    consult = EmbeddedDocumentField(NoteConsultObj, help_text='图文咨询，当create_from==from_consult时有效')
    pay_at = StringField(help_text='支付时间，支付成功有此值')
    refund_at = StringField(help_text='退款时间，退款成功有此值')

    last_user_chat = EmbeddedDocumentField(LastChat)  # 患者端
    last_doctor_chat = EmbeddedDocumentField(LastChat)  # 医生端

    creator_id = StringField(help_text='创建者id')

    emp_creator_id = StringField(help_text='来源客服确认者id，用于create_from==from_wework')
    wework_msg_id = StringField(help_text='企业微信消息id，用于create_from==from_wework')
    wework_seq = IntField(help_text='企业微信偏移量，用于create_from==from_wework')

    first_reply_at = StringField(help_text='医生首次回复时间')
    used_doctor_times = IntField(help_text='经过的医生空闲时间，单位：分钟')

    @property
    def age_str(self):
        # 年龄转为字符串
        if not self.age:
            return ''

        year, month = str(self.age).split('.')
        if int(month) != 0:
            age = str(self.age)
        else:
            age = year

        return age
