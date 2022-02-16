
from datetime import datetime
import shortuuid
from mongoengine import DynamicEmbeddedDocument, DynamicDocument, EmbeddedDocument, EmbeddedDocumentField, StringField, DateTimeField, IntField, DictField, ListField, BooleanField
from app.mongo_db.model.note import LastChat

class ThreadsModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "threads",
        'indexes': [
            {
                "fields": ["thread_type", "doctor_id", "user_id", "create_at"],
                'name': '_fit_'
            },
            {
                "fields": [("create_at", -1)],
                'name': '_sort_'
            },
        ]
    }

    THREAD_TYPE_OUTPATIENT = 'outpatient'  # 门诊
    THREAD_TYPE_CONSULT = 'consult'  # 图文咨询
    THREAD_TYPES = [
        THREAD_TYPE_OUTPATIENT,
        THREAD_TYPE_CONSULT
    ]

    thread_id = StringField(required=True, unique=True, help_text='唯一id')
    thread_type = StringField(required=True, help_text='聊天类型', choices=THREAD_TYPES)
    doctor_id = StringField(required=True, help_text='医生id')
    user_id = StringField(help_text='患者用户id')
    last_user_chat = EmbeddedDocumentField(LastChat)  # 患者端最后一条消息
    last_doctor_chat = EmbeddedDocumentField(LastChat)  # 医生端最后一条消息
    create_at = StringField(required=True)
    update_at = StringField(required=True)


