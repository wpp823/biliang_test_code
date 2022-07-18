# coding: utf-8
from sqlalchemy import Column, DECIMAL, text
from sqlalchemy.dialects.mysql import CHAR, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SxoOrderAddressModel(Base):
    __tablename__ = 'sxo_order_address'
    __table_args__ = {'comment': '订单地址'}

    id = Column(INTEGER, primary_key=True, comment='自增id')
    order_id = Column(INTEGER, nullable=False, index=True, server_default=text("'0'"), comment='订单id')
    user_id = Column(INTEGER, nullable=False, index=True, server_default=text("'0'"), comment='用户id')
    address_id = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='收件地址id')
    alias = Column(CHAR(60), nullable=False, server_default=text("''"), comment='别名')
    name = Column(CHAR(60), nullable=False, server_default=text("''"), comment='收件人-姓名')
    tel = Column(CHAR(15), nullable=False, server_default=text("''"), comment='收件人-电话')
    province = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='收件人-省')
    city = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='收件人-市')
    county = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='收件人-县/区')
    address = Column(CHAR(200), nullable=False, server_default=text("''"), comment='收件人-详细地址')
    province_name = Column(CHAR(30), nullable=False, server_default=text("''"), comment='收件人-省-名称')
    city_name = Column(CHAR(30), nullable=False, server_default=text("''"), comment='收件人-市-名称')
    county_name = Column(CHAR(30), nullable=False, server_default=text("''"), comment='收件人-县/区-名称')
    lng = Column(DECIMAL(13, 10), nullable=False, server_default=text("'0.0000000000'"), comment='收货地址-经度')
    lat = Column(DECIMAL(13, 10), nullable=False, server_default=text("'0.0000000000'"), comment='收货地址-纬度')
    idcard_name = Column(CHAR(60), nullable=False, server_default=text("''"), comment='身份证姓名')
    idcard_number = Column(CHAR(30), nullable=False, server_default=text("''"), comment='身份证号码')
    idcard_front = Column(CHAR(255), nullable=False, server_default=text("''"), comment='身份证人像面图片')
    idcard_back = Column(CHAR(255), nullable=False, server_default=text("''"), comment='身份证国微面图片')
    add_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='添加时间')
    upd_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='更新时间')
