import arrow

from app.mongo_db.dao.orders import OrderDao
from app.mongo_db.dao.shopxo.sxo_order_addreses import SxoOrderAddressDao
from app.mongo_db.dao.shopxo.sxo_order_aftersales import SxoOrderAftersaleDao
from app.mongo_db.dao.shopxo.sxo_order_details import SxoOrderDetailsDao
from app.mongo_db.dao.shopxo.sxo_orders import SxoOrdersDao
from app.mongo_db.dao.shopxo.sxo_users import SxoUserDao
from app.mongo_db.model.order import OrderModel, OrderDetailObj, PayInfoObj, DeliveryInfoObj, AddressInfoObj, AftersaleDetailObj, AftersaleOrderObj, PriceInfoObj, ProductInfoObj, \
    SkuAttrObj, ExpressFeeObj
from app.util.shop.order import OrderItem


class ShopXoOrder:
    # MONGO_HOST_PART = "mongodb://root:@192.168.1.230"
    # #
    # # MONGO_HOST_PART = "mongodb://root:@dds-wz9db3743e6de5041152-pub.mongodb.rds.aliyuncs.com:3717"  # 测试服
    # # MONGO_HOST_PART = "mongodb://root:@dds-wz982bab2e6c05b42390-pub.mongodb.rds.aliyuncs.com:3717"  # 正式服
    #
    # MONGO_HOST_AUTH_DB = "admin"
    # MONGO_HOST_REPLICA_SET = None
    #
    # MONGO_HOST = MONGO_HOST_PART + "/" + MONGO_HOST_AUTH_DB
    # MONGO_DB_NAME = 'nightcrawler'
    #
    # DEP_NC_SERVER_NAME = 'nightcrawler'
    # DEP_NC_SERVER_PORT = 18851
    # DEP_NC_HOSTNAME = None

    def __init__(self, log):
        self.log = log
        # self.log = get_logger_3(name='ShopXoTools.log', log_root='./')
        # self._db = get_mongo(host=ShopXoOrder.MONGO_HOST_PART,
        #                      db=ShopXoOrder.MONGO_DB_NAME,
        #                      host_uri=ShopXoOrder.MONGO_HOST,
        #                      authentication_source=ShopXoOrder.MONGO_HOST_AUTH_DB,
        #                      replicaset=ShopXoOrder.MONGO_HOST_REPLICA_SET,
        #                      log=self.log,
        #                      )

    def shopxo_order_to_wx(self, shopxo_order_no) -> OrderItem:
        """
        shopxo订单同步到微信订单

        微信订单结构对应:
         order_detail.product_infos  --> sxo_order_detail
         order_detail.pay_info  -->  sxo_pay_log
         order_detail.price_info  -->
         order_detail.delivery_info:
                                    order_detail.delivery_info.address_info--> address_info
                                    order_detail.delivery_info.delivery_product_info-->

         order_id/status/create_time/update_time   -->  sxo_order

         aftersale_detail  --> sxo_order_aftersale

        """
        sxo_order_dao = SxoOrdersDao(log=self.log)
        sxo_user_dao = SxoUserDao(log=self.log)
        sxo_order_details_dao = SxoOrderDetailsDao(log=self.log)
        sxo_order_aftersale_dao = SxoOrderAftersaleDao(log=self.log)
        sxo_order_address_dao = SxoOrderAddressDao(log=self.log)
        wx_order_dao = OrderDao(log=self.log)

        order_data = None
        try:
            sxo_order_info = sxo_order_dao.get_by_order_no(order_no=shopxo_order_no)

            wx_order_obj = OrderModel(
                xlkk_order_id=shopxo_order_no,
                order_id=0,  # 订单ID
                order_source=OrderModel.ORDER_SOURCE_SHOPXO,
                out_order_id="",  # order.out_order_id 	string 	外部订单id
                status=sxo_order_info.status,  # order.status 	number 	商品状态
                create_time=arrow.get(sxo_order_info.add_time).to(tz="+08:00").format('YYYY-MM-DD HH:mm:ss'),  # order.create_time 	string 	创建时间  "2020-03-25 13:05:25"
                update_time=arrow.get(sxo_order_info.upd_time).to(tz="+08:00").format('YYYY-MM-DD HH:mm:ss')  # order.update_time 	string 	更新时间
                # ext_info = EmbeddedDocumentField(ExtInfoObj, help_text="openid")  #
                # products_ext = EmbeddedDocumentListField(ProductExtObj, help_text="每个产品的扩展信息")
            )
            # 获取用户openid
            sxo_user_id = sxo_order_info.user_id
            sxo_user_info = sxo_user_dao.get(user_id=sxo_user_id)
            sxo_user_openid = sxo_user_info.weixin_web_openid
            wx_order_obj.openid = sxo_user_openid

            # 订单详情====================================================
            order_detail = OrderDetailObj()

            # order_detail.product_infos
            sxo_order_id = sxo_order_info.id
            sxo_order_details = sxo_order_details_dao.get_by_order_id(order_id=sxo_order_id)
            product_infos = []
            for sxo_order_detail in sxo_order_details:
                product_infos.append(
                    ProductInfoObj(
                        # product_id=sxo_order.goods_id, #IntField(help_text="小商店内部商品ID") todo
                        # sku_id = IntField(help_text="小商店内部skuID")
                        # thumb_img = StringField(help_text="sku小图")
                        spu_code=sxo_order_detail.model,
                        sku_cnt=sxo_order_detail.buy_number,  # 购买个数
                        on_aftersale_sku_cnt=sxo_order_detail.returned_quantity,  # todo 正在售后/退款流程中的sku数量")
                        finish_aftersale_sku_cnt=sxo_order_detail.returned_quantity,  # todo 完成售后/退款的sku数量")
                        sale_price=int(float(sxo_order_detail.price)*100),
                        sku_attrs=[SkuAttrObj(
                            attr_key=item.get("type"),
                            attr_value=item.get("value"),
                        ) for item in eval(sxo_order_detail.spec)] if sxo_order_detail.spec else [],
                        title=sxo_order_detail.title,
                        sku_code=sxo_order_detail.spec_coding

                    )
                )
            order_detail.product_infos = product_infos

            # order_detail.pay_info
            pay_info = PayInfoObj(
                pay_method="",  # 支付方式（目前只有微信支付）
                prepay_id="",  # 预支付ID
                transaction_id="",  # 支付订单号
                prepay_time="",  # 预付款时间
                pay_time=arrow.get(sxo_order_info.pay_time).to(tz="+08:00").format('YYYY-MM-DD HH:mm:ss') if sxo_order_info.pay_time > 0 else "",
            )
            order_detail.pay_info = pay_info

            # order_detail.price_info支付金额
            price_info = PriceInfoObj(
                product_price=sum([sxo_order_detail.buy_number * sxo_order_detail.price for sxo_order_detail in sxo_order_details]) * 100,
                order_price=sxo_order_info.total_price * 100,
                discounted_price=sxo_order_info.preferential_price,
                is_discounted=True if sxo_order_info.preferential_price else False

            )
            # 运费获取
            freight = 0  # 默认
            if sxo_order_info.increase_price > 0:
                ex_data = sxo_order_info.extension_data
                if ex_data:
                    for item in eval(ex_data):
                        if item.get("name", None) == '运费':
                            freight = int(item.get("price", 0)) * 100
            price_info.freight = freight

            order_detail.price_info = price_info

            # order_detail.delivery_info
            # 获取shopxo快递地址
            sxo_order_address_info = sxo_order_address_dao.get_by_order_id(order_id=sxo_order_id)
            delivery_info = DeliveryInfoObj(
                delivery_method="快递",  # 快递方式（目前只有快递)
                delivery_time="",
                delivery_product_info=[],  # 发货商品信息 待金蝶回写
                express_fee=[],  # 快递费用
                # delivery_time = StringField(help_text="发货时间")
                # offline_delivery_time = IntField(help_text="线下配送时间")
                # offline_pickup_time = IntField(help_text="线下自提时间")
                # ship_done_time = IntField(help_text="配送完成时间")
                # delivery_product_info = EmbeddedDocumentListField(DeliveryProductInfoObj, help_text="发货商品信息")
                # pickup_address = EmbeddedDocumentField(PickupAddressObj, help_text="自提地址信息")
            )

            # order_detail.delivery_info.address_info
            address_info = AddressInfoObj(
                user_name=sxo_order_address_info.name,  # StringField(help_text="收货人姓名")
                postal_code="",  # StringField(help_text="邮编")
                province_name=sxo_order_address_info.province_name,  # StringField(help_text="国标收货地址第一级地址")
                city_name=sxo_order_address_info.city_name,  # StringField(help_text="国标收货地址第二级地址")
                county_name=sxo_order_address_info.county_name,  # StringField(help_text="国标收货地址第三级地址")
                detail_info=sxo_order_address_info.address,  # StringField(help_text="详细收货地址信息")
                national_code='440402002',  # StringField(help_text="收货地址国家码")
                tel_number=sxo_order_address_info.tel,  # StringField(help_text="收货人手机号码")

            )
            delivery_info.address_info = address_info
            order_detail.delivery_info = delivery_info
            # order_detail.delivery_info.express_info

            wx_order_obj.order_detail = order_detail

            # ======================================================order_detail
            # coupon_info = EmbeddedDocumentField(CouponInfoObj, help_text="优惠券信息")

            # 获取shopxo售后订单
            sxo_order_aftersales = sxo_order_aftersale_dao.get_by_order_id(order_id=sxo_order_id)

            aftersale_detail = AftersaleDetailObj(
                on_aftersale_order_cnt=0,
                aftersale_order_list=[
                    AftersaleOrderObj(aftersale_order_id=row_data.id)
                    for row_data in sxo_order_aftersales
                ]
            )
            wx_order_obj.aftersale_detail = aftersale_detail

            order_item = wx_order_obj.to_mongo().to_dict()
            order_data = OrderItem(**order_item)


        except:
            self.log.exception("[ShopXoOrder.shopxo_order_to_wx][order_id:{}]".format(shopxo_order_no))

        return order_data

# if __name__ == '__main__':
#     shopxo_order = ShopXoOrder()
#     shopxo_order.shopxo_order_to_wx(shopxo_order_no="20220706100525197042")

# old_order_info = wx_order_dao.get_by_xlkk_order_id(xlkk_order_id=shopxo_order_no)
# if old_order_info:
#     res = wx_order_dao.update_by_xlkk_order_id(order_item=OrderItem(**order_item), order_source=OrderModel.ORDER_SOURCE_SHOPXO, xlkk_order_id=shopxo_order_no)
# else:
#     # 添加订单
#
#     res = wx_order_dao.add(OrderItem(**order_item))
#     self.log.info("add order order_item:{},res:{}".format(order_item, res))
