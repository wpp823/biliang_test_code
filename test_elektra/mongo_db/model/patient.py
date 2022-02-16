
from datetime import datetime
import shortuuid
from mongoengine import DynamicEmbeddedDocument, DynamicDocument, EmbeddedDocument, EmbeddedDocumentField, StringField, DateTimeField, IntField, \
    DictField, ListField,FloatField,BooleanField,SortedListField

import arrow


class PatientModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "patients",
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

    SEX_MAP = {
        '男': 1,
        '女': 2,
    }
    RELA_SELF = 'self'          # 自己
    RELA_SPOUSE = 'spouse'      # 配偶
    RELA_CHILDRED = 'children'  # 子女
    RELA_PARENTS = 'parents'    # 父母
    RELA_OTHER = 'other'    # 其他

    RELATIONS = [RELA_SELF, RELA_SPOUSE, RELA_CHILDRED, RELA_PARENTS, RELA_OTHER]

    FERTILITY_NO = 'no'     # 未生育
    FERTILITY_HAS = 'has'   # 已生育
    FERTILITY_UNKNOWN = 'unknown'
    FERTILITY_STATUS = [FERTILITY_NO, FERTILITY_HAS]

    CREATE_AUTO = 'auto'
    CREATE_MANUAL = 'manual'

    user_id = StringField(help_text='用户id')
    patient_id = StringField(required=True, help_text='就诊人id,唯一id')
    name = StringField()
    telephone = StringField()
    sex = IntField()
    relation = StringField(choices=RELATIONS)
    create_from = StringField(help_tex='创建方式')
    birthday = StringField(help_text='出生年')
    fertility = StringField(help_text='生育状态')
    family_cases = StringField(help_text='家族病例')
    operation_history = StringField(help_text='手术和外伤史')
    previous_history = StringField(help_text='既往史')
    drug_allergy = StringField(help_text='药物过敏')
    food_allergy = StringField(help_text='食物,接触过敏')
    habit = StringField(help_text='习惯')
    create_at = DateTimeField(help_text='utc时间')
    
    #表明修改名称的历史,只有create_from == CREATE_AUTO 时此字段有效，且每次修改name字段，都要将旧的名称增加到这个列表中。
    # ocr_name_history = SortedListField(help_text="记录所以修改过的名字")
    ocr_name_history = ListField(help_text="记录所以修改过的名字")
    
    # misago_tag = StringField()
    
    @property
    def sex_str(self):
        return '男' if self.sex == 1 else '女'

    @staticmethod
    def get_sex_val(sex_str):
        if sex_str in PatientModel.SEX_MAP:
            return PatientModel.SEX_MAP[sex_str]
        return 0

    @staticmethod
    def get_birthday(age):
        birthday = ''
        if age:
            if age.find('.') != -1:
                year, month = age.split('.')
            else:
                year = int(age)
                month = 0
            birthday = arrow.now(tz='+08:00').shift(years=-int(year), months=-int(month)).format('YYYY-MM-DD')

        return birthday

    def get_age(self):
        """
        获取患者年龄
        :return:
        """
        if self.birthday:
            age = int(arrow.now().format('YYYY')) - int(arrow.get(self.birthday).format('YYYY'))
        else:
            age = 0

        return age 