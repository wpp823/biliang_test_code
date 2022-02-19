from app.mongo_db.model.after_sale_order import AfterSaleOrderModel, DetailObj, ProductInfoObj, RefundInfoObj, ReturnInfoObj, MerchantUploadInfoObj, RefundRespObj
from app.util.shop.order import AfterSaleOrder


class AfterSaleOrderDao():

    def __init__(self, log):
        self.log = log

    def add(self, after_order_item: AfterSaleOrder):
        """
        添加售后单

        :param after_order_item:
        :type after_order_item:
        :return:
        :rtype:
        """

        after_sale_order_obj = AfterSaleOrderModel()
        try:
            after_sale_order_obj.order_id = after_order_item.order_id  # 订单号
            after_sale_order_obj.status = after_order_item.get("status")  # 订单状态
            after_sale_order_obj.openid = after_order_item.get("openid")  # 用户openid
            after_sale_order_obj.details = DetailObj(**after_order_item.details)  # 售后详情
            after_sale_order_obj.original_order_id = after_order_item.original_order_id  # 售后单对应的订单号
            after_sale_order_obj.product_info = ProductInfoObj(**after_order_item.product_info)  # 产品信息
            after_sale_order_obj.refund_info = RefundInfoObj(**after_order_item.refund_info)  # 退款信息
            after_sale_order_obj.return_info = ReturnInfoObj(**after_order_item.return_info)  # 退货信息
            after_sale_order_obj.merchant_upload_info = MerchantUploadInfoObj(**after_order_item.merchant_upload_info)  # 拒绝信息
            after_sale_order_obj.create_time = after_order_item.get("create_time")  # 售后单创建时间
            after_sale_order_obj.update_time = after_order_item.get("update_time")  # 售后单更新时间
            after_sale_order_obj.reason = after_order_item.get("reason")  # 退款原因
            after_sale_order_obj.refund_resp = RefundRespObj(**after_order_item.refund_resp)
            after_sale_order_obj.type = after_order_item.get("type")  # 退款方式

            res = AfterSaleOrderModel.save(after_sale_order_obj)
            if res:
                self.log.info("[AfterSaleOrderDao.add_ok],[order_id:{},original_order_id:{}]".format(after_order_item.order_id, after_order_item.original_order_id))
            else:
                self.log.error("[AfterSaleOrderDao.add],[add_error],[after_order_item:{}]".format(after_order_item))
        except Exception as e:
            self.log.exception("[AfterSaleOrderDao.add],[add_fail],[after_order_item:{}]".format(after_order_item))

    def update(self, after_order_item: AfterSaleOrder, order_id: int):
        """
        更新售后单

        :param order_id:
        :type order_id:
        :param after_order_item:
        :type after_order_item:
        :return:
        :rtype:
        """

        fit = {
            AfterSaleOrderModel.order_id.name: order_id
        }
        if not after_order_item:
            return False

        update_info = {
            "$set": after_order_item
        }
        try:
            res = AfterSaleOrderModel.objects(__raw__=fit).update(__raw__=update_info)
            if res:
                self.log.info("[AfterSaleOrderDao.update_ok],[order_id:{},original_order_id:{}]".format(after_order_item.order_id, after_order_item.original_order_id))
        except:
            self.log.exception(
                "[AfterSaleOrderDao.update],[fail],[order_id:{},order_item:{}]".format(order_id, after_order_item))
            return False
        return res

    def get_by_order_id(self, order_id: int):
        """
        获取售后订单id,判断订单是否存在

        :param order_id:
        :type order_id:
        :return:
        :rtype:
        """
        fit = {
            AfterSaleOrderModel.order_id.name: order_id
        }
        fields = [AfterSaleOrderModel.order_id.name]

        res = AfterSaleOrderModel.objects(__raw__=fit).only(*fields).first()

        return res
