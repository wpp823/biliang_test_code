from mongoengine import *


class RobotChatMessage(DynamicDocument):
    """
        robot 使用的临时会话数据
    """
    meta = {
        'strict': False,
        "collection": "robot_chat_messages",
        'indexes': [
            {
                "fields": ["msg_id"],
                "name": "_msg_id_",
            },
            {
                "fields": ["user_id", "doctor_id", "status", "is_user_send", ],
                "name": "_mix_search_",
            },
            {
                "fields": ["expired_time"],
                'name': '_expired_time_'
            },
            {
                "fields": ["status"],
                'name': '_status_'
            },
        ]
    }

    STATUS_UNDO = 0  # 未处理
    STATUS_HANDLED = 1  # 已处理
    STATUS_CLEANED = 2  # 已关闭

    msg_id = IntField(help_text='消息id')
    user_id = StringField(required=True)
    doctor_id = StringField(required=True)
    thread_id = StringField(help_text="临时的会话id. 只有当临时会话结束后, 才会赋值", default="")

    # 内容
    content = DictField(help_text='内容')
    create_at = StringField(help_text='创建的时间')
    create_at_time = LongField(help_text="创建的时间. 时间戳, 单位 s")
    expired_time = LongField(help_text="需要回复的时间. 时间戳, 单位 s")

    # 状态参数
    is_user_send = IntField(help_text="是否是用户发送的, 取值 0, 1")
    status = IntField(help_text="状态", choices=[STATUS_UNDO, STATUS_HANDLED, STATUS_CLEANED])
    handled_time = StringField(help_text='处理的时间')

    # 机器人相关配置
    conversation_id = StringField(help_text="rasa 会话 ID")


class RobotChatQRMessage(DynamicDocument):
    """
        robot 随访会话, 自动回复
    """
    meta = {
        'strict': False,
        "collection": "robot_chat_qr_messages",
        'indexes': [
            {
                "fields": ["msg_id"],
                "name": "_msg_id_",
            },
            {
                "fields": ["user_id", "doctor_id", "status", "is_user_send", ],
                "name": "_mix_search_",
            },
            {
                "fields": ["expired_time"],
                'name': '_expired_time_'
            },
            {
                "fields": ["status"],
                'name': '_status_'
            },
        ]
    }

    STATUS_UNDO = 0  # 未处理
    STATUS_HANDLED = 1  # 已处理
    STATUS_CLEANED = 2  # 已关闭

    msg_id = IntField(help_text='消息id', required=True)
    thread_id = StringField(help_text="会话 id", required=True)
    create_at_time = LongField(help_text="创建的时间. 时间戳, 单位 s")
    expired_time = LongField(help_text="需要回复的时间. 时间戳, 单位 s")

    # 状态参数
    is_user_send = IntField(help_text="是否是用户发送的, 取值 0, 1")
    status = IntField(help_text="状态", choices=[STATUS_UNDO, STATUS_HANDLED, STATUS_CLEANED])
    handled_time = StringField(help_text='处理的时间')

    # 机器人相关配置
    intent = DictField(help_text="rasa 意图解析")


class RobotAutoReplyTask(DynamicDocument):
    """
        自动安抚任务
    """
    meta = {
        'strict': False,
        "collection": "robot_auto_reply_task",
        'indexes': [

        ]
    }

    thread_id = StringField(help_text="临时的会话id. 只有当临时会话结束后, 才会赋值", default="", unique=True)
    thread_type = StringField(default="")
    doctor_id = StringField(help_text="doctor_id", default="")
    user_id = StringField(help_text="user_id", default="")
    content = StringField(help_text='内容')
    create_at = StringField(help_text='创建的时间')
    create_at_time = LongField(help_text="创建的时间. 时间戳, 单位 s")

    status = IntField(help_text="状态", choices=[RobotChatMessage.STATUS_UNDO, RobotChatMessage.STATUS_HANDLED])
    handled_time = StringField(help_text='处理的时间')
