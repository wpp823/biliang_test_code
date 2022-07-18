import arrow

from base.base import mysql_conn_session
from model.sxo_warehouse_good import SxoWarehouseGoodsModel


class SxoWarehouseGoodsDao():
    def __init__(self, log):
        self.log = log

    @mysql_conn_session
    def add(self, data: SxoWarehouseGoodsModel):
        """

        """
        now_at = arrow.now(tz="+08:00").timestamp

        data.add_time = now_at
        data.upd_time = now_at

        warehouse_goods_id = None

        try:
            self.conn.add(data)
            self.conn.commit()
            warehouse_goods_id = data.id
        except:
            self.log.exception("[SxoWarehouseGoodsDao.add]")

        return warehouse_goods_id

    @mysql_conn_session
    def get_by_goods_warehouse_id(self, warehouse_id, goods_id):
        """通过goods_id和编码获取"""

        rows = self.conn.query(SxoWarehouseGoodsModel).filter_by(goods_id=goods_id, warehouse_id=warehouse_id).first()
        return rows

    @mysql_conn_session
    def update(self, warehouse_goods_id, data: SxoWarehouseGoodsModel):
        """更新"""
        dict_data = data.to_dict()

        dict_data.pop("add_time", "404")  # SEO标题
        dict_data.pop("id", "404")
        dict_data['upd_time'] = arrow.now(tz="+08:00").timestamp

        rows = self.conn.query(SxoWarehouseGoodsModel).filter(SxoWarehouseGoodsModel.id == warehouse_goods_id).update(dict_data, synchronize_session="fetch")
        return rows
