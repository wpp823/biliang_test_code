import arrow

from base.base import mysql_conn_session
from model.sxo_warehouse_goods_spec import SxoWarehouseGoodsSpecModel


class SxoWarehouseGoodsSpecDao():
    def __init__(self, log):
        self.log = log

    @mysql_conn_session
    def add(self, data: SxoWarehouseGoodsSpecModel):
        """

        """

        data.add_time = arrow.now(tz="+08:00").timestamp

        warehouse_goods_spec_id = None

        try:
            self.conn.add(data)
            self.conn.commit()
            warehouse_goods_spec_id = data.id
        except:
            self.log.exception("[SxoWarehouseGoodsSpecDao.add]")

        return warehouse_goods_spec_id

    @mysql_conn_session
    def get_by_goods_warehouse_id(self, warehouse_id, goods_id, warehouse_goods_id):
        """通过goods_id和编码获取"""

        rows = self.conn.query(SxoWarehouseGoodsSpecModel).filter_by(goods_id=goods_id, warehouse_id=warehouse_id, warehouse_goods_id=warehouse_goods_id).first()
        return rows

    @mysql_conn_session
    def update(self, warehouse_goods_spec_id, data: SxoWarehouseGoodsSpecModel):
        """更新"""
        dict_data = data.to_dict()

        dict_data.pop("add_time", "404")  # SEO标题
        dict_data.pop("id", "404")
        rows = self.conn.query(SxoWarehouseGoodsSpecModel).filter(SxoWarehouseGoodsSpecModel.id == warehouse_goods_spec_id).update(dict_data, synchronize_session="fetch")
        return rows
