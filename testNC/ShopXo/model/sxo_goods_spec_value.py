

from sqlalchemy import Column
from sqlalchemy.dialects.mysql.base import INTEGER, CHAR, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SxoGoodsSpecValueModel(Base):
    """商品规格值"""
    __tablename__ = 'sxo_goods_spec_value'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True,comment="自增id")  # 自增id
    goods_id = Column(INTEGER, nullable=False, default=0, comment="商品id")
    goods_spec_base_id = Column(INTEGER, nullable=False, default=0, comment="商品规格基础id")
    value = Column(CHAR(230), nullable=False, default='', comment="规格值")
    add_time = Column(INTEGER, nullable=False, default=0, comment="添加时间")  # 时间戳


    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}