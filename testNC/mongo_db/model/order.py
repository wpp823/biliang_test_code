from mongoengine import DynamicEmbeddedDocument, DynamicDocument, EmbeddedDocument, EmbeddedDocumentField, \
    StringField, DateTimeField, IntField, DictField, ListField, EmbeddedDocumentListField, BooleanField, SequenceField

from Nightcrawler_client.constant import ORDER_STATUS_PEND, ORDER_STATUS_COLL, ORDER_STATUS_RECV, \
    ORDER_STATUS_TO_WRIT, ORDER_STATUS_TO_SHIP, ORDER_STATUS_PART_SHIP, ORDER_STATUS_TO_RECE, ORDER_STATUS_COMP, \
    ORDER_STATUS_COMP_CANC, ORDER_STATUS_OVER_TIME, SELF_STATUS_MAP


class SkuAttrObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    attr_key = StringField(help_text="自定义属性key")
    attr_value = StringField(help_text="自定义属性value")


class ProductInfoObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    product_id = IntField(help_text="小商店内部商品ID")
    sku_id = IntField(help_text="小商店内部skuID")
    thumb_img = StringField(help_text="sku小图")
    sku_cnt = IntField(help_text="sku数量")
    on_aftersale_sku_cnt = IntField(help_text="正在售后/退款流程中的sku数量")
    finish_aftersale_sku_cnt = IntField(help_text="完成售后/退款的sku数量")
    sale_price = IntField(help_text="售卖价格（单位：分）")
    sku_attrs = EmbeddedDocumentListField(SkuAttrObj, help_text="自定义属性")
    title = StringField(help_text="名称")
    sku_code = StringField(help_text="sku_code") # 作用未知




class PayInfoObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    pay_method = StringField(help_text="支付方式（目前只有微信支付）")
    prepay_id = StringField(help_text="预支付ID")
    transaction_id = StringField(help_text="支付订单号")
    prepay_time = StringField(help_text="预付款时间")
    pay_time = StringField(help_text="付款时间")


class PriceInfoObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    product_price = IntField(help_text="商品金额（单位：分）")
    order_price = IntField(help_text="订单金额（单位：分）")
    freight = IntField(help_text="运费（单位：分）")
    discounted_price = IntField(help_text="优惠金额（单位：分）")
    is_discounted = BooleanField(help_text="是否有优惠（false：无优惠/true：有优惠）")


class AddressInfoObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    username = StringField(help_text="收货人姓名")
    postal_code = StringField(help_text="邮编")
    province_name = StringField(help_text="国标收货地址第一级地址")
    city_name = StringField(help_text="国标收货地址第二级地址")
    county_name = StringField(help_text="国标收货地址第三级地址")
    detail_info = StringField(help_text="详细收货地址信息")
    national_code = StringField(help_text="收货地址国家码")
    tel_number = StringField(help_text="收货人手机号码")


class PickupAddressObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    province_name = StringField(help_text="自提地址国标第一级地址（自提订单才有该信息）")
    city_name = StringField(help_text="自提地址国标第二级地址（自提订单才有该信息）")
    county_name = StringField(help_text="自提地址国标第三级地址（自提订单才有该信息）")
    detail_info = StringField(help_text="自提地址详细信息（自提订单才有该信息")
    house_number = StringField(help_text="自提地址门牌号（自提订单才有该信息，可能为空）")
    tel_number = StringField(help_text="自提商家联系号码（自提订单才有该信息）")


class ExpressFeeObj(DynamicEmbeddedDocument):
    meta = {'strict': False}

    shipping_method = StringField(help_text="配送方式")
    distance = IntField(help_text="线下自提,同城配送距离")


class DeliveryProductInfoObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    waybill_id = StringField(help_text="快递单号")
    waybill_token = StringField(help_text="waybill_token")
    delivery_id = StringField(help_text="快递公司编号")
    delivery_time = IntField(help_text="delivery_time")
    is_all_product = BooleanField(help_text="是否所有商品")
    product_infos = EmbeddedDocumentListField(ProductInfoObj, help_text="已发货商品列表")




class DeliveryInfoObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    delivery_method = StringField(help_text="快递方式（目前只有快递)")
    delivery_time = StringField(help_text="发货时间")
    offline_delivery_time = IntField(help_text="线下配送时间")
    offline_pickup_time = IntField(help_text="线下自提时间")
    ship_done_time = IntField(help_text="配送完成时间")

    delivery_product_info = EmbeddedDocumentListField(DeliveryProductInfoObj, help_text="发货商品信息")
    pickup_address = EmbeddedDocumentField(PickupAddressObj, help_text="自提地址信息")
    address_info = EmbeddedDocumentField(AddressInfoObj, help_text="快递地址信息")
    express_fee = EmbeddedDocumentListField(ExpressFeeObj, help_text="快递费用")

class CouponInfoObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    coupon_id = ListField(help_text="优惠券id")

class OrderDetailObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    # 订单详情
    product_infos = EmbeddedDocumentListField(ProductInfoObj, help_text="商品列表")
    pay_info = EmbeddedDocumentField(PayInfoObj, help_text="支付信息")
    delivery_info = EmbeddedDocumentField(DeliveryInfoObj, help_text="快递信息")
    price_info = EmbeddedDocumentField(PriceInfoObj, help_text="支付金额")
    coupon_info = EmbeddedDocumentField(CouponInfoObj, help_text="优惠券信息")


class AftersaleOrderObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    aftersale_order_id = IntField(help_text="售后订单号")


class AftersaleDetailObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    aftersale_order_list = EmbeddedDocumentListField(AftersaleOrderObj, help_text="售后订单列表")
    on_aftersale_order_cnt = IntField(help_text="售后订单数量")


class ExtInfoObj(DynamicEmbeddedDocument):
    meta = {'strict': False}
    customer_notes = StringField(help_text="用户备注")
    merchant_notes = StringField(help_text="商家备注")


class ProductExtObj(DynamicEmbeddedDocument):
    '''
    产品的扩展信息，这里的 product_id和sku_id 要与order_detail.product_infos 的保持一致。
    '''
    meta = {'strict': False}
    product_id = IntField(help_text="小商店内部商品ID")
    sku_id = IntField(help_text="小商店内部skuID")
    hot_val = IntField(help_text='可分得的佣金/每个SKU，单位分')
    referrer_doctor_id = StringField(help_text="推荐医生id")
    
    def to_dict(self):
        return {
            ProductExtObj.hot_val.name: self.hot_val,
            ProductExtObj.product_id.name: self.product_id,
            ProductExtObj.sku_id.name: self.sku_id,
            ProductExtObj.referrer_doctor_id.name: self.referrer_doctor_id
        }


class OrderModel(DynamicDocument):
    meta = {
        'strict': False,
        "collection": "orders",
        'indexes': [
            {
                "fields": ["order_id", "status", "ext_info"],
                'name': '_order_fit_'
            }
        ]
    }

    order_id = IntField(help_text="订单ID")  # order.order_id 	number 	订单ID
    out_order_id = StringField(help_text="外部订单id")  # order.out_order_id 	string 	外部订单id
    status = IntField(help_text="商品状态")  # order.status 	number 	商品状态
    create_time = StringField(help_text="创建时间")  # order.create_time 	string 	创建时间  "2020-03-25 13:05:25"
    update_time = StringField(help_text="更新时间")  # order.update_time 	string 	更新时间
    order_detail = EmbeddedDocumentField(OrderDetailObj, help_text="订单详情")
    openid = StringField(help_text="openid")
    ext_info = EmbeddedDocumentField(ExtInfoObj, help_text="openid")  # 用户的openid，用于物流助手接口

    aftersale_detail = EmbeddedDocumentField(AftersaleDetailObj, help_text="售后详情")
    products_ext = EmbeddedDocumentListField(ProductExtObj, help_text="每个产品的扩展信息")

    @property
    def custom_order_status(self):
        '''
        自有订单状态。
        :return:    str
        '''

        self_status = SELF_STATUS_MAP.get(self.status, None)
        return self_status
