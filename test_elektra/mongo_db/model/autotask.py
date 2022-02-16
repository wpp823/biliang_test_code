


from datetime import datetime
import shortuuid
from mongoengine import *


class RunAt(DynamicEmbeddedDocument):

    meta = {"strict": False}

    day = IntField()     # 加 几天
    time_beg = StringField()    # 开始时间
    time_end = StringField()
    time_desc = StringField()  # 描述


class AutoTaskModel(DynamicDocument):
    """
    定时任务
    """
    meta = {
        'strict': False,
        "collection": "auto_tasks",
        'indexes': [
            {
                "fields": ["task_id"],
                'name': '_task_id_'
            }
        ]
    }

    TYPE_GLOBAL_FOLLOW = 'global_follow'    # 欢迎粉丝
    TYPE_GLOBAL_REPEAT = 'global_repeat'    # 随访问候
    TYPE_GLOBAL_REPLY_REMINDER = 'global_reply_reminder'    # 答复提醒
    TYPE_GLOBAL_OVERTIME_APPEASE = 'global_overtime_appease'  # 超时安抚

    task_id = StringField(help_text='任务id')
    user_id = StringField()
    task_type = StringField(help_text='任务类型')
    text = StringField(help_text='发送内容')
    enable = BooleanField(default=True, help_text='是否启用')
    run_at = EmbeddedDocumentListField(RunAt)
    celery_task_ids = ListField()



