
import shortuuid
from mongoengine import DynamicEmbeddedDocument, DynamicDocument, EmbeddedDocument, EmbeddedDocumentField, StringField, \
    DateTimeField, IntField, DictField, ListField, BooleanField, EmbeddedDocumentListField


class FieldItemConfigOptionObj(DynamicEmbeddedDocument):
    """
    选项配置
    """
    option_id = StringField(help_text='id')
    label = StringField(help_text='选项名称')
    value = StringField(help_text='值')
    children = ListField(help_text='下级数据，同当前结构')


class FormFormulaConfigParamsObj(DynamicEmbeddedDocument):
    """
    目标区域
    """
    meta = {"strict": False}

    FORMULA_PARAM_TYPE_FORM_FIELD = 'form_field'  # 数据表id+字段id
    FORMULA_PARAM_TYPE_CONDITION = 'condition'    # 条件
    FORMULA_PARAM_TYPE_FORMULA = 'formula'  # 公式
    FORMULA_PARAM_TYPE_TARGET_FIELD = 'target_field'  # 目标字段id
    FORMULA_PARAM_TYPE_NORMAL = 'normal'  # 常规值
    FORMULA_PARAM_TYPES = [
        FORMULA_PARAM_TYPE_FORM_FIELD,
        FORMULA_PARAM_TYPE_CONDITION,
        FORMULA_PARAM_TYPE_FORMULA,
        FORMULA_PARAM_TYPE_TARGET_FIELD,
    ]

    param_type = StringField(help_text='公式参数类型', choices=FORMULA_PARAM_TYPES)
    form_id = StringField(help_text='数据表id')
    form_name = StringField(help_text='数据表名称')
    field_id = StringField(help_text='数据表字段id')
    field_name = StringField(help_text='数据表字段名称')
    condition_value = StringField(help_text='条件比较')
    normal_value = StringField(help_text='常规值')


    formula_type = StringField(help_text='嵌套公式类型')
    formula_value_type = StringField(help_text='嵌套公式值类型')
    formula_params = ListField(help_text='嵌套公式参数列表')


class FormFormulaConfigObj(DynamicEmbeddedDocument):
    meta = {"strict": False}

    formula_str = StringField(help_text='公式')
    formula_value_type = StringField(help_text='公式值类型，同字段类型')
    formula_params = EmbeddedDocumentListField(FormFormulaConfigParamsObj, help_text='公式参数列表')


class FieldConfigObj(DynamicEmbeddedDocument):
    """
    组件配置
    """
    meta = {"strict": False}
    # max_length = IntField(help_text='最大长度')
    # number_max = IntField(help_text='数字最大值')
    # number_min = IntField(help_text='数字最小值')
    # number_step = IntField(help_text='数字步长')
    # options = EmbeddedDocumentListField(FieldItemConfigOptionObj)
    # data_api_url = StringField(help_text='数据来源api链接')

    formula_config = EmbeddedDocumentField(FormFormulaConfigObj, help_text='公式配置')


class FieldTduckConfigRegListObj(DynamicEmbeddedDocument):
    meta = {"strict": False}

    pattern = StringField(help_text='正则表达式')
    message = StringField(help_text='错误提示')

class FieldTduckConfigObj(DynamicEmbeddedDocument):
    """
    填鸭组件配置
    """
    meta = {"strict": False}
    type = StringField()
    label = StringField()
    show_label = IntField()
    default_value = DictField()
    required = IntField()
    placeholder = StringField()
    sort = IntField()
    span = IntField()
    expand = DictField()
    reg_list = EmbeddedDocumentListField(FieldTduckConfigRegListObj, help_text='正则表达式')
    is_display_type = IntField()


class FieldItemObj(DynamicEmbeddedDocument):
    """
    组件信息
    """
    meta = {"strict": False}
    FIELD_TYPE_TEXT = 'text'  # 文本
    FIELD_TYPE_NUMBER = 'number'  # 数字
    FIELD_TYPE_CASCADER = 'cascader'  # 级联菜单
    FIELD_TYPE_MONEY = 'money'  # 货币
    FIELD_TYPE_OPTIONS = 'options'  # 选项
    FIELD_TYPE_BOOL = 'bool'  # 布尔
    FIELD_TYPE_DATE = 'date'  # 日期
    FIELD_TYPE_TIME = 'time'  # 时间
    FIELD_TYPE_URL = 'url'  # 网址
    FIELD_TYPE_TEL = 'tel'  # 手机
    FIELD_TYPE_EMAIL = 'email'  # 邮箱
    FIELD_TYPE_IMG = 'imgs'  # 图片
    FIELD_TYPE_ATT = 'att'  # 附件
    FIELD_TYPE_AUDIO = 'audio'  # 音频
    FIELD_TYPE_VIDEO = 'video'  # 视频
    FIELD_TYPE_LEVEL = 'level'  # 星级
    FIELD_TYPE_FORMULA = 'formula'  # 公式
    FIELD_TYPE_TICK = 'tick'  # 勾选
    FIELD_TYPE_FILE = 'file'  # 文件
    FIELD_TYPES = [
        FIELD_TYPE_TEXT,
        FIELD_TYPE_NUMBER,
        FIELD_TYPE_CASCADER,
        FIELD_TYPE_MONEY,
        FIELD_TYPE_OPTIONS,
        FIELD_TYPE_BOOL,
        FIELD_TYPE_DATE,
        FIELD_TYPE_TIME,
        FIELD_TYPE_URL,
        FIELD_TYPE_TEL,
        FIELD_TYPE_EMAIL,
        FIELD_TYPE_IMG,
        FIELD_TYPE_ATT,
        FIELD_TYPE_AUDIO,
        FIELD_TYPE_VIDEO,
        FIELD_TYPE_LEVEL,
        FIELD_TYPE_FORMULA,
        FIELD_TYPE_TICK,
        FIELD_TYPE_FILE
    ]

    field_id = StringField(required=True, help_text='字段id')
    version = StringField(required=True, help_text='版本号')
    name = StringField(required=True, help_text='字段名称')
    mapping_field = StringField(help_text='api接口映射字段')
    field_type = StringField(required=True, help_text='字段类型', choices=FIELD_TYPES)
    config = EmbeddedDocumentField(FieldConfigObj, help_text='配置')
    options_from_api_url = StringField(help_text='选项来源api地址')
    tduck_config = EmbeddedDocumentField(FieldTduckConfigObj, help_text='填鸭配置')

class FormTduckConfigObj(DynamicEmbeddedDocument):
    """
    表单配置，填鸭配置
    """
    meta = {"strict": False}

    formRef = StringField()
    formModel = StringField()
    size = StringField()
    labelPosition = StringField()
    labelWidth = IntField()
    formRules = StringField()
    gutter = IntField()
    disabled = BooleanField()
    span = IntField()
    title = StringField()
    description = StringField()
    formBtns = BooleanField()
    unFocusedComponentBorder = BooleanField()

class FormApiConfigParamsObj(DynamicEmbeddedDocument):
    meta = {"strict": False}

    key = StringField(help_text='参数key')
    value = StringField(help_text='参数值')
    operate = StringField(default='=', help_text='判断操作')

class FormApiConfigRewriteFieldsObj(DynamicEmbeddedDocument):
    meta = {"strict": False}

    field_name = StringField(help_text='数据表字段名称')
    res_field = StringField(help_text='返回参数字段名')


class FormApiConfigParamsConfigObj(DynamicEmbeddedDocument):
    """
    参数配置
    """
    meta = {"strict": False}

    name = StringField(help_text='参数名')
    is_need = BooleanField(help_text='是否必须', default=False)
    explain = StringField(help_text='说明')

class FormApiConfigObj(DynamicEmbeddedDocument):
    meta = {"strict": False}

    # 接口触发条件
    API_CONF_TRIGGER_TYPE_GET = 'get'  # 获取数据
    API_CONF_TRIGGER_TYPE_UPDATE = 'update'  # 更新数据
    API_CONF_TRIGGER_TYPE_CREATE = 'create'  # 新增数据
    API_CONF_TRIGGER_TYPE_DELETE = 'delete'  # 删除数据
    API_CONF_TRIGGER_TYPES = [
        API_CONF_TRIGGER_TYPE_GET,
        API_CONF_TRIGGER_TYPE_UPDATE,
        API_CONF_TRIGGER_TYPE_CREATE,
        API_CONF_TRIGGER_TYPE_DELETE,
    ]

    # 接口请求类型
    REQUEST_METHOD_GET = 'get'
    REQUEST_METHOD_POST = 'post'
    REQUEST_METHOD_PUT = 'put'
    REQUEST_METHOD_DELETE = 'delete'
    REQUEST_METHODS = [
        REQUEST_METHOD_GET,
        REQUEST_METHOD_POST,
        REQUEST_METHOD_PUT,
        REQUEST_METHOD_DELETE,
    ]

    API_DATA_TYPE_JSON = 'json'
    API_DATA_TYPE_XML = 'xml'
    API_DATA_TYPES = [
        API_DATA_TYPE_JSON,
        API_DATA_TYPE_XML
    ]

    trigger_type = StringField(help_text='接口触发条件，create|update|delete|get', choices=API_CONF_TRIGGER_TYPES)
    api_url = StringField(help_text='api接口地址')
    api_data_type = StringField(help_text='接口数据类型', choices=API_DATA_TYPES)
    request_method = StringField(help_text='接口请求方式，get|post', choices=REQUEST_METHODS)
    request_headers = EmbeddedDocumentListField(FormApiConfigParamsObj, help_text='请求头')
    request_params = EmbeddedDocumentListField(FormApiConfigParamsObj, help_text='接入参数')
    params_config = EmbeddedDocumentListField(FormApiConfigParamsConfigObj, help_text='参数配置')
    success_condition = EmbeddedDocumentListField(FormApiConfigParamsObj, help_text='返回结果成功判断条件')
    success_rewrite_fields = EmbeddedDocumentListField(FormApiConfigRewriteFieldsObj, help_text='返回结果回写字段')

class FormTemplatesModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "form_templates",
        'indexes': [
            {
                "fields": [("create_at", -1)],
                'name': '_sort_'
            },
        ]
    }

    FORM_TYPE_FREE = 'free'  # 自由录入
    FORM_TYPE_SUBMIT = 'submit'  # 提交表单
    FORM_TYPE_API = 'api'  # api接口
    FORM_TYPE_STATISTICS = 'statistics'  # 分组统计
    FORM_TYPE_PERSPECTIVE = 'perspective'  # 数据透视
    FORM_TYPES = [
        FORM_TYPE_FREE,
        FORM_TYPE_SUBMIT,
        FORM_TYPE_API,
        FORM_TYPE_STATISTICS,
        FORM_TYPE_PERSPECTIVE
    ]

    form_id = StringField(required=True, unique=True, help_text='唯一id')
    name = StringField(required=True, unique=True, help_text='模板名称')
    form_type = StringField(required=True, help_text='数据表类型', choices=FORM_TYPES)
    form_tduck_config = EmbeddedDocumentField(FormTduckConfigObj, help_text='表单填鸭配置')
    api_config = EmbeddedDocumentListField(FormApiConfigObj, help_text='api配置')
    fields = EmbeddedDocumentListField(FieldItemObj, help_text='组件列表')
    create_at = StringField(required=True)
    update_at = StringField(required=True)


