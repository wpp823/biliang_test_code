
from mongoengine import *

class PaymentDataObj(DynamicEmbeddedDocument):
    """
    付款成功信息
    """
    meta = {"strict": False}

    openid = StringField(help_text='付款openid')
    nickname = StringField(help_text='付款用户昵称')
    real_name = StringField(help_text='付款用户实名')
    avatar = StringField(help_text='付款用户头像')
    partner_trade_no = StringField(help_text='付款订单id')
    payment_no = StringField(help_text='付款成功，返回的微信付款单号')
    payment_time = StringField(help_text='付款成功时间')
    appid = StringField(help_text='appid')
    bankcard_number = StringField(help_text='银行卡号')


class ProductSkuObj(DynamicEmbeddedDocument):
    """
    产品信息
    """
    meta = {"strict": False}

    product_id = StringField(help_text='产品id')
    product_name = StringField(help_text='产品名称')


class ProductDataObj(DynamicEmbeddedDocument):
    """
    订单产品信息
    """
    meta = {"strict": False}

    order_id = StringField(help_text='订单id')

    product_sku = EmbeddedDocumentListField(ProductSkuObj, help_text='产品信息')
    product_price = IntField(help_text='订单产品价格，非单价，单位：分')
    remark = StringField(help_text='备注')
    is_first = BooleanField(help_text='是否首购')

class DoctorIncomesOrdersModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "doctor_incomes_orders",
        'indexes': [
            {
                "fields": ["order_type", "from_order_id", "from_order_pay_at", "from_doctor_id", "doctor_id", "note_id", "transfer_status",
                           "transfer_type", "thread_id", "create_at", "update_at", "payment_data.openid",
                           "payment_data.partner_trade_no", "payment_data.payment_no", "payment_data.payment_time",
                           "product_data.order_id", "product_data.is_first"],
                'name': '_fit3_'
            },
            # {
            #     'fields': ['from_order_id', 'from_doctor_id', 'doctor_id'],
            #     'unique': True
            # }
        ]
    }

    ORDER_TYPE_CONSULT = 'consult'  # 图文咨询
    ORDER_TYPE_ORIGINAL_MSG = 'original_msg'  # 原创话术
    ORDER_TYPE_PRETATION = 'pretation'  # 报告解读
    ORDER_TYPE_PRODUCT = 'product'  # 产品(健康建议)
    ORDER_TYPE_OTHER = 'other'  # 其他
    ORDER_TYPE_AWARD = 'award'  # 心意

    ORDER_TYPES = [
        ORDER_TYPE_CONSULT,
        ORDER_TYPE_ORIGINAL_MSG,
        ORDER_TYPE_PRETATION,
        ORDER_TYPE_PRODUCT,
        ORDER_TYPE_OTHER,
        ORDER_TYPE_AWARD
    ]
    # 订单类型商品描述
    ORDER_DESC = {
        ORDER_TYPE_CONSULT: '图文咨询',
        ORDER_TYPE_ORIGINAL_MSG: '原创话术',
        ORDER_TYPE_PRETATION: '报告解读',
        ORDER_TYPE_PRODUCT: '健康建议',
        ORDER_TYPE_AWARD: '心意',
    }

    TRANSFER_TYPE_WECHAT = 'wechat'  # 微信支付
    TRANSFER_TYPE_YZH_WECHAT = 'yunzhanghu_wechat'  # 云帐户付款到微信
    TRANSFER_TYPE_YZH_BANK = 'yunzhanghu_bank'  # 云帐户付款到银行卡
    TRANSFER_TYPES = [
        TRANSFER_TYPE_WECHAT,
        TRANSFER_TYPE_YZH_WECHAT,
        TRANSFER_TYPE_YZH_BANK
    ]

    TRANSFER_STATUS_SUCCESS = 'success'  # 已转帐
    TRANSFER_STATUS_WITHDRAWAL = 'withdrawal'  # 提现中，待转帐
    TRANSFER_STATUS_PENDING = 'pending'  # 待提现
    TRANSFER_STATUS_IN_TRANSIT = 'in_transit'  # 在途
    TRANSFER_STATUS_CANCEL = 'cancel'  # 取消


    TRANSFER_STATUS = [
        TRANSFER_STATUS_SUCCESS,
        TRANSFER_STATUS_WITHDRAWAL,
        TRANSFER_STATUS_PENDING,
        TRANSFER_STATUS_IN_TRANSIT,
        TRANSFER_STATUS_CANCEL,
    ]
    incomes_order_id = StringField(unique=True, help_text='收益订单id')
    order_type = StringField(required=True, help_text='订单类型', choices=ORDER_TYPES)
    from_order_id = StringField(required=True, help_text='来源订单id')
    from_order_pay_at = StringField(required=True, help_text='来源订单支付时间')
    from_doctor_id = StringField(required=True, help_text='来源医生id')
    partner_id = StringField(help_text='合伙人id')
    agent_id = StringField(help_text='代理商id')
    doctor_id = StringField(required=True, help_text='医生id')
    user_id = StringField(required=True, help_text='用户id')
    desc = StringField(required=True, help_text='收益描述')
    cost = IntField(required=True, help_text='收益金额，单位：分')
    note_id = StringField(required=True, help_text='笔记id')
    thread_id = StringField(required=True, help_text='会话id')

    award_code = StringField(help_text='心意id')

    product_data = EmbeddedDocumentField(ProductDataObj, help_tex='产品订单信息')


    transfer_status = StringField(required=True, help_tex='付款状态', choices=TRANSFER_STATUS, default=TRANSFER_STATUS_PENDING)

    create_at = StringField(required=True)
    update_at = StringField(required=True)

    transfer_type = StringField(help_tex='付款类型', choices=TRANSFER_TYPES)

    payment_data = EmbeddedDocumentField(PaymentDataObj, help_tex='微信付款成功信息')



