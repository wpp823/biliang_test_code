from typing import List
from base.base import mysql_conn_session
from model.sxo_order_aftersale import SxoOrderAftersaleModel


class SxoOrderAftersaleDao():
    def __init__(self, log):
        super().__init__(log)

    @mysql_conn_session
    def get_by_order_id(self, order_id) -> List[SxoOrderAftersaleModel]:
        """
        通过订单号获取订单订单列表


        :param order_id:
        :return:
        """

        rows = self.conn.query(SxoOrderAftersaleModel).filter_by(order_id=order_id).all()

        if rows:
            return rows
        else:
            return []
