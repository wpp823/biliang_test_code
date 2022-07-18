from base.base import mysql_conn_session
from model.sxo_user import SxoUserModel


class SxoUserDao():
    def __init__(self, log):
        self.log = log

    @mysql_conn_session
    def get(self, user_id):
        """
        通过订单号获取订单


        :param user_id:
        :return:
        """

        rows = self.conn.query(SxoUserModel).filter_by(id=user_id).first()

        if rows:
            return rows
        else:
            return None
