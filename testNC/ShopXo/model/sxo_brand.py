from sqlalchemy import Column
from sqlalchemy.dialects.mysql.base import INTEGER, CHAR, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SxoBrandModel(Base):
    """品牌表"""
    __tablename__ = 'sxo_brand'
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, comment="自增id")  # 自增id
    logo = Column(CHAR(255), nullable=False, default="", comment="logo图标")
    name = Column(CHAR(30), nullable=False, default="", comment="名称")
    describe = Column(CHAR(255), nullable=False, default="", comment="描述")
    website_url = Column(CHAR(255), nullable=False, default="", comment="官网地址")
    is_enable = Column(TINYINT, nullable=False, default=1, comment="是否启用（0否，1是）")
    sort = Column(TINYINT, nullable=False, default=0, comment="顺序")
    seo_title = Column(CHAR(255), nullable=False, default="", comment="SEO标题")
    seo_keywords = Column(CHAR(130), nullable=False, default="", comment="SEO关键字")
    seo_desc = Column(CHAR(230), nullable=False, default="", comment="SEO描述")
    add_time = Column(INTEGER, nullable=False, default=0, comment="添加时间")  # 添加时间 秒级时间戳
    upd_time = Column(INTEGER, nullable=False, default=0, comment="更新时间")  # 更新时间 秒级时间戳

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
