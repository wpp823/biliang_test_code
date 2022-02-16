



from datetime import datetime
import shortuuid
from mongoengine import *


class PatientModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "health_records",
        'indexes': [
            {
                "fields": ["patient_id"],
                'name': '_patient_id_'
            },
            {
                "fields": ["name"],
                'name': '_name_'
            }
        ]
    }

    patient_id = StringField()
    height = IntField(help_text='身高cm')
    weight = FloatField(help_text='体重kg')
    heart_rate = IntField(help_text='心率,每分钟多少次')
    blood_pressure = StringField(help_text='血压 低/高')
    blood_sugar = FloatField(help_text='血糖')
    temperature = FloatField(help_text='体温')
    sleep = FloatField(help_text='睡眠')
    steps = FloatField(help_text='步数')
    create_at = DateTimeField()
    measure_at = DateTimeField(help_text='测量时间')
