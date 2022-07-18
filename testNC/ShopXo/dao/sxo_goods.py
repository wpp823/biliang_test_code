import arrow

from model.sxo_good import SxoGoodModel
from base.base import mysql_conn_session

class SxoGoodDao():
    def __init__(self, log):
        self.log = log

    @mysql_conn_session
    def add(self, brand_id, site_type, title, simple_desc, model, inventory, inventory_unit, images, original_price, min_original_price,
            max_original_price, price, min_price, max_price, give_integral, buy_min_number, buy_max_number, is_deduction_inventory, is_shelves, content_web, photo_count,
            sales_count, access_count, is_exist_many_spec, fictitious_goods_value: str = None, title_color: str = None, spec_base: str = None,
            seo_title: str = None, seo_keywords: str = None, seo_desc: str = None, video: str = None, place_origin: str = None, **kwargs):
        """
        添加商品

        :param conn:
        :param brand_id:
        :param site_type:
        :param title:
        :param title_color:
        :param simple_desc:
        :param model:
        :param place_origin:
        :param inventory:
        :param inventory_unit:
        :param images:
        :param original_price:
        :param min_original_price:
        :param max_original_price:
        :param price:
        :param min_price:
        :param max_price:
        :param give_integral:
        :param buy_min_number:
        :param buy_max_number:
        :param is_deduction_inventory:
        :param is_shelves:
        :param content_web:
        :param photo_count:
        :param sales_count:
        :param access_count:
        :param video:
        :param is_exist_many_spec:
        :param spec_base:
        :param fictitious_goods_value:
        :param seo_title:
        :param seo_keywords:
        :param seo_desc:
        :param is_delete_time:
        :param add_time:
        :param upd_time:
        :return:
        """
        now_at = arrow.now(tz="+08:00").timestamp
        sxo_good_obj = SxoGoodModel(
            brand_id=brand_id,
            site_type=site_type,
            title=title,
            title_color=title_color,
            simple_desc=simple_desc,
            model=model,
            inventory=inventory,
            inventory_unit=inventory_unit,
            images=images,
            original_price=original_price,
            min_original_price=min_original_price,
            max_original_price=max_original_price,
            price=price,
            min_price=min_price,
            max_price=max_price,
            give_integral=give_integral,
            buy_min_number=buy_min_number,
            buy_max_number=buy_max_number,
            is_deduction_inventory=is_deduction_inventory,
            is_shelves=is_shelves,
            content_web=content_web,
            photo_count=photo_count,
            sales_count=sales_count,
            access_count=access_count,
            is_exist_many_spec=is_exist_many_spec,
            # spec_base=spec_base,
            add_time=now_at,
            upd_time=now_at,
        )
        # 选填字段
        if seo_title is not None:
            sxo_good_obj.seo_title = seo_title  # SEO标题
        if seo_keywords is not None:
            sxo_good_obj.seo_keywords = seo_keywords  # SEO关键字
        if seo_desc is not None:
            sxo_good_obj.seo_desc = seo_desc  # SEO描述

        if video:
            sxo_good_obj.video = video  # 视频
        if place_origin is not None:
            sxo_good_obj.place_origin = place_origin  # 产地（地区省id）

        if place_origin is not None:
            sxo_good_obj.place_origin = place_origin  # 产地（地区省id）

        if spec_base is not None:
            sxo_good_obj.spec_base = spec_base  # 基础规格信息
        if fictitious_goods_value is not None:
            sxo_good_obj.fictitious_goods_value = fictitious_goods_value  # 虚拟商品展示数据
        good_id = None
        try:
            self.conn.add(sxo_good_obj)  # 添加到session
            self.conn.commit()  # 提交到数据库
            good_id = sxo_good_obj.id
        except:
            self.log.exception("[SxoGoodDao.add]")
        return good_id

    @mysql_conn_session
    def get_by_model(self, model):
        """通过型号获取商品"""
        rows = self.conn.query(SxoGoodModel).filter_by(model=model).first()

        return rows

    @mysql_conn_session
    def update(self, good_id, data: SxoGoodModel):
        """更新商品表"""

        # 选填字段
        dict_data = data.to_dict()
        if data.seo_title is None:
            dict_data.pop("seo_title", "404")  # SEO标题
        if data.seo_keywords is None:
            dict_data.pop("seo_keywords", "404")  # SEO关键字
        if data.seo_desc is None:
            dict_data.pop("seo_desc", "404")  # SEO描述
        if data.video is None:
            dict_data.pop("video", "404")  # 视频
        if data.place_origin is None:
            dict_data.pop("place_origin", "404")  # 产地（地区省id）
        if data.spec_base is None:
            dict_data.pop("spec_base", "404")  # 基础规格信息
        if data.fictitious_goods_value is None:
            dict_data.pop("fictitious_goods_value", "404")  # 虚拟商品展示数据
        if data.title_color is None:
            dict_data.pop("title_color", "404")  # 虚拟商品展示数据
        if data.inventory is None:
            dict_data.pop("inventory", "404")  # 库存

        if data.sales_count is None:
            dict_data.pop("sales_count", "404")  # 库存

        dict_data.pop("id", "404")
        dict_data.pop("add_time", "404")
        dict_data["upd_time"] = arrow.now().timestamp  # 更新时间 秒级时间戳
        res = self.conn.query(SxoGoodModel).filter(SxoGoodModel.id == good_id).update(dict_data, synchronize_session="fetch")
        self.conn.commit()
        return res

    @mysql_conn_session
    def delete(self, goods_id):
        res = self.conn.query(SxoGoodModel).filter(SxoGoodModel.id == goods_id).delete()
        self.conn.commit()

        return res
