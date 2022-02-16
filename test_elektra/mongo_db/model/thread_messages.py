from mongoengine import DynamicEmbeddedDocument, DynamicDocument, EmbeddedDocumentField, StringField, IntField, ListField, BooleanField


class MessageContentObj(DynamicEmbeddedDocument):
    desc = StringField(help_text='内容描述')
    upload_id = StringField(help_text='oss资源id')
    url = StringField(help_text='链接')
    type = StringField(help_text='类型')

    length = StringField(help_text='语音时间长度，单位：毫秒')

    nickname = StringField(help_text='昵称')
    avatar = StringField(help_text='头像')
    sex = StringField(help_text='性别，1|2|0')
    city = StringField(help_text='')
    province = StringField(help_text='')
    regionCode = StringField(help_text='')

    title = StringField(help_text='标题')
    image = StringField(help_text='图片')


    uri = StringField(help_text='')
    name = StringField(help_text='')

    # 小程序
    mp_icon = StringField(help_text='http开头为网络图片，非http开头为本地图片')
    mp_name = StringField(help_text='小程序名称')
    mp_avatar = StringField(help_text='封面图')
    mp_avatar_type = StringField(help_text='封面图类型，图片或视频。')

    note_id = StringField(help_text='笔记ID')
    visit_at = StringField(help_text='就诊日期')
    patient_name = StringField(help_text='就诊人名称')

    # 图文咨询
    disease = StringField(help_text='咨询疾病')
    content = StringField(help_text='咨询内容')
    patient_sex = StringField(help_text='患者性别')
    patient_age = StringField(help_text='患者年龄')

    op_name = StringField(help_text='动作按钮名称')
    target_url = StringField(help_text='跳转地址')

    data_list = ListField(help_text='列表数据')


class MessageChatFromObj(DynamicEmbeddedDocument):
    USER_ROLE_DOCTOR = 'doctor'  # 医生
    USER_ROLE_USER = 'user'  # 用户
    USER_ROLE_EMPLOY = 'employ'  # 客服
    USER_ROLE_AI_ASSISTANT = 'ai_assistant'  # AI助理
    USER_ROLES = [
        USER_ROLE_DOCTOR,
        USER_ROLE_USER,
        USER_ROLE_EMPLOY,
        USER_ROLE_AI_ASSISTANT
    ]

    user_id = StringField(help_text='用户id')
    # nickname = StringField(help_text='昵称')
    # avatar = StringField(help_text='头像')
    # remark_name = StringField(help_text='备注名称')
    role = StringField(help_text='角色', choices=USER_ROLES)


class MessageAtObj(DynamicEmbeddedDocument):
    thread_id = StringField(help_text='会话id')
    type = StringField(help_text='会话类型')
    name = StringField(help_text='会话名称')


class MessageFromWxInfoObj(DynamicEmbeddedDocument):
    wx_msg_id = StringField(help_text='对应微信聊天消息id')
    wx_user_id = StringField(help_text='对应微信聊天对象微信id')


class MessageReferObj(DynamicEmbeddedDocument):
    msg_id = IntField(help_text='消息id')
    msg_type = StringField(help_text='消息类型')
    content_lite = EmbeddedDocumentField(MessageContentObj)
    chat_from = EmbeddedDocumentField(MessageChatFromObj)
    from_wx_info = EmbeddedDocumentField(MessageFromWxInfoObj)


class MessageFromDoctorChatroomMsgObj(DynamicEmbeddedDocument):
    meta = {"strict": False}

    msg_id = StringField()  # 消息Id
    msgSvrId = StringField()  # 微信消息Id
    chatroom_username = StringField()  # 微信群id


class ThreadMessagesModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "thread_messages",
        'indexes': [
            {
                "fields": ["msg_id", "msg_type", "at.thread_id", "at.type", "create_at", "chat_from.user_id",
                           "from_wx_info.wx_msg_id", "from_wx_info.wx_user_id", "from_doctor_chatroom_msg.msg_id"],
                'name': '_fit2_'
            },
            {
                "fields": ["user_list"],
                'name': '_user_list_'
            },
        ]
    }

    MSG_TYPE_ARTICLE = 'article'
    MSG_TYPE_TEXT = 'text'
    MSG_TYPE_VOICE = 'voice'
    MSG_TYPE_IMAGE = 'image'
    MSG_TYPE_VIDEO = 'video'
    MSG_TYPE_FILE = 'file'
    MSG_TYPE_THREAD_SHARE = 'thread_share'
    MSG_TYPE_ACTION_DESC = 'action_desc'
    MSG_TYPE_NO_FROM_IMAGE = 'no_from_image'
    MSG_TYPE_INQUIRY_APPLICATION = 'inquiry_application'
    MSG_TYPE_INQUIRY_NOTE = 'inquiry_note'
    MSG_TYPE_CONSULT_NOTE = 'consult_note'
    MSG_TYPE_MINIPROGRAM = 'miniprogram'
    MSG_TYPE_MSG_CARD = 'msg_card'
    MSG_TYPE_WECHAT_CARD = 'wechat_card'
    MSG_TYPE_CHAT_RECORD = 'chat_record'
    MSG_TYPE_VOIP_CONTENT_VOICE = 'voip_content_voice'
    MSG_TYPE_VOIP_CONTENT_VIDEO = 'voip_content_video'

    msg_id = IntField(required=True, unique=True, help_text='唯一id')
    msg_version = StringField(help_text='版本号')
    msg_type = StringField(required=True, help_text='消息类型')
    tags = ListField(help_text='标签', default=[])
    content = EmbeddedDocumentField(MessageContentObj)
    refer = EmbeddedDocumentField(MessageReferObj)
    chat_from = EmbeddedDocumentField(MessageChatFromObj)
    at = EmbeddedDocumentField(MessageAtObj)
    from_wx_info = EmbeddedDocumentField(MessageFromWxInfoObj)
    from_doctor_chatroom_msg = EmbeddedDocumentField(MessageFromDoctorChatroomMsgObj, help_text='记录来源医生群聊话术信息')

    create_at = StringField(required=True, help_text='聊天时间')
    create_time = StringField(required=True, help_text='消息入库时间')
    update_time = StringField(required=True, help_text='消息更新时间')

    # 新加字段
    user_list = ListField(help_text='关联用户', default=[])

    image_ocr_data = StringField(help_text='图片ocr内容')



class BbsGoExtraObj(DynamicEmbeddedDocument):
    StatusOk = 0  # 正常
    StatusRecall = 3  # 已撤回

    is_original = BooleanField(help_text="是否原创")
    msg_status = IntField(required=True, default=StatusOk, help_text="Msg状态")


class BbsGoMessagesModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "bbsgo_messages",
        'indexes': [
            {
                "fields": ["msg_id", "msg_type", "at.thread_id", "at.type", "create_at", "chat_from.user_id",
                           "from_wx_info.wx_msg_id", "from_wx_info.wx_user_id", "from_doctor_chatroom_msg.msg_id"],
                'name': '_fit2_'
            },
            {
                "fields": ["bbsgo_extra.is_original"],
                "name": "_bbsgo_extra_is_original_",
            },
            {
                "fields": ["bbsgo_extra.msg_status"],
                "name": "_bbsgo_extra_msg_status_",
            },
            {
                "fields": ["user_list"],
                'name': '_user_list_'
            },
            {
                "fields": ["at.thread_id"],
                'name': '_at__thread_id_'
            },
        ]
    }

    msg_id = IntField(required=True, unique=True, help_text='唯一id')
    msg_version = StringField(help_text='版本号')
    msg_type = StringField(required=True, help_text='消息类型')
    tags = ListField(help_text='标签', default=[])
    content = EmbeddedDocumentField(MessageContentObj)
    refer = EmbeddedDocumentField(MessageReferObj)
    chat_from = EmbeddedDocumentField(MessageChatFromObj)
    at = EmbeddedDocumentField(MessageAtObj)

    # 这些字段, 不用
    from_wx_info = EmbeddedDocumentField(MessageFromWxInfoObj)
    from_doctor_chatroom_msg = EmbeddedDocumentField(MessageFromDoctorChatroomMsgObj, help_text='记录来源医生群聊话术信息')

    create_at = StringField(required=True, help_text='聊天时间')
    create_time = StringField(required=True, help_text='消息入库时间')
    update_time = StringField(required=True, help_text='消息更新时间')

    # bbsgo 特定状态
    bbsgo_extra = EmbeddedDocumentField(BbsGoExtraObj)

    # 新加字段
    user_list = ListField(help_text='关联用户', default=[])

    image_ocr_data = StringField(help_text='图片ocr内容')
