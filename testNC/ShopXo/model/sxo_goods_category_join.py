# CREATE TABLE `sxo_goods_category_join` (
#   `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
#   `goods_id` int unsigned NOT NULL DEFAULT '0' COMMENT '商品id',
#   `category_id` int unsigned NOT NULL DEFAULT '0' COMMENT '分类id',
#   `add_time` int unsigned DEFAULT '0' COMMENT '添加时间',
#   PRIMARY KEY (`id`) USING BTREE,
#   KEY `goods_id` (`goods_id`) USING BTREE,
#   KEY `category_id` (`category_id`) USING BTREE
# ) ENGINE=InnoDB AUTO_INCREMENT=1193 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='商品分类关联';


from sqlalchemy import Column, CHAR
from sqlalchemy.dialects.mysql.base import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SxoGoodsCategoryJoinModel(Base):
    # __tablename__ = 'sxo_goods_category_join_220704' # 测试表
    __tablename__ = 'sxo_goods_category_join'

    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, comment="自增id")

    goods_id = Column(INTEGER, default=0, server_default='0', nullable=False, comment="商品id")
    category_id = Column(CHAR(255), default="",server_default='', nullable=False, comment="分类id")
    add_time = Column(INTEGER, default=0,server_default='0',  nullable=False, comment="添加时间")

    # 查询单条数据
    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
