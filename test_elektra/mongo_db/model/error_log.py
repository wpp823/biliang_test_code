



from datetime import datetime
import shortuuid
from mongoengine import *


class ErrorLogModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "error_log",
        'indexes': [
        ]
    }

    err_id = StringField(unique=True)
    content = StringField()
    create_at = StringField()
