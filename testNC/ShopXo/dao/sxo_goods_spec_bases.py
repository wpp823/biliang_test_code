import arrow

from base.base import mysql_conn_session
from model.sxo_goods_spec_base import SxoGoodsSpecBaseModel


class SxoGoodsSpecBaseDao():
    """商品规格基础表"""

    def __init__(self, log):
        self.log = log
        # self.session = sessionmaker(self._engine)()  # 构建session对象

    @mysql_conn_session
    def add(self, goods_id, price, inventory, coding, original_price, weight: float = None, barcode: str = None, extends: str = None):
        """
        添加
        :param extends:
        :param goods_id:
        :param price:
        :param inventory:
        :param weight:
        :param coding:
        :param barcode:
        :param original_price:
        :return:
        """
        sxo_good_spec_base_obj = SxoGoodsSpecBaseModel(

            goods_id=goods_id,
            price=price,
            inventory=inventory,
            coding=coding,
            original_price=original_price,
            add_time=arrow.now(tz="+08:00").timestamp
        )
        if weight:
            sxo_good_spec_base_obj.weight = weight
        if extends:
            sxo_good_spec_base_obj.extends = extends
        if barcode:
            sxo_good_spec_base_obj.barcode = barcode
        spec_base_id = None
        try:
            self.conn.add(sxo_good_spec_base_obj)
            self.conn.commit()
            spec_base_id = sxo_good_spec_base_obj.id
        except:
            self.log.exception("[SxoGoodsSpecBaseDao.add]")

        return spec_base_id

    @mysql_conn_session
    def get_by_good_id_coding(self, goods_id, coding):
        """通过goods_id和编码获取"""

        rows = self.conn.query(SxoGoodsSpecBaseModel.id).filter_by(goods_id=goods_id, coding=coding).first()
        return rows

    @mysql_conn_session
    def update(self, spec_id, data: SxoGoodsSpecBaseModel):
        """更新"""

        data_dict = data.to_dict()
        if data.weight is None:
            data_dict.pop("weight", "404")

        if data.extends is None:
            data_dict.pop("extends", "404")

        if data.barcode is None:
            data_dict.pop("barcode", "404")

        data_dict.pop("id", "404")
        data_dict.pop("add_time", "404")

        rows = self.conn.query(SxoGoodsSpecBaseModel).filter(SxoGoodsSpecBaseModel.id == spec_id).update(data_dict, synchronize_session="fetch")
        return rows
