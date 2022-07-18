import arrow

from base.base import mysql_conn_session
from model.sxo_goods_spec_value import SxoGoodsSpecValueModel


class SxoGoodsSpecValuesDao():
    def __init__(self, log):
        self.log = log

    @mysql_conn_session
    def add(self, goods_id, goods_spec_base_id, value):
        """

        :param goods_spec_base_id:
        :param goods_id:
        :param value:
        :return:
        """
        sxo_goods_spec_value_obj = SxoGoodsSpecValueModel(
            goods_id=goods_id,
            goods_spec_base_id=goods_spec_base_id,
            value=value,
            add_time=arrow.now(tz="+08:00").timestamp
        )
        goods_spec_value_id = None

        try:
            self.conn.add(sxo_goods_spec_value_obj)
            self.conn.commit()
            goods_spec_value_id = sxo_goods_spec_value_obj.id
        except:
            self.log.exception("[SxoGoodsSpecValuesDao.add]")

        return goods_spec_value_id

    @mysql_conn_session
    def get_by_goods_id_spec_base_id(self, goods_id, goods_spec_base_id):
        """

        :param goods_id:
        :param goods_spec_base_id:
        :return:
        """
        rows = self.conn.query(SxoGoodsSpecValueModel).filter_by(goods_id=goods_id, goods_spec_base_id=goods_spec_base_id).first()
        return rows

    @mysql_conn_session
    def update(self, spec_value_id, data: SxoGoodsSpecValueModel):
        """更新"""

        dict_data = data.to_dict()

        dict_data.pop("id", "404")
        dict_data.pop("add_time", "404")
        res = self.conn.query(SxoGoodsSpecValueModel).filter(SxoGoodsSpecValueModel.id == spec_value_id).update(dict_data, synchronize_session="fetch")
        return res
