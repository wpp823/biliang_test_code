from sqlalchemy import Column
from sqlalchemy.dialects.mysql.base import INTEGER, CHAR, DECIMAL, LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SxoGoodsSpecBaseModel(Base):
    """商品规格基础"""
    __tablename__ = 'sxo_goods_spec_base'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True,comment="自增id")  # 自增id
    goods_id = Column(INTEGER, nullable=False, default=0, comment="商品id")
    price = Column(DECIMAL(10, 2), nullable=False, default=0.00, comment="销售价格")
    inventory = Column(INTEGER, nullable=False, default=0, comment="库存")
    weight = Column(DECIMAL(10, 2), nullable=False, default=0.00, comment="重量（kg）")
    coding = Column(CHAR(80), nullable=False, default='', comment="编码")
    barcode = Column(CHAR(80), nullable=False, default='', comment="条形码")
    original_price = Column(DECIMAL(10, 2), nullable=False, default=0.00, comment="原价")
    extends = Column(LONGTEXT, nullable=False, default="", comment="扩展数据(json格式存储)")
    add_time = Column(INTEGER, nullable=False, default=0, comment="添加时间")  # 时间戳

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}