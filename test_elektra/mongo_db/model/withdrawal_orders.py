
from mongoengine import DynamicDocument, EmbeddedDocumentField, StringField, IntField, ListField
from app.mongo_db.model.doctor_incomes_orders import PaymentDataObj, DoctorIncomesOrdersModel

class WithdrawalOrdersModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "withdrawal_orders",
        'indexes': [
            {
                "fields": ["transfer_type", "doctor_id", "income_order_ids", "transfer_status",  "create_at",
                           "update_at", "payment_data.openid",
                           "payment_data.partner_trade_no", "payment_data.payment_no", "payment_data.payment_time"],
                'name': '_fit_'
            }
        ]
    }


    TRANSFER_STATUS_SUCCESS = 'success'  # 已转帐
    TRANSFER_STATUS_PENDING = 'pending'  # 待转帐
    TRANSFER_STATUS_PROCESSING = 'processing'  # 转帐中
    TRANSFER_STATUS = [
        TRANSFER_STATUS_SUCCESS,
        TRANSFER_STATUS_PENDING,
        TRANSFER_STATUS_PROCESSING,
    ]
    withdrawal_order_id = StringField(unique=True, help_text='提现订单id')
    doctor_id = StringField(required=True, help_text='医生id')
    income_order_ids = ListField(help_text='收益订单id列表')
    description = StringField(required=True, help_text='转帐描述')
    income_amount = IntField(required=True, help_text='提现金额，单位：分')
    income_tax = IntField(required=True, help_text='个人扣除服务费或所得税，单位：分')
    transfer_amount = IntField(required=True, help_text='转帐金额，扣除服务费后剩余金额，单位：分')
    transfer_type = StringField(help_text='转帐类型', choices=DoctorIncomesOrdersModel.TRANSFER_TYPES)
    transfer_status = StringField(required=True, help_tex='转帐状态', choices=TRANSFER_STATUS, default=TRANSFER_STATUS_PENDING)

    remark = StringField(help_tex='备注',)
    create_at = StringField(required=True)
    update_at = StringField(required=True)

    payment_data = EmbeddedDocumentField(PaymentDataObj, help_tex='微信付款成功信息')

