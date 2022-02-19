

from mongoengine import *


class ChatsModel(DynamicDocument):
    """
    临时聊天会话
    """
    meta = {
        'strict': False,
        "collection": "chats",
        'indexes': [
            {
                "fields": ["doctor_id", "user_id", "create_at"],
                'name': '_fit_'
            },
        ]
    }

    CREATE_FROM_NORMAL = 'normal'
    CREATE_FROM_FOLLOW = 'follow'   # 关注
    CREATE_FROM_TYPES = [
        CREATE_FROM_NORMAL,
        CREATE_FROM_FOLLOW
    ]

    thread_id = StringField(unique=True, help_text='会话id')
    user_id = StringField(required=True)
    doctor_id = StringField(required=True)
    create_from = StringField(choices=CREATE_FROM_TYPES, default=CREATE_FROM_NORMAL)
    from_page = StringField(help_text='来源页面')
    create_at = StringField(help_text='创建时间')
    update_at = StringField(help_text='更新时间')
