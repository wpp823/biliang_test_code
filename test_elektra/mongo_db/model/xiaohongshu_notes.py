
from mongoengine import DynamicDocument, StringField, ListField

class XiaoHongShuNotesModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "xiaohongshu_notes",
        'indexes': []
    }

    note_id = StringField(required=True, unique=True, help_text='笔记id')
    data = ListField(help_text='笔记数据')
    create_at = StringField()


