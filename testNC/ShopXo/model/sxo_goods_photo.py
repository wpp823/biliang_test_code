from sqlalchemy import Column
from sqlalchemy.dialects.mysql.base import INTEGER, CHAR, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SxoGoodsPhotoModel(Base):
    """商品相册图片"""
    __tablename__ = 'sxo_goods_photo'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, comment="自增id")  # 自增id
    goods_id = Column(INTEGER, nullable=False, default=0, comment="商品id")
    images = Column(CHAR(255), nullable=False, default="", comment="图片")
    is_show = Column(TINYINT, nullable=False, default=1, comment="是否显示（0否, 1是）")
    sort = Column(TINYINT, nullable=False, default=0, comment="顺序")
    add_time = Column(INTEGER, nullable=False, default=0, comment="添加时间")  # 时间戳

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}