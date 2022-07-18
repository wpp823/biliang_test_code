# coding: utf-8
from sqlalchemy import Column, DECIMAL, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SxoOrderDetailModel(Base):
    __tablename__ = 'sxo_order_detail'
    __table_args__ = {'comment': '订单详情'}

    id = Column(INTEGER, primary_key=True, comment='自增id')
    user_id = Column(INTEGER, nullable=False, index=True, server_default=text("'0'"), comment='用户id')
    order_id = Column(INTEGER, nullable=False, index=True, server_default=text("'0'"), comment='订单id')
    goods_id = Column(INTEGER, nullable=False, index=True, server_default=text("'0'"), comment='商品id')
    title = Column(CHAR(160), nullable=False, server_default=text("''"), comment='标题')
    images = Column(CHAR(255), nullable=False, server_default=text("''"), comment='封面图片')
    original_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='原价')
    price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='价格')
    total_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='当前总价(单价*数量)')
    spec = Column(TEXT, comment='规格')
    buy_number = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='购买数量')
    model = Column(CHAR(30), nullable=False, server_default=text("''"), comment='型号')
    spec_weight = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='重量（kg）')
    spec_coding = Column(CHAR(80), nullable=False, server_default=text("''"), comment='编码')
    spec_barcode = Column(CHAR(80), nullable=False, server_default=text("''"), comment='条形码')
    refund_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='退款金额')
    returned_quantity = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='退货数量')
    add_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='添加时间')
    upd_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='更新时间')
