import arrow

from base.base import mysql_conn_session
from model.sxo_brand import SxoBrandModel


class SxoBrandsDao():
    def __init__(self, log):
        self.log = log

    @mysql_conn_session
    def add(self, name):

        now_at = arrow.now(tz="+08:00").timestamp
        sxo_brand_obj = SxoBrandModel()
        sxo_brand_obj.name = name
        sxo_brand_obj.add_time = now_at
        sxo_brand_obj.upd_time = now_at
        brand_id = None
        try:
            self.conn.add(sxo_brand_obj)
            self.conn.commit()  # 提交到数据库
            brand_id = sxo_brand_obj.id
        except:
            self.log.exception("[SxoBrandsDao.add][name:{}]".format(name))

        return brand_id

    @mysql_conn_session
    def get_by_name(self, name):
        """
        获取品牌信息

        :param name:
        :return:
        """

        rows = self.conn.query(SxoBrandModel).filter_by(name=name).first()

        if rows:
            return rows
        else:
            return None
