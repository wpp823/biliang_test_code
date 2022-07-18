from sqlalchemy import Column
from sqlalchemy.dialects.mysql.base import INTEGER, CHAR, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SxoUserModel(Base):
    """用户信息"""
    __tablename__ = 'sxo_user'

    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True, comment="自增id")  # 自增id
    system_type = Column(CHAR(60), nullable=False, default='default', server_default="default", comment="系统类型（默认 default, 其他按照SYSTEM_TYPE常量类型）")
    alipay_openid = Column(CHAR(60), nullable=False, default='', server_default='', comment="支付宝openid")
    weixin_openid = Column(CHAR(60), nullable=False, default='', server_default='', comment="微信openid")
    weixin_unionid = Column(CHAR(60), nullable=False, default='', server_default='', comment="微信unionid")
    weixin_web_openid = Column(CHAR(60), nullable=False, default='', server_default='', comment="微信web用户openid")
    baidu_openid = Column(CHAR(60), nullable=False, default='', server_default='', comment="百度openid")
    toutiao_openid = Column(CHAR(60), nullable=False, default='', server_default='', comment="百度openid")
    qq_openid = Column(CHAR(60), nullable=False, default='', server_default='', comment="QQopenid")
    qq_unionid = Column(CHAR(60), nullable=False, default='', server_default='', comment="QQunionid")
    status = Column(TINYINT, nullable=False, default=0, server_default='0', comment="状态（0正常, 1禁止发言, 2禁止登录）")
    salt = Column(CHAR(32), nullable=False, default='', server_default='', comment="配合密码加密串")
    pwd = Column(CHAR(32), nullable=False, default='', server_default='', comment="登录密码")
    token = Column(CHAR(60), nullable=False, default='', server_default='', comment="token")
    username = Column(CHAR(60), nullable=False, default='', server_default='', comment="用户名")
    nickname = Column(CHAR(60), nullable=False, default='', server_default='', comment="用户昵称")
    mobile = Column(CHAR(11), nullable=False, default='', server_default='', comment="手机号码")
    email = Column(CHAR(60), nullable=False, default='', server_default='', comment="电子邮箱（最大长度60个字符）")
    gender = Column(TINYINT, nullable=False, default=0, server_default='0', comment="性别（0保密，1女，2男）")
    avatar = Column(CHAR(255), nullable=False, default='', server_default='', comment="用户头像地址")
    province = Column(CHAR(60), nullable=False, default='', server_default='', comment="所在省")
    city = Column(CHAR(60), nullable=False, default='', server_default='', comment="所在市")
    birthday = Column(INTEGER, nullable=False, default=0, server_default='0', comment="生日")
    address = Column(CHAR(150), nullable=False, default='', server_default='', comment="详细地址")
    integral = Column(INTEGER, nullable=False, default=0, server_default='0', comment="有效积分")
    locking_integral = Column(INTEGER, nullable=False, default=0, server_default='0', comment="锁定积分")
    referrer = Column(INTEGER, nullable=False, default=0, server_default='0', comment="推荐人用户id")
    plugins_distribution_level = Column(INTEGER, nullable=False, default=0, comment="分销等级")
    is_delete_time = Column(INTEGER, nullable=False, default=0, server_default='0', comment="是否已删除（0否, 大于0删除时间")

    upd_time = Column(INTEGER, nullable=False, default=0, server_default='0', comment="更新时间")  # int unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',\n" \
    add_time = Column(INTEGER, nullable=False, default=0, server_default='0', comment="添加时间")  # 时间戳

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# CREATE TABLE `sxo_user` (
#   `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
#   `system_type` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'default' COMMENT '系统类型（默认 default, 其他按照SYSTEM_TYPE常量类型）',
#   `alipay_openid` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '支付宝openid',
#   `weixin_openid` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '微信openid',
#   `weixin_unionid` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '微信unionid',
#   `weixin_web_openid` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '微信web用户openid',
#   `baidu_openid` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '百度openid',
#   `toutiao_openid` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '百度openid',
#   `qq_openid` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'QQopenid',
#   `qq_unionid` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'QQunionid',
#   `status` tinyint unsigned NOT NULL DEFAULT '0' COMMENT '状态（0正常, 1禁止发言, 2禁止登录）',
#   `salt` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '配合密码加密串',
#   `pwd` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '登录密码',
#   `token` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT 'token',
#   `username` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '用户名',
#   `nickname` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '用户昵称',
#   `mobile` char(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '手机号码',
#   `email` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '电子邮箱（最大长度60个字符）',
#   `gender` tinyint unsigned NOT NULL DEFAULT '0' COMMENT '性别（0保密，1女，2男）',
#   `avatar` char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '用户头像地址',
#   `province` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '所在省',
#   `city` char(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '所在市',
#   `birthday` int NOT NULL DEFAULT '0' COMMENT '生日',
#   `address` char(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '详细地址',
#   `integral` int NOT NULL DEFAULT '0' COMMENT '有效积分',
#   `locking_integral` int NOT NULL DEFAULT '0' COMMENT '锁定积分',
#   `referrer` int unsigned NOT NULL DEFAULT '0' COMMENT '推荐人用户id',
#   `plugins_distribution_level` int unsigned NOT NULL DEFAULT '0' COMMENT '分销等级',
#   `is_delete_time` int unsigned NOT NULL DEFAULT '0' COMMENT '是否已删除（0否, 大于0删除时间）',
#   `add_time` int unsigned NOT NULL DEFAULT '0' COMMENT '添加时间',
#   `upd_time` int unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',
#   PRIMARY KEY (`id`) USING BTREE,
#   KEY `alipay_openid` (`alipay_openid`) USING BTREE,
#   KEY `weixin_openid` (`weixin_openid`) USING BTREE,
#   KEY `mobile` (`mobile`) USING BTREE,
#   KEY `username` (`username`) USING BTREE,
#   KEY `token` (`token`) USING BTREE,
#   KEY `baidu_openid` (`baidu_openid`) USING BTREE,
#   KEY `system_type` (`system_type`) USING BTREE,
#   KEY `status` (`status`) USING BTREE,
#   KEY `weixin_unionid` (`weixin_unionid`) USING BTREE,
#   KEY `weixin_web_openid` (`weixin_web_openid`) USING BTREE,
#   KEY `is_delete_time` (`is_delete_time`) USING BTREE
# ) ENGINE=InnoDB AUTO_INCREMENT=409 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户';
