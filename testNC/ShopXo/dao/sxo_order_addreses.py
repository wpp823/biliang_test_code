from base.base import mysql_conn_session
from model.sxo_order_address import SxoOrderAddressModel


class SxoOrderAddressDao():
    def __init__(self, log):
        self.log = log

    @mysql_conn_session
    def get_by_order_id(self, order_id) -> SxoOrderAddressModel:
        """
        通过订单号获取订单订单列表


        :param order_id:
        :return:
        """

        rows = self.conn.query(SxoOrderAddressModel).filter_by(order_id=order_id).first()

        if rows:
            return rows
        else:
            return None
