
from mongoengine import DynamicDocument, StringField, IntField

class UserCoinRecordsModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "user_coin_records",
        'indexes': [
            {
                "fields": ["user_id", "coin_type", "status", "create_at", "overdue_at"],
                'name': '_fit_'
            }
        ]
    }

    COIN_TYPE_INVITE = 'invite'  # 邀请好友
    COIN_TYPE_TIMING = 'timing'  # 健康计时
    COIN_TYPE_SIGN_IN = 'sign_in'  # 签到
    COIN_TYPE_EXCHANGE_COUPONS = 'exchange_coupons'  # 兑换优惠券
    COIN_TYPE_RETURN_COUPONS = 'return_coupons'  # 退回优惠券
    COIN_TYPES = [
        COIN_TYPE_INVITE,
        COIN_TYPE_TIMING,
        COIN_TYPE_SIGN_IN,
        COIN_TYPE_EXCHANGE_COUPONS,
        COIN_TYPE_RETURN_COUPONS
    ]

    COIN_STATUS_NORMAL = 'normal'   # 正常
    COIN_STATUS_OVERDUE = 'overdue' # 过期
    COIN_STATUS = [
        COIN_STATUS_NORMAL,
        COIN_STATUS_OVERDUE
    ]

    record_id = StringField(required=True, unique=True, help_text='记录id,唯一id')
    coin_type = StringField(required=True, help_text='类型', choices=COIN_TYPES)
    user_id = StringField(required=True, help_text='用户id')
    coin = IntField(required=True, help_text='健康币数量')
    from_at = StringField(help_text='来源页面')
    status = StringField(required=True, help_text='状态', choices=COIN_STATUS)
    create_at = StringField(required=True)
    overdue_at = StringField(help_text='过期时间')

