


from datetime import datetime
import shortuuid
from mongoengine import *


class ChatMessage(DynamicDocument):
    """
    聊天记录
    """
    meta = {
        'strict': False,
        "collection": "chat_messages",
        'indexes': [
        ]
    }

    msg_id = StringField(help_text='消息id')
    user_id = StringField(required=True)
    doctor_id = StringField(required=True)
    note_id = StringField()
    thread_id = StringField()
    content = DictField(help_text='内容')
    create_at = DateTimeField(help_text='时间')

    image_ocr_data = StringField(help_text="图片识别数据")