from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.mysql.base import INTEGER, CHAR, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SxoWarehouseGoodsSpecModel(Base):
    """商品规格基础"""
    __tablename__ = 'test_table'

    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, comment="自增id")  # 自增id
    warehouse_goods_id = Column(INTEGER, nullable=False, default=0, comment='仓库商品id')
    warehouse_id = Column(INTEGER, nullable=False, default=0, comment='仓库id')
    goods_id = Column(INTEGER, nullable=False, default=0, comment='商品id')
    md5_key = Column(CHAR(32), nullable=False, default=1, comment='md5key值')
    spec = Column(TEXT, nullable=False, default=0, comment='规格值')
    inventory = Column(INTEGER, nullable=False, default=0, comment='库存')
    add_time = Column(INTEGER, nullable=False, default=0, comment="添加时间")  # 添加时间 秒级时间戳

    UniqueConstraint('warehouse_id', 'warehouse_id', name='test')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


