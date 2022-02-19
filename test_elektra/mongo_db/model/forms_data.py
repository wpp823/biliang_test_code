
import shortuuid
from mongoengine import DynamicEmbeddedDocument, DynamicDocument, EmbeddedDocument, EmbeddedDocumentField, StringField, \
    DateTimeField, IntField, DictField, ListField, BooleanField, EmbeddedDocumentListField


class FormsDataObj(DynamicEmbeddedDocument):
    meta = {"strict": False}

    _openid = StringField(help_text='用户openid')
    _user_id = StringField(help_text='用户id')
    _doctor_id = StringField(help_text='医生id')
    _company_id = StringField(help_text='单位id')
    _department_id = StringField(help_text='科室id')
    _thread_id = StringField(help_text='会话id')
    _tool_id = StringField(help_text='工具id')
    _add_at = StringField(help_text='提交时间')

class FormsDataModel(DynamicDocument):
    '''
    活动表单数据
    '''
    meta = {
        'strict': False,
        "collection": "forms_data",
        'indexes': [
            {
                'fields': ['form_id', "form_data._doctor_id", "form_data._user_id", "form_data._openid",
                           "form_data._company_id", "form_data._department_id", "form_data._thread_id",
                           "form_data._tool_id", "form_data._add_at", 'approval_status', 'approval_res', 'create_at'],
                'name': '_filter_'
            },
        ]
    }


    FREE_FORM_SYSTEM_FIELD_OPENID = '_openid'         # 提交人openid
    FREE_FORM_SYSTEM_FIELD_ADD_AT = '_add_at'         # 提交时间
    FREE_FORM_SYSTEM_FIELD_USER_ID = '_user_id'       # 用户id
    FREE_FORM_SYSTEM_FIELD_DOCTOR_ID = '_doctor_id'   # 医生id
    FREE_FORM_SYSTEM_FIELD_COMPANY_ID = '_company_id'   # 医生单位id
    FREE_FORM_SYSTEM_FIELD_DEPARTMENT_ID = '_department_id'   # 医生科室id
    FREE_FORM_SYSTEM_FIELD_THREAD_ID = '_thread_id'   # 会话id
    FREE_FORM_SYSTEM_FIELD_TOOL_ID = '_tool_id'       # 工具id

    APPROVAL_STATUS_PENDING = 'pending'     # 待审核
    APPROVAL_STATUS_APPROVED = 'approved'   # 已审核
    APPROVAL_STATUS_NO_NEED = 'no_need'     # 无需审核
    APPROVAL_STATUS = [
        APPROVAL_STATUS_PENDING,
        APPROVAL_STATUS_APPROVED,
        APPROVAL_STATUS_NO_NEED
    ]

    APPROVAL_RES_PASS = 'pass'
    APPROVAL_RES_REFUSE = 'refuse'
    APPROVAL_RES = [
        APPROVAL_RES_PASS,
        APPROVAL_RES_REFUSE
    ]

    fd_id = StringField(required=True, unique=True, help_text='数据id')
    form_id = StringField(required=True, help_text='数据表id')
    form_data = EmbeddedDocumentField(FormsDataObj, help_text='表单数据')
    approval_status = StringField(help_text='审核状态', choices=APPROVAL_STATUS)
    approval_res = StringField(help_text='审核结果', choices=APPROVAL_RES)
    approval_at = StringField(help_text='审核时间')
    order = IntField(help_text='排序字段')
    msg_id = StringField(help_text='对应会话消息id')
    create_at = StringField(required=True)
    update_at = StringField(required=True)



