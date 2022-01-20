from mongoengine import DynamicEmbeddedDocument, DynamicDocument, EmbeddedDocumentField, \
    StringField, IntField, ListField


class ProductInfoObj(DynamicEmbeddedDocument):
    """
    产品信息
    """
    meta = {'strict': False}
    product_id = IntField(help_text="商品id")
    sku_id = IntField(help_text="sku_id")
    count = IntField(help_text="sku数量")


class DetailObj(DynamicEmbeddedDocument):
    """
    详情
    """
    meta = {'strict': False}
    num = IntField(help_text="退款的数量")
    desc = StringField(help_text="没用")
    time = IntField(help_text="没用")
    receive_product = IntField(help_text="没用")
    cancel_time = IntField(help_text="取消时间")
    prove_imgs = ListField(help_text="用户上传的凭证")
    tel_number = StringField(help_text="用户电话")


class RefundInfoObj(DynamicEmbeddedDocument):
    """
    退款
    """
    meta = {'strict': False}
    amount = IntField(help_text="退款金额")


class ReturnInfoObj(DynamicEmbeddedDocument):
    """
    退货物流信息
    """
    meta = {'strict': False}
    waybill_id = StringField(help_text="退货快递单号")
    delivery_id = StringField(help_text="退货物流公司id")
    delivery_name = StringField(help_text="退货物流公司名字")


class MerchantUploadInfoObj(DynamicEmbeddedDocument):
    """
    线下处理信息
    """
    meta = {'strict': False}
    reject_reason = StringField(help_text="商家拒绝原因")
    refund_certificates = ListField(help_text="商家线下退款凭证")


class RefundRespObj(DynamicEmbeddedDocument):
    """
    无说明
    """
    meta = {'strict': False}
    code = StringField(help_text="无说明")
    ret = IntField(help_text="无说明")
    message = StringField(help_text="无说明")


class AfterSaleOrderModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "after_sale_order",
        'indexes': [
            {
                "fields": ["order_id", "status", "original_order_id"],
                'name': '_after_sale_order_fit_'
            }
        ]
    }

    AFTERSALESTATUS_INVALID = 0  # 无效
    USER_CANCELD = 1  # 用户取消申请
    MERCHANT_PROCESSING = 2  # 商家受理中
    MERCHANT_REJECT_REFUND = 4  # 商家拒绝退款
    MERCHANT_REJECT_RETURN = 5  # 商家拒绝退货退款
    USER_WAIT_RETURN = 6  # 待买家退货
    RETURN_CLOSED = 7  # 退货退款关闭
    MERCHANT_WAIT_RECEIPT = 8  # 待商家收货
    MERCHANT_OVERDUE_REFUND = 12  # 商家逾期未退款
    MERCHANT_REFUND_SUCCESS = 13  # 退款完成
    MERCHANT_RETURN_SUCCESS = 14  # 退货退款完成
    PLATFORM_REFUNDING = 15  # 平台退款中
    PLATFORM_REFUND_FAIL = 16  # 平台退款失败
    USER_WAIT_CONFIRM = 17  # // 待用户确认
    MERCHANT_REFUND_RETRY_FAIL = 18  # 商家打款失败，客服关闭售后
    MERCHANT_FAIL = 19  # 售后关闭
    AFTER_SALE_STATUS = [
        AFTERSALESTATUS_INVALID,
        USER_CANCELD,
        MERCHANT_PROCESSING,
        MERCHANT_REJECT_REFUND,
        MERCHANT_REJECT_RETURN,
        USER_WAIT_RETURN,
        RETURN_CLOSED,
        MERCHANT_WAIT_RECEIPT,
        MERCHANT_OVERDUE_REFUND,
        MERCHANT_REFUND_SUCCESS,
        MERCHANT_RETURN_SUCCESS,
        PLATFORM_REFUNDING,
        PLATFORM_REFUND_FAIL,
        USER_WAIT_CONFIRM,
        MERCHANT_REFUND_RETRY_FAIL,
        MERCHANT_FAIL,
    ]

    REFUND = 1  # 退款
    RETURN = 2  # 退货退款

    AFTER_SALE_TYPE = [
        REFUND,
        RETURN
    ]

    INCORRECT_SELECTION = 1  # 拍错 / 多拍
    NO_LONGER_WANT = 2  # 不想要了
    NO_EXPRESS_INFO = 3  # 无快递信息
    EMPTY_PACKAGE = 4  # // 包裹为空
    REJECT_RECEIVE_PACKAGE = 5  # 已拒签包裹
    NOT_DELIVERED_TOO_LONG = 6  # 快递长时间未送达
    NOT_MATCH_PRODUCT_DESC = 7  # 与商品描述不符
    QUALITY_ISSUE = 8  # 质量问题
    SEND_WRONG_GOODS = 9  # 卖家发错货
    THREE_NO_PRODUCT = 10  # 三无产品
    FAKE_PRODUCT = 11  # 假冒产品
    OTHERS = 12  # 其它

    AFTER_SALE_REASON = [
        INCORRECT_SELECTION,
        NO_LONGER_WANT,
        NO_EXPRESS_INFO,
        EMPTY_PACKAGE,
        REJECT_RECEIVE_PACKAGE,
        NOT_DELIVERED_TOO_LONG,
        NOT_MATCH_PRODUCT_DESC,
        QUALITY_ISSUE,
        SEND_WRONG_GOODS,
        THREE_NO_PRODUCT,
        FAKE_PRODUCT,
        OTHERS
    ]

    order_id = IntField(help_text="售后单号")
    status = StringField(help_text="售后单状态")
    openid = StringField(help_text="用户openid")
    original_order_id = IntField(help_text="售后单对应的订单号")
    details = EmbeddedDocumentField(DetailObj, help_text="售后详情")
    product_info = EmbeddedDocumentField(ProductInfoObj, help_text="产品数据")
    refund_info = EmbeddedDocumentField(RefundInfoObj, help_text="退款信息")
    return_info = EmbeddedDocumentField(ReturnInfoObj, help_text="退货信息")
    merchant_upload_info = EmbeddedDocumentField(MerchantUploadInfoObj, help_text="拒绝信息")
    create_time = IntField(help_text="售后单创建时间")  # 1591319454
    update_time = IntField(help_text="售后单更新时间")  # 1612754444
    reason = StringField(help_text="退款原因")
    refund_resp = EmbeddedDocumentField(RefundRespObj, help_text="售后单号")
    type = StringField(help_text="退款方式")
