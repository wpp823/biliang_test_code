# coding: utf-8
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, TEXT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# // 订单售后状态
# 'common_order_aftersale_status_list' = > [
#     0 = > ['value' = > 0, 'name' = > '待确认'],
# 1 = > ['value' = > 1, 'name' = > '待退货'],
# 2 = > ['value' = > 2, 'name' = > '待审核'],
# 3 = > ['value' = > 3, 'name' = > '已完成'],
# 4 = > ['value' = > 4, 'name' = > '已拒绝'],
# 5 = > ['value' = > 5, 'name' = > '已取消'],
# ],

class SxoOrderAftersaleModel(Base):
    __tablename__ = 'sxo_order_aftersale'
    __table_args__ = {'comment': '订单售后'}

    id = Column(INTEGER, primary_key=True, comment='自增id')
    order_no = Column(CHAR(60), nullable=False, server_default=text("''"), comment='订单号')
    order_detail_id = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='订单详情id')
    order_id = Column(INTEGER, nullable=False, index=True, server_default=text("'0'"), comment='订单id')
    goods_id = Column(INTEGER, nullable=False, index=True, server_default=text("'0'"), comment='商品id')
    user_id = Column(INTEGER, nullable=False, index=True, server_default=text("'0'"), comment='用户id')
    status = Column(TINYINT, nullable=False, index=True, server_default=text("'0'"), comment='状态（0待确认, 1待退货, 2待审核, 3已完成, 4已拒绝, 5已取消）')
    type = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='业务类型（0仅退款, 1退货退款）')
    refundment = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='退款类型（0原路退回, 1退至钱包, 2手动处理）')
    reason = Column(CHAR(180), nullable=False, server_default=text("''"), comment='申请原因')
    number = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='退货数量')
    price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='退款金额')
    msg = Column(TEXT, comment='退款说明')
    images = Column(TEXT, comment='凭证图片（一维数组json存储）')
    refuse_reason = Column(CHAR(230), nullable=False, server_default=text("''"), comment='拒绝原因')
    express_name = Column(CHAR(60), nullable=False, server_default=text("''"), comment='快递名称')
    express_number = Column(CHAR(60), nullable=False, server_default=text("''"), comment='快递单号')
    apply_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='申请时间')
    confirm_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='确认时间')
    delivery_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='退货时间')
    audit_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='审核时间')
    cancel_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='取消时间')
    add_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='添加时间')
    upd_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='更新时间')
