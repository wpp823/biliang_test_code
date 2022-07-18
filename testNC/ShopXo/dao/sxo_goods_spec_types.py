import arrow

from base.base import mysql_conn_session
from model.sxo_goods_spec_type import SxoGoodsSpecTypeModel


class SxoGoodsSpecTypesDao():
    def __init__(self, log):
        self.log = log

    @mysql_conn_session
    def add(self, goods_id, value, name):
        """

        :param goods_id:
        :param value:
        :param name:
        :return:
        """
        sxo_goods_spec_type_obj = SxoGoodsSpecTypeModel(
            goods_id=goods_id,
            value=value,
            name=name,
            add_time=arrow.now(tz="+08:00").timestamp
        )
        goods_spec_type_id = None

        try:
            self.conn.add(sxo_goods_spec_type_obj)
            self.conn.commit()
            goods_spec_type_id = sxo_goods_spec_type_obj.id
        except:
            self.log.exception("[SxoGoodsSpecTypesDao.add]")

        return goods_spec_type_id

    @mysql_conn_session
    def get_by_goods_id(self, goods_id):
        """通过goods_id和编码获取"""

        rows = self.conn.query(SxoGoodsSpecTypeModel).filter_by(goods_id=goods_id).first()
        return rows

    @mysql_conn_session
    def update(self, goods_spec_type_id, data: SxoGoodsSpecTypeModel):
        """更新"""
        dict_data = data.to_dict()

        dict_data.pop("add_time", "404")  # SEO标题
        dict_data.pop("id", "404")

        rows = self.conn.query(SxoGoodsSpecTypeModel).filter(SxoGoodsSpecTypeModel.id == goods_spec_type_id).update(dict_data, synchronize_session="fetch")
        return rows
