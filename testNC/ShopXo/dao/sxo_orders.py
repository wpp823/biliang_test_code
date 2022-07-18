import arrow

from base.base import mysql_conn_session
from model.sxo_order import SxoOrderModel


class SxoOrdersDao():
    def __init__(self, log):
        super().__init__(log)

    @mysql_conn_session
    def add(self, order_data: SxoOrderModel):
        """添加订单"""

        data_dict = order_data

    @mysql_conn_session
    def get_by_order_no(self, order_no) -> SxoOrderModel:
        """
        通过订单号获取订单


        :param order_no:
        :return:
        """

        rows = self.conn.query(SxoOrderModel).filter_by(order_no=order_no).first()

        if rows:
            return rows
        else:
            return None

    @mysql_conn_session
    def update_order_send_data(self, order_id, status, express_id, express_number, delivery_time):
        """更新订单发货信息"""
        upd_time = arrow.now().timestamp

        upd_info = {
            SxoOrderModel.id: order_id,
            SxoOrderModel.status: status,
            SxoOrderModel.express_id: express_id,
            SxoOrderModel.express_number: express_number,
            SxoOrderModel.delivery_time: delivery_time,
            SxoOrderModel.upd_time: upd_time,
        }

        res = self.conn.query(SxoOrderModel).filter(SxoOrderModel.id == order_id).update(upd_info, synchronize_session="fetch")
        self.conn.commit()
        return res
        # "status": 3,
        # "express_id": 0,
        # "express_number": "",
        # "delivery_time": "",
        # "upd_time": ""
