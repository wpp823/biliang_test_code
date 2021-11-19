
from datetime import datetime
import    shortuuid
from mongoengine import DynamicEmbeddedDocument, DynamicDocument, EmbeddedDocumentListField, EmbeddedDocumentField, StringField, DateTimeField, IntField, DictField, ListField, BooleanField


class BbsGo(DynamicEmbeddedDocument):

    meta = {"strict": False}

    id = StringField()     # bbsgo id
    username = StringField()    # bbsgo 用户名
    token = StringField()       # bbso 可能调用接口要用
    email = StringField()    #
    password = StringField()

class AiUseQaObj(DynamicEmbeddedDocument):

    meta = {"strict": False}

    person = BooleanField(default=True)         # 个人
    hospital = BooleanField(default=True)       # 本院
    department = BooleanField(default=False)     # 科室
    product = BooleanField(default=False)        # 产品

class BankCardObj(DynamicEmbeddedDocument):
    """
    银行卡信息
    """
    meta = {"strict": False}

    name = StringField(help_text='银行名称')
    card_no = StringField(help_text='卡号')

class PayeeInfoObj(DynamicEmbeddedDocument):
    """
    收款人信息
    """
    meta = {"strict": False}

    CERT_TYPE_IDENTIFY = 'identity'     # 身份证
    CERT_TYPE_HK_MACAO_PASS = 'hk_macao_pass'     # 港澳通行证
    CERT_TYPE_TW_PASS = 'tw_pass'                 # 台湾通行证
    CERT_TYPE_HK_MACAO_RESIDENCE = 'hk_macao_residence'     # 港澳居住证
    CERT_TYPE_TW_RESIDENCE = 'tw_residence'         # 台湾居住证
    CERT_TYPES = [
        CERT_TYPE_IDENTIFY,
        CERT_TYPE_HK_MACAO_PASS,
        CERT_TYPE_TW_PASS,
        CERT_TYPE_HK_MACAO_RESIDENCE,
        CERT_TYPE_TW_RESIDENCE
    ]

    name = StringField(help_text='真实姓名')

    certificate_type = StringField(help_text='证件类型', choices=CERT_TYPES)
    certificate_number = StringField(help_text='证件号码')

    check_name = BooleanField(default=False, help_text='姓名是否已核实, 已核实不可再更改')
    
class WorkWxObj(DynamicEmbeddedDocument):
    '''
    工作微信相关信息。
    '''
    meta = {"strict": False}
    user_id_in_wework = StringField(help_text='工作微信在企业微信中的客户ID')
    
class ServiceItem(DynamicEmbeddedDocument):
    '''
    开展的业务服务项
    '''
    
    SS_CONSULT = 'consult'  #   图文咨询
    SS_PRETATION = 'pretation' #  报告解读
    SS_CONSULT_WEEK = 'consult_week'    #  包周咨询
    SS_CONSULT_MONTH = 'consult_month'  #  包月咨询
    SS_OUTPATIENT_ADD = 'outpatient_add' #  门诊加号
    
    # 每种服务的默认价格。单位为分。
    SS_DEFAULT_PRICE = {
        SS_CONSULT:15000,
        SS_PRETATION:4000,
        SS_CONSULT_WEEK:1000000,
        SS_CONSULT_MONTH:1000000,
        SS_OUTPATIENT_ADD:0
    }
    
    code = StringField(help_text='服务编码', choices=SS_DEFAULT_PRICE.keys())
    price = IntField(help_text='服务标价')
    open_at = StringField(help_text='服务开启时间')
    operator_id = StringField(help_text='此条数据的最后修改人')

    
    @staticmethod
    def get_service_default_price(service_code)->int:
        '''
        获取某个服务的默认坐果
        :param service_code:
        :return:    单位：分
        '''
        
        return ServiceItem.SS_DEFAULT_PRICE.get(service_code, 0)

    
class TimeAt(DynamicEmbeddedDocument):
    '''
    时间点。
    '''
    begin_hour = IntField(help_text='起始时间，小时。')
    begin_minute = IntField(help_text='起始时间，分钟。')
    end_hour = IntField(help_text='结束时间，小时。')
    end_minute = IntField(help_text='结束时间，分钟。')
    
    @property
    def begin_str(self):
        return "{:02}:{:02}".format(self.begin_hour, self.begin_minute)

    @property
    def end_str(self):
        return "{:02}:{:02}".format(self.end_hour, self.end_minute)
    
class IdleItem(DynamicEmbeddedDocument):
    '''
    医生空闲时间配置
    '''
    D_ALL = 'every'
    D_MON = 'monday'
    D_TUS = 'tuesday'
    D_WED = 'wednesday'
    D_THU = 'thursday'
    D_FRI = 'friday'
    D_SAT = 'saturday'
    D_SUN = 'sunday'
    
    D_DAYS = [D_ALL, D_MON,D_TUS, D_WED, D_THU, D_FRI,D_SAT, D_SUN]
    
    day = StringField(help_text='具体是哪一天。',choices=D_DAYS)
    times = EmbeddedDocumentListField(TimeAt, help_text='时间度列表。')
    

class Doctor(DynamicEmbeddedDocument):  # 用于商务填写
    doc_telephone = StringField(help_text='医生手机号')  # 用于激活流程
    work_telephone = StringField(help_text='工作手机号')  # 用于关联深瞳
    real_name = StringField(help_text='实名')
    sex = IntField(help_text='性别, 1男;2女')
    avatar = StringField(help_text='医生头像')
    hospital_name = StringField(help_text='医院名称')
    ocr_hospital_name = StringField(help_text='医院名称')
    ocr_department = StringField(help_text='科室,带门诊')
    hospital_id = StringField(help_text='医院id')
    department = StringField(help_text='科室')
    title_level = IntField(help_text='职称级别')
    title_name = StringField(help_text='职称名称')
    main_desc = StringField(help_text='主页描述')
    main_large_image = StringField(help_text='主页大图')
    qrcode = StringField(help_text='二维码图片链接')

    # 助理设置
    ai_assistant_nickname = StringField(help_text='ai助理昵称')
    ai_assistant_avatar = StringField(help_text='ai助理头像')
    assistant_nickname = StringField(help_text='助理昵称')
    assistant_avatar = StringField(help_text='助理头像')
    ai_use_doctor = BooleanField(help_text='ai助理与医生一致', default=True)
    assistant_use_doctor = BooleanField(help_text='人工助理与医生一致', default=True)
    ai_use_qa = EmbeddedDocumentField(AiUseQaObj, help_text='AI助理使用的问答库列表')
    assistant_overdue_time = IntField(help_text='助理逾期时间，单位：秒', default=900)

    person_qrcode = StringField(help_text='个人二维码图片')
    wx_video_qrcode = StringField(help_text='微信视频号二维码图片')

    consult_enable = BooleanField(help_text='是否启用图文咨询')
    consult_cost = IntField(help_text='咨询费用, 单位：分', default=2000)
    bank_card = EmbeddedDocumentField(BankCardObj, help_text='银行卡信息')

    async_data_rate = IntField(help_text='工作手机同步数据频率，单位：分钟', default=24*60)
    async_voice_notify = BooleanField(help_text='工作手机同步语音提示', default=False)
    deepeyes_version = StringField(help_text='深瞳app版本号')

    marketer_name = StringField(help_text='市场人员名称')
    marketer_telephone = StringField(help_text='市场人员手机号')

    payee_info = EmbeddedDocumentField(PayeeInfoObj, help_text='收款人实名信息')
    entry_time = StringField(help_text='入驻时间')
    
    work_wx = EmbeddedDocumentField(WorkWxObj, help_text='工作微信相关信息')
    services_list = EmbeddedDocumentListField(ServiceItem,help_text='医生开启的服务列表,关闭的或没开启的不在列表中')
    idle_list = EmbeddedDocumentListField(IdleItem,help_text='医生设置的空闲时间段，没有设置的天不在列表里')

    introducer_name = StringField(help_text='介绍人名称')
    director_name = StringField(help_text='所属主任名称')

    enable_endorsement = BooleanField(help_text='设置医生是否开启代言',default=False)


class Config(DynamicEmbeddedDocument):
    auto_patient = BooleanField(help_text='是否自动创建就诊人', default=True)

class EmployeeWorkTelsObj(DynamicEmbeddedDocument):

    meta = {"strict": False}

    telephone = StringField(help_text='手机号')
    create_at = StringField(help_text='关联时间')
    session_id = StringField(help_text='登录session_id')
    login_at = StringField(help_text='登录时间')

class EmployObj(DynamicEmbeddedDocument):  # 客服信息
    # 客服职位
    POSITION_NORMAL = 'normal'  # 普通客服
    POSITION_DIRECTOR = 'director'  # 客服主管
    POSITIONS = [
        POSITION_NORMAL,
        POSITION_DIRECTOR
    ]

    position = StringField(required=True, help_text='客服职位', choices=POSITIONS, default=POSITION_NORMAL)
    work_tels = EmbeddedDocumentListField(EmployeeWorkTelsObj, help_text='客服关联的手机号', default=[])

class UsersModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "users",
        'indexes': [
            {
                "fields": ["user_role", "doctor.hospital_id", "doctor.hospital_name", "doctor.doc_telephone",
                           "doctor.department", "status"],
                'name': '_doctor_fit_'
            },
            {
                "fields": ["user_role", "openid", "telephone", "status", "country", "province", "city"],
                'name': '_user_filter_'
            },
            {
                "fields": ["user_role", "telephone", "status", 'employ.position', 'employ.work_tels.telephone'],
                'name': '_employ_fit_'
            },
        ]
    }
    ROLE_DOCTOR = 'doctor'          # 医生
    ROLE_USER = 'user'              # 用户
    ROLE_NURSE = 'nurse'              # 护士
    ROLE_EMPLOY = 'employ'              # 客服
    # ROLE_OPERATOR = 'operator'      # 运营员
    # ROLE_AI = 'ai_assistant'        # ai助理

    ROLES = [ROLE_DOCTOR, ROLE_USER, ROLE_NURSE, ROLE_EMPLOY]

    STATUS_NORMAL = 'normal'    # 正常
    STATUS_DISABLE = 'disable'  # 禁用
    # 客服状态
    STATUS_NONE = 'none'  # 新建时为空
    STATUS_WORK = 'work'  # 工作中
    STATUS_REST = 'rest'  # 休息中
    STATUS_OFF_WORK = 'off_work'  # 下班
    STATUS = [
        STATUS_NORMAL,
        STATUS_DISABLE,
        STATUS_NONE,
        STATUS_WORK,
        STATUS_REST,
        STATUS_OFF_WORK
    ]

    user_id = StringField(required=True, unique=True, help_text='用户id,唯一id')
    openid = StringField(help_text='小程序openid')
    unionid = StringField(help_text='小程序unionid')
    telephone = StringField(help_text='手机号，医生以doctor字段中的手机号为准')
    nickname = StringField()        # 昵称
    sex = IntField()
    avatar = StringField()  # 医生头像不覆盖
    country = StringField()        # 国家
    province = StringField()        # 省份
    city = StringField()        # 城市
    user_role = StringField(choices=ROLES)
    # misago = EmbeddedDocumentField(Misago)
    bbs_go = EmbeddedDocumentField(BbsGo)
    create_at = DateTimeField(required=True)     # utc
    update_at = DateTimeField()     # utc
    session_id = StringField(help_text='登录session')

    from_doctor_id = StringField(help_text='注册来源医生id')

    last_login_at = DateTimeField()
    doctor = EmbeddedDocumentField(Doctor)
    config = EmbeddedDocumentField(Config)
    status = StringField(help_text='状态', choices=STATUS, default=STATUS_NORMAL)
    last_used_at = StringField(help_text='最近使用时间')

    # 客服
    employ = EmbeddedDocumentField(EmployObj)

    @property
    def doctor_name(self):
        # 21.04.19 将所有自动加“医生“字样的地方全部移除
        return self.doctor.real_name# if self.doctor.real_name.endswith('医生') else '{}医生'.format(self.doctor.real_name)
    
    
    def get_service_config(self, service_code:str) -> ServiceItem:
        '''
        返回某个服务的配置。
        :param service_code:    [str]
        :return:    [ServiceItem]
        '''
        
        for tmp_item in self.doctor.services_list:
            if tmp_item.code == service_code:
                return tmp_item
            
        
        return None
        