
from mongoengine import *


class TransferInfoObj(DynamicEmbeddedDocument):
    """
    转帐信息
    """
    meta = {"strict": False}

    bank_name = StringField(help_tex='银行',)
    card_no = StringField(help_tex='银行卡号',)
    transfer_at = StringField(help_tex='转帐时间')

class OrdersModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "orders",
        'indexes': [
            {
                "fields": ["order_type", "user_id", "doctor_id", "note_id", "pay_status", "pay_type", "create_at",
                           "pay_at", "transaction_id", "out_trade_no"],
                'name': '_fit_'
            }
        ]
    }

    ORDER_TYPE_CONSULT = 'consult'  # 图文咨询
    ORDER_TYPE_PRETATION = 'pretation'  # 报告解读
    ORDER_TYPE_AWARD = 'award'  # 心意
    ORDER_TYPES = [
        ORDER_TYPE_CONSULT,
        ORDER_TYPE_PRETATION,
        ORDER_TYPE_AWARD,
    ]
    # 订单类型商品描述
    ORDER_DESC = {
        ORDER_TYPE_CONSULT: '图文咨询',
        ORDER_TYPE_PRETATION: '报告解读',
        ORDER_TYPE_AWARD: '心意',
    }

    PAY_TYPE_WECHAT = 'wechat'  # 微信支付
    PAY_TYPES = [
        PAY_TYPE_WECHAT
    ]

    PAY_STATUS_SUCCESS = 'success'  # 已支付
    PAY_STATUS_PENDING = 'pending'  # 待支付
    PAY_STATUS_REFUND_PENDING = 'refund_pending'  # 退款处理中
    PAY_STATUS_REFUND_SUCCESS = 'refund_success'  # 退款成功
    PAY_STATUS_DELETE = 'delete'  # 删除
    PAY_STATUS = [
        PAY_STATUS_SUCCESS,
        PAY_STATUS_PENDING,
        PAY_STATUS_REFUND_PENDING,
        PAY_STATUS_REFUND_SUCCESS,
        PAY_STATUS_DELETE,
    ]
    order_id = StringField(unique=True, help_text='订单id')
    order_type = StringField(required=True, help_text='订单类型', choices=ORDER_TYPES)
    user_id = StringField(required=True, help_text='用户id')
    doctor_id = StringField(required=True, help_text='医生id')
    description = StringField(required=True, help_text='商品描述')
    cost = IntField(required=True, help_text='费用金额，单位：分')
    note_id = StringField(required=True, help_text='笔记id')
    thread_id = StringField(help_text='会话id')
    award_code = StringField(help_text='心意id')

    pay_status = StringField(required=True, help_tex='支付状态', choices=PAY_STATUS, default=PAY_STATUS_PENDING)

    remark = StringField(help_tex='备注',)
    create_at = StringField(required=True)
    update_at = StringField(required=True)

    pay_type = StringField(help_tex='支付类型', choices=PAY_TYPES)
    wx_out_trade_no = StringField(help_tex='微信预支付订单id')
    wx_prepay_id = StringField(help_tex='微信预支付id')
    transaction_id = StringField(help_tex='交易流水id，支付成功后有此值')
    pay_at = StringField(help_tex='支付时间，支付成功后有此值')
    refund_id = StringField(help_tex='微信退款订单号，退款成功后有此值')
    refund_at = StringField(help_tex='退款时间，退款成功后有此值')

    transfer = BooleanField(help_tex='是否已转帐医生帐户', default=False)
    transfer_info = EmbeddedDocumentField(TransferInfoObj, help_tex='转帐信息')

