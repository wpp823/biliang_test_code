from sqlalchemy import Column, UniqueConstraint
from sqlalchemy.dialects.mysql.base import INTEGER, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.ddl import CreateTable

Base = declarative_base()


class TestModel(Base):
    """商品规格基础"""
    __tablename__ = 'test_table'
    __table_args__ = (UniqueConstraint('warehouse_id', 'goods_id', name='warehouse_id_goods_id'),)
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, comment="自增id")  # 自增id
    warehouse_id = Column(INTEGER, nullable=False, default=0, comment='仓库id')
    goods_id = Column(INTEGER, nullable=False, default=0, comment='商品id')
    md5_key = Column(CHAR(32), nullable=False, default=1, comment='md5key值')
    # index = UniqueConstraint('warehouse_id', 'goods_id')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

print(CreateTable(TestModel.__table__))


