import arrow

from base.base import mysql_conn_session
from model.sxo_goods_photo import SxoGoodsPhotoModel


class SxoGoodsPhotosDao():
    def __init__(self, log):
        self.log = log
        # self.session = sessionmaker(self._engine)()  # 构建session对象

    @mysql_conn_session
    def add(self, goods_id, images, is_show, sort):
        """添加"""
        sxo_goods_photo_obj = SxoGoodsPhotoModel(
            goods_id=goods_id,
            images=images,
            is_show=is_show,
            sort=sort,
            add_time=arrow.now(tz="+08:00").timestamp
        )
        goods_photo_id = None
        try:
            self.conn.add(sxo_goods_photo_obj)
            self.conn.commit()
            goods_photo_id = sxo_goods_photo_obj.id
        except:
            self.log.exception("[SxoGoodsPhotosDao.add]")

        return goods_photo_id

    @mysql_conn_session
    def get_by_goods_id(self, goods_id, sort):
        """通过goods_id和编码获取"""

        rows = self.conn.query(SxoGoodsPhotoModel).filter_by(goods_id=goods_id, sort=sort).first()
        return rows

    @mysql_conn_session
    def update(self, goods_photo_id, data: SxoGoodsPhotoModel):
        """更新"""
        dict_data = data.to_dict()

        dict_data.pop("add_time", "404")  # SEO标题
        dict_data.pop("id", "404")

        rows = self.conn.query(SxoGoodsPhotoModel).filter(SxoGoodsPhotoModel.id == goods_photo_id).update(dict_data, synchronize_session="fetch")
        return rows
