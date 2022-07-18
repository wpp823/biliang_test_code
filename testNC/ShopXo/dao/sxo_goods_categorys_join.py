import arrow

from base.base import mysql_conn_session
from model.sxo_goods_category_join import SxoGoodsCategoryJoinModel


class SxoGoodsCategorysJoinDao():
    def __init__(self, log):
        self.log = log

    @mysql_conn_session
    def add(self, data: SxoGoodsCategoryJoinModel):
        """添加"""
        now_at = arrow.now().timestamp
        data.add_time = now_at

        sxo_goods_category_join_id = None
        try:
            self.conn.add(data)  # 添加到session
            self.conn.commit()  # 提交到数据库
            sxo_goods_category_join_id = data.id
        except:
            self.log.exception("[SxoGoodsCategorysJoinDao.add]")

        return sxo_goods_category_join_id

    @mysql_conn_session
    def get_by_ids(self, goods_id, category_id):
        """获取"""
        data = self.conn.query(SxoGoodsCategoryJoinModel).filter_by(goods_id=goods_id, category_id=category_id).first()

        return data

    @mysql_conn_session
    def update(self, sxo_goods_categorys_join_id, data: SxoGoodsCategoryJoinModel):
        """

        :param sxo_goods_categorys_join_id:
        :param data:
        :return:
        """

        data_dict = data.to_dict()
        data_dict.pop("add_time", 404)
        data_dict.pop("id", 404)
        res = self.conn.query(SxoGoodsCategoryJoinModel).filter(
            SxoGoodsCategoryJoinModel.id == sxo_goods_categorys_join_id).update(data_dict, synchronize_session="fetch")
        return res
