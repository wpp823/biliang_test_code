import arrow

from base.base import mysql_conn_session
from model.sxo_goods_category import SxoGoodsCategoryModel


class SxoGoodsCategorysDao():
    def __init__(self, log):
        self.log = log

    @mysql_conn_session
    def add(self, data: SxoGoodsCategoryModel):
        """添加"""
        now_at = arrow.now().timestamp
        data.add_time = now_at
        data.upd_time = now_at
        # 选填字段
        if data.seo_title is None:
            data.seo_title = ''  # SEO标题
        if data.seo_keywords is None:
            data.seo_keywords = ""  # SEO关键字
        if data.seo_desc is None:
            data.seo_desc = ''  # SEO描述
        if data.vice_name is None:
            data.vice_name = ''  # 副标题
        if data.describe is None:
            data.describe = ''  # 描述
        if data.bg_color is None:
            data.bg_color = ''  # css背景色值
        if data.big_images is None:
            data.big_images = ''  # 大图片
        goods_category_id = None
        try:
            self.conn.add(data)  # 添加到session
            self.conn.commit()  # 提交到数据库
            goods_category_id = data.id
        except:
            self.log.exception("[SxoGoodsCategorysDao.add]")

        return goods_category_id

    @mysql_conn_session
    def get_by_name(self, sxo_goods_categorys_name):
        """获取"""
        data = self.conn.query(SxoGoodsCategoryModel).filter_by(name=sxo_goods_categorys_name).first()

        return data

    @mysql_conn_session
    def update(self, sxo_goods_categorys_id, data: SxoGoodsCategoryModel):
        """

        :param sxo_goods_categorys_id:
        :param data:
        :return:
        """

        # 选填字段
        if data.seo_title is None:
            data.seo_title = ''  # SEO标题
        if data.seo_keywords is None:
            data.seo_keywords = ""  # SEO关键字
        if data.seo_desc is None:
            data.seo_desc = ''  # SEO描述
        if data.vice_name is None:
            data.vice_name = ''  # 副标题
        if data.describe is None:
            data.describe = ''  # 描述
        if data.bg_color is None:
            data.bg_color = ''  # css背景色值
        if data.big_images is None:
            data.big_images = ''  # 大图片

        data_dict = data.to_dict()
        res = self.conn.query(SxoGoodsCategoryModel).filter(SxoGoodsCategoryModel.id == sxo_goods_categorys_id).update(data_dict, synchronize_session="fetch")
        return res
