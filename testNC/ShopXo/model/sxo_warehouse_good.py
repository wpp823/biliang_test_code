from sqlalchemy import Column
from sqlalchemy.dialects.mysql.base import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SxoWarehouseGoodsModel(Base):
    """商品规格基础"""
    __tablename__ = 'sxo_warehouse_goods'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, comment="自增id")  # 自增id
    warehouse_id = Column(INTEGER, nullable=False, default=0, comment='仓库id')
    goods_id = Column(INTEGER, nullable=False, default=0, comment='商品id')
    is_enable = Column(TINYINT, nullable=False, default=1, comment='是否启用（0否，1是）')
    inventory = Column(INTEGER, nullable=False, default=0, comment='总库存')
    add_time = Column(INTEGER, nullable=False, default=0, comment="添加时间")  # 添加时间 秒级时间戳
    upd_time = Column(INTEGER, nullable=False, default=0, comment="更新时间")  # 更新时间 秒级时间戳

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}