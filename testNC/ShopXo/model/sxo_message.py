# CREATE TABLE `sxo_message` (
#   `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
#   `user_id` int unsigned NOT NULL DEFAULT '0' COMMENT '用户id',
#   `title` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '标题',
#   `detail` char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '详情',
#   `business_id` int unsigned NOT NULL DEFAULT '0' COMMENT '业务id',
#   `business_type` char(180) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '业务类型，字符串（如：订单、充值、提现、等...）',
#   `type` tinyint unsigned NOT NULL DEFAULT '0' COMMENT '消息类型（0普通通知, ...）',
#   `is_read` tinyint unsigned NOT NULL DEFAULT '1' COMMENT '是否已读（0否, 1是）',
#   `is_delete_time` int unsigned NOT NULL DEFAULT '0' COMMENT '是否已删除（0否, 大于0删除时间）',
#   `user_is_delete_time` int unsigned NOT NULL DEFAULT '0' COMMENT '用户是否已删除（0否, 大于0删除时间）',
#   `add_time` int unsigned NOT NULL DEFAULT '0' COMMENT '添加时间',
#   PRIMARY KEY (`id`) USING BTREE,
#   KEY `user_id` (`user_id`) USING BTREE
# ) ENGINE=InnoDB AUTO_INCREMENT=1074 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='消息';


from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.dialects.mysql.base import INTEGER, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# // 是否已读
# 'common_is_read_list' = > [
#     0 = > ['id' = > 0, 'name' = > '未读', 'checked' = > true],
# 1 = > ['id' = > 1, 'name' = > '已读'],
# ],
#
# // 消息类型
# 'common_message_type_list' = > [
#     0 = > ['id' = > 0, 'name' = > '默认', 'checked' = > true],
# ],

class SxoMessageModel(Base):
    __tablename__ = 'sxo_message'
    id = Column(INTEGER, nullable=False, autoincrement=True, comment="自增id")
    user_id = Column(INTEGER, nullable=False, default=0, server_default=text("'0'"), comment="用户id")
    title = Column(CHAR(60), nullable=False, default="", server_default=text("''"), comment="标题")
    detail = Column(CHAR(255), nullable=False, default="", server_default=text("''"), comment="详情")
    business_id = Column(INTEGER, nullable=False, default=0, server_default=text("'0'"), comment="业务id")
    business_type = Column(CHAR(180), nullable=False, default=0, server_default=text("'0'"), comment="业务类型，字符串（如：订单、充值、提现、等...）")
    type = Column(TINYINT, nullable=False, default=0, server_default=text("'0'"), comment="消息类型（0普通通知, ...）")
    is_read = Column(TINYINT, nullable=False, default=0, server_default=text("'0'"), comment="是否已读（0否, 1是）")
    is_delete_time = Column(INTEGER, nullable=False, default=0, server_default=text("'0'"), comment="是否已删除（0否, 大于0删除时间）")
    user_is_delete_time = Column(INTEGER, nullable=False, default=0, server_default=text("'0'"), comment="用户是否已删除（0否, 大于0删除时间）")
    add_time = Column(INTEGER, nullable=False, default=0, server_default=text("'0'"), comment="添加时间")
