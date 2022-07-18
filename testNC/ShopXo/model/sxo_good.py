from sqlalchemy import Column
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.dialects.mysql.base import INTEGER, VARCHAR, CHAR, DECIMAL, SMALLINT, MEDIUMTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SxoGoodModel(Base):
    __tablename__ = 'sxo_goods'

    id = Column(INTEGER(unsigned=True), primary_key=True,autoincrement=True, comment="自增id")  # 自增id
    brand_id = Column(INTEGER, default=0, comment="品牌id")  # 品牌id
    site_type = Column(SMALLINT, nullable=False, default=-1, comment="商品类型")  # 商品类型（跟随站点类型一致[0销售, 1展示, 2自提, 3虚拟销售, 4销售+自提]）
    title = Column(VARCHAR(160), nullable=False, default='')  # 标题
    title_color = Column(VARCHAR(7), nullable=False, default='')  # 标题颜色
    simple_desc = Column(VARCHAR(230), nullable=False, default='')  # 简述
    model = Column(VARCHAR(30), nullable=False, default='', comment="型号")  # 型号
    place_origin = Column(INTEGER, nullable=False, default=0, comment="产地（地区省id）")  # 产地（地区省id）
    inventory = Column(INTEGER, nullable=False, default=0, comment="库存（所有规格库存总和）")  # 库存（所有规格库存总和）
    inventory_unit = Column(VARCHAR(15), nullable=False, default="", comment="库存单位")  # 库存单位
    images = Column(VARCHAR(255), nullable=False, default="", comment="封面图片")  # 封面图片
    original_price = Column(VARCHAR(60), nullable=False, default="", comment="原价（单值:10, 区间:10.00-20.00）一般用于展示使用")  # 原价（单值:10, 区间:10.00-20.00）一般用于展示使用
    min_original_price = Column(DECIMAL(10, 2), nullable=False, default=0.00, comment="最低原价")  # 最低原价
    max_original_price = Column(DECIMAL(10, 2), nullable=False, default=0.00, comment="最大原价")  # 最大原价
    price = Column(VARCHAR(60), nullable=False, default="", comment="售价格（单值:10, 区间:10.00-20.00）一般用于展示使用")  # 售价格（单值:10, 区间:10.00-20.00）一般用于展示使用
    min_price = Column(DECIMAL(10, 2), nullable=False, default=0.00, comment="最低价格")  # 最低价格
    max_price = Column(DECIMAL(10, 2), nullable=False, default=0.00, comment="最高价格")  # 最高价格
    give_integral = Column(INTEGER, nullable=False, default=0, comment="购买赠送积分比例")  # 购买赠送积分比例
    buy_min_number = Column(INTEGER, nullable=False, default=1, comment="最低起购数量")  # 购买赠送积分比例
    buy_max_number = Column(INTEGER, nullable=False, default=0, comment="最大购买数量")  # 最大购买数量（最大数值 100000000, 小于等于0或空则不限）
    is_deduction_inventory = Column(SMALLINT, nullable=False, default=1, comment="是否扣减库存")  # 是否扣减库存（0否, 1是）
    is_shelves = Column(SMALLINT, nullable=False, default=1, comment="是否上架")  # 是否上架（下架后用户不可见, 0否, 1是））
    content_web = Column(MEDIUMTEXT, comment="电脑端详情内容")  # 电脑端详情内容
    photo_count = Column(SMALLINT, nullable=False, default=0, comment="相册图片数量")  # 相册图片数量
    sales_count = Column(INTEGER, nullable=False, default=0, comment="销量")  # 销量
    access_count = Column(INTEGER, nullable=False, default=0, comment="访问次数")  # 访问次数
    video = Column(CHAR(255), nullable=False, default='', comment="短视频")  # 短视频
    is_exist_many_spec = Column(SMALLINT(unsigned=True), nullable=False, default=0, comment="是否存在多个规格（0否, 1是")  # 是否存在多个规格（0否, 1是
    spec_base = Column(TEXT, nullable=False, default='', comment="规格基础数据")  # 规格基础数据
    fictitious_goods_value = Column(TEXT, comment="虚拟商品展示数据")  # 虚拟商品展示数据
    seo_title = Column(CHAR(100), nullable=False, default='', comment="SEO标题")  # SEO标题
    seo_keywords = Column(CHAR(130), nullable=False, default='', comment="SEO关键字")  # SEO关键字
    seo_desc = Column(CHAR(230), nullable=False, default='', comment="SEO描述")  # SEO描述
    is_delete_time = Column(INTEGER, nullable=False, default=0, comment="是否已删除（0 未删除, 大于0则是删除时间）")  # 是否已删除（0 未删除, 大于0则是删除时间）
    add_time = Column(INTEGER, nullable=False, default=0, comment="添加时间")  # 添加时间 秒级时间戳
    upd_time = Column(INTEGER, nullable=False, default=0, comment="更新时间")  # 更新时间 秒级时间戳

    # 查询单条数据
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # # 第二种方法
    # def to_dict(self):
    #     model_dict = dict(self.__dict__)
    #     del model_dict['_sa_instance_state']
    #     return model_dict
