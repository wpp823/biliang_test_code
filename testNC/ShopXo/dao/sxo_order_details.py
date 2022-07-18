from typing import List

from base.base import mysql_conn_session
from model.sxo_order_detail import SxoOrderDetailModel


class SxoOrderDetailsDao():
    def __init__(self, log):
        super().__init__(log)

    @mysql_conn_session
    def get_by_order_id(self, order_id) -> List[SxoOrderDetailModel]:
        """
        通过订单号获取订单


        :param order_id:
        :return:
        """

        rows = self.conn.query(SxoOrderDetailModel).filter_by(order_id=order_id).all()

        if rows:
            return rows
        else:
            return None
