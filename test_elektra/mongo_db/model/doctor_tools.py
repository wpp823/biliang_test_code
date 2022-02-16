
import shortuuid
from mongoengine import DynamicEmbeddedDocument, DynamicDocument, EmbeddedDocument, EmbeddedDocumentField, StringField, \
    DateTimeField, IntField, DictField, ListField, BooleanField, EmbeddedDocumentListField
from app.mongo_db.model.form_templates import FieldItemObj



class ToolFormInfoObj(DynamicEmbeddedDocument):
    """
    表单信息
    """
    # 数据提交范围
    FORM_DATA_RANGE_COMPANY = 'company'  # 单位
    FORM_DATA_RANGE_DEPARTMENT = 'department'  # 科室
    FORM_DATA_RANGE_SELF = 'self'  # 自己
    FORM_DATA_RANGES = [
        FORM_DATA_RANGE_COMPANY,
        FORM_DATA_RANGE_DEPARTMENT,
        FORM_DATA_RANGE_SELF
    ]

    form_data_range = StringField(required=True, help_text='提交范围', choices=FORM_DATA_RANGES)
    form_id = StringField(required=True, help_text='模板表单id')
    # form_name = StringField(required=True, help_text='模板表单名称')
    # fields = EmbeddedDocumentListField(FieldItemObj, help_text='组件列表')


class DoctorToolsModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "doctor_tools",
        'indexes': [
            {
                "fields": ["tool_type", "doctor_id", "approval", "template_id", "status", "create_at"],
                'name': '_fit_'
            },
            {
                "fields": [("create_at", -1)],
                'name': '_sort_'
            },
        ]
    }
    STATUS_NORMAL = 'normal'
    STATUS_DELETE = 'delete'
    STATUS = [
        STATUS_NORMAL,
        STATUS_DELETE
    ]

    TOOL_TYPE_FORM = 'form'     # 表单
    TOOL_TYPES = [
        TOOL_TYPE_FORM
    ]

    tool_id = StringField(required=True, unique=True, help_text='唯一id')
    tool_type = StringField(required=True, help_text='工具类型', choices=TOOL_TYPES)
    doctor_id = StringField(required=True, help_text='医生id')
    name = StringField(required=True, help_text='模板名称')
    approval = BooleanField(required=True, help_text='是否需要审核', default=True)
    form_info = EmbeddedDocumentField(ToolFormInfoObj,  help_text='表单信息')
    status = StringField(required=True, help_text='状态', choices=STATUS, default=STATUS_NORMAL)
    create_at = StringField(required=True)
    update_at = StringField(required=True)


