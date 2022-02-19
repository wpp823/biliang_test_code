from Nightcrawler_client.constant import ORDER_STATUS_COMP
from app.mongo_db.model.order import OrderModel, OrderDetailObj, ExtInfoObj, ProductInfoObj, AftersaleDetailObj, \
    PriceInfoObj, DeliveryInfoObj, PayInfoObj, SkuAttrObj, DeliveryProductInfoObj, PickupAddressObj, AddressInfoObj, \
    ExpressFeeObj, AftersaleOrderObj, ProductExtObj, CouponInfoObj
from app.util.shop.order import OrderItem


class OrderDao():

    def __init__(self, log):
        self.log = log

    def add(self, order_item: OrderItem):
        """
        添加订单
        :param order_item:
        :return:
        """
        try:
            order_obj = OrderModel()
            order_obj.order_id = order_item.order_id  # 订单ID
            order_obj.out_order_id = order_item.get("out_order_id", None)  # 外部订单id
            order_obj.status = order_item.get("status", None)  # 商品状态
            order_obj.create_time = order_item.get("create_time", None)  # 创建时间
            order_obj.update_time = order_item.get("update_time", None)  # 更新时间

            order_obj.openid = order_item.get("openid", None)
            order_obj.ext_info = ExtInfoObj(**order_item.get("ext_info", None))
            order_obj.products_ext = order_item.get("products_ext", None)

            # 订单内容详情
            order_detail = OrderDetailObj()
            if order_item.get("order_detail"):
                # 商品信息
                product_infos = order_item.product_infos
                for item in product_infos:
                    item[ProductInfoObj.sku_attrs.name] = [SkuAttrObj(**temp) for temp in item.get("sku_attrs")]

                order_detail.product_infos = [ProductInfoObj(**item) for item in product_infos]
                order_detail.price_info = PriceInfoObj(**order_item.price_info)
                order_detail.pay_info = PayInfoObj(**order_item.pay_info)

                delivery_item = order_item.delivery_info
                if order_item.pickup_address:
                    delivery_item[DeliveryInfoObj.pickup_address.name] = PickupAddressObj(**order_item.pickup_address)
                delivery_item[DeliveryInfoObj.address_info.name] = AddressInfoObj(**order_item.address_info)
                delivery_item[DeliveryInfoObj.express_fee.name] = [ExpressFeeObj(**item) for item in
                                                                   order_item.express_fee]
                # 物流信息
                if order_item.delivery_product_info:
                    for tem_obj in order_item.delivery_product_info:
                        if tem_obj.get("product_infos"):
                            tem_obj["product_infos"] = [ProductInfoObj(**item) for item in tem_obj.get("product_infos")]
                    delivery_item[DeliveryInfoObj.delivery_product_info.name] = [DeliveryProductInfoObj(**item) for item in order_item.delivery_product_info]
                order_detail.delivery_info = DeliveryInfoObj(**delivery_item)

                # 优惠券信息
                if order_item.coupon_info:
                    order_detail.coupon_info = CouponInfoObj(**order_item.coupon_info)

            order_obj.order_detail = order_detail  # "订单详情")

            # 获取售后单号
            if order_item.aftersale_detail:
                aftersale_detail = order_item.aftersale_detail
                # 是否有售后订单列表
                if aftersale_detail.get("aftersale_order_list"):
                    tmp_item_list = [AftersaleOrderObj(**tem_item) for tem_item in
                                     aftersale_detail.get("aftersale_order_list")]
                    aftersale_detail[AftersaleDetailObj.aftersale_order_list.name] = tmp_item_list
                order_obj.aftersale_detail = AftersaleDetailObj(**aftersale_detail)

            res = OrderModel.save(order_obj)
        except:
            if self.log:
                self.log.exception('[OderDao.add],[fail],[order_item]:{}'.format(order_item))
            return False
        return res

    def update(self, order_item: OrderItem, order_id: int, except_products_ext: bool = True):
        """
        更新订单信息
        :param order_item:      [OrderItem]从微信小商店获取到的订单对象。
        :param order_id:
        :param except_products_ext:    [bool]True代表，products_ext 不进行更新。
        :return:
        """

        fit = {
            OrderModel.order_id.name: int(order_id)
        }
        if not order_item:
            return False

        # 代表不更新products_ext字段。
        if except_products_ext:
            del order_item["products_ext"]
        else:
            new_list = []
            for tmp_ext in order_item["products_ext"]:
                if isinstance(tmp_ext, ProductExtObj):
                    new_list.append(tmp_ext.to_dict())
                else:
                    new_list.append(tmp_ext)

            order_item["products_ext"] = new_list

        update_info = {
            "$set": order_item
        }

        # self.log.info("[OrderDao.update],[order_id:{}]".format(order_id))
        res = None

        try:
            res = OrderModel.objects(__raw__=fit).update(__raw__=update_info)
            self.log.info("[OrderDao.update][order_id:{} res:{}, set:{}]".format(order_id, res, order_item))

        except:
            self.log.exception(
                "[OrderDao.update],[fail],[prams order_id:{},order_item:{}]".format(order_id, order_item))
        return res

    def get_order_by_id(self, order_id: int, fields=[]):
        """
        通过订单id获取订单
        :param order_id:
        :param fields:
        :return:
        """
        fit = {
            OrderModel.order_id.name: int(order_id)
        }
        res = None
        try:
            if fields:
                res = OrderModel.objects(__raw__=fit).only(*fields).first()
            else:
                res = OrderModel.objects(__raw__=fit).first()
        except:
            self.log.exception('[OrderDao.get_order_by_id_fail][order_id:{}]'.format(order_id))

        return res

    def get_max_order_update_time(self) -> str:
        """
        获取所有订单最大更新时间
        :return: e.g:2021-11-13 09:31:41
        """
        fit = {}
        fields = [OrderModel.update_time.name]
        res = ""
        sort = "-{}".format(OrderModel.update_time.name)
        try:
            res = OrderModel.objects(__raw__=fit).only(*fields).order_by(sort).first()
            if res:
                return res.update_time
        except:
            self.log.exception('[get_max_order_update_time]')

        return res

    def product_sales_volume(self, product_id: int) -> int:
        """
        根据商品id计算销量
        :param product_id:
        :return:
        """
        sales_volume = 0
        fit = {
            "{}.{}.{}".format(OrderModel.order_detail.name, OrderDetailObj.product_infos.name,
                              ProductInfoObj.product_id.name): int(product_id),
            "{}".format(OrderModel.status.name): ORDER_STATUS_COMP  # 订单状态为100
        }
        pipeline = [
            {"$unwind": "${}.{}".format(OrderModel.order_detail.name, OrderDetailObj.product_infos.name)},
            {
                '$group': {
                    "_id": "{}.{}.{}".format(OrderModel.order_detail.name, OrderDetailObj.product_infos.name,
                                             ProductInfoObj.product_id.name),
                    "sum": {"$sum": "${}.{}.{}".format(OrderModel.order_detail.name, OrderDetailObj.product_infos.name,
                                                       ProductInfoObj.sku_cnt.name)},
                }
            }
        ]

        data = OrderModel.objects(__raw__=fit).aggregate(*pipeline)
        if data:
            data = list(data)
            sales_volume = data[0]['sum'] if len(data) > 0 else 0

        return sales_volume

    def get_hot_val(self, product_id: int, sku_id: int, order_id: int) -> int:
        """
        获取的订单扩展信息的热力值
        :param order_id:
        :param product_id:
        :param sku_id:
        :return: 默认返回0 代表无热力值
        """
        res = 0
        fit = {
            "{}".format(OrderModel.order_id.name): order_id,
            "{}.{}".format(OrderModel.products_ext.name, ProductExtObj.product_id.name): product_id,
            "{}.{}".format(OrderModel.products_ext.name, ProductExtObj.sku_id.name): sku_id
        }

        fields = [OrderModel.products_ext.name]
        try:
            res = OrderModel.objects(__raw__=fit).only(*fields).first()
            if res:
                return res.hot_val
        except:
            self.log.exception(
                '[OrderDao.get_hot_val_fail][product_id:{},sku_id:{},order_id:{}]'.format(product_id, sku_id,order_id))
        return res

    def get_product_ext_obj(self, product_id: int, sku_id: int, order_id: int):
        """
        获取扩展信息

        :param product_id:
        :param sku_id:
        :param order_id:
        :return:
        """
        res = None
        fit = {
            OrderModel.order_id.name: int(order_id),
            "{}.{}".format(OrderModel.products_ext.name, ProductExtObj.product_id.name): int(product_id),
            "{}.{}".format(OrderModel.products_ext.name, ProductExtObj.sku_id.name): int(sku_id)
        }
        fields = [OrderModel.products_ext.name]
        try:
            res = OrderModel.objects(__raw__=fit).only(*fields).first()
        except:
            self.log.exception(
                '[OrderDao.get_product_ext_obj_fail][product_id:{},sku_id:{},order_id:{}]'.format(product_id, sku_id,order_id))
        return res
