# CREATE TABLE = Column()#sxo_goods_category= Column()# (
#   = Column()#id= Column()# int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
#   = Column()#pid= Column()# int unsigned NOT NULL DEFAULT '0' COMMENT '父id',
#   = Column()#icon= Column()# char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'icon图标',
#   = Column()#name= Column()# char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '名称',
#   = Column()#vice_name= Column()# char(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '副标题',
#   = Column()#describe= Column()# char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '描述',
#   = Column()#bg_color= Column()# char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'css背景色值',
#   = Column()#big_images= Column()# char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '大图片',
#   = Column()#is_home_recommended= Column()# tinyint unsigned NOT NULL DEFAULT '0' COMMENT '是否首页推荐（0否, 1是）',
#   = Column()#sort= Column()# tinyint unsigned NOT NULL DEFAULT '0' COMMENT '排序',
#   = Column()#is_enable= Column()# tinyint unsigned NOT NULL DEFAULT '1' COMMENT '是否启用（0否，1是）',
#   = Column()#seo_title= Column()# char(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'SEO标题',
#   = Column()#seo_keywords= Column()# char(130) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'SEO关键字',
#   = Column()#seo_desc= Column()# char(230) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'SEO描述',
#   = Column()#add_time= Column()# int unsigned NOT NULL DEFAULT '0' COMMENT '添加时间',
#   = Column()#upd_time= Column()# int unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',
#   PRIMARY KEY (= Column()#id= Column()#) USING BTREE,
#   KEY = Column()#pid= Column()# (= Column()#pid= Column()#) USING BTREE,
#   KEY = Column()#is_enable= Column()# (= Column()#is_enable= Column()#) USING BTREE,
#   KEY = Column()#sort= Column()# (= Column()#sort= Column()#) USING BTREE
# ) ENGINE=InnoDB AUTO_INCREMENT=893 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='商品分类';


from sqlalchemy import Column, CHAR
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql.base import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SxoGoodsCategoryModel(Base):
    # __tablename__ = 'sxo_goods_category_220704' # 测试表
    __tablename__ = 'sxo_goods_category'# 正式表

    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, comment="自增id")

    pid = Column(INTEGER, default=0, nullable=False, comment="父id")
    icon = Column(CHAR(255), default="", nullable=False, comment="icon图标")
    name = Column(CHAR(60), default="", nullable=False, comment="名称")
    vice_name = Column(CHAR(80), default="", nullable=False, comment="副标题")
    describe = Column(CHAR(255), default="", nullable=False, comment="描述")
    bg_color = Column(CHAR(30), default="", nullable=False, comment="css背景色值")
    big_images = Column(CHAR(255), default="", nullable=False, comment="大图片")
    is_home_recommended = Column(TINYINT, default=0, nullable=False, comment="是否首页推荐（0否, 1是）")
    sort = Column(TINYINT, default=0, nullable=False, comment="排序")
    is_enable = Column(TINYINT, default=1, nullable=False, comment="是否启用（0否，1是）")
    seo_title = Column(CHAR(100), default="", nullable=False, comment="SEO标题")
    seo_keywords = Column(CHAR(130), default="", nullable=False, comment="SEO关键字")
    seo_desc = Column(CHAR(230), default="", nullable=False, comment="SEO描述")
    add_time = Column(INTEGER(unsigned=True), default=0, nullable=False, comment="添加时间")
    upd_time = Column(INTEGER(unsigned=True), default=0, nullable=False, comment="更新时间")

    # 查询单条数据
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
