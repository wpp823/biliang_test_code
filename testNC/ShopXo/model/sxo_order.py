# coding: utf-8
from sqlalchemy import Column, DECIMAL, text
from sqlalchemy.dialects.mysql import CHAR, DECIMAL, INTEGER, LONGTEXT, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# // 订单状态
# 'common_order_status' = > [
#     0 = > ['id' = > 0, 'name' = > '待确认', 'checked' = > true],
# 1 = > ['id' = > 1, 'name' = > '待付款'],
# 2 = > ['id' = > 2, 'name' = > '待发货'],
# 3 = > ['id' = > 3, 'name' = > '待收货'],
# 4 = > ['id' = > 4, 'name' = > '已完成'],
# 5 = > ['id' = > 5, 'name' = > '已取消'],
# 6 = > ['id' = > 6, 'name' = > '已关闭'],
# ],

class SxoOrderModel(Base):
    __tablename__ = 'sxo_order'
    __table_args__ = {'comment': '订单'}

    id = Column(INTEGER, primary_key=True, comment='自增id')
    order_no = Column(CHAR(60), nullable=False, unique=True, server_default=text("''"), comment='订单号')
    user_id = Column(INTEGER, nullable=False, index=True, server_default=text("'0'"), comment='用户id')
    warehouse_id = Column(INTEGER, nullable=False, index=True, server_default=text("'0'"), comment='仓库id')
    user_note = Column(CHAR(255), nullable=False, server_default=text("''"), comment='用户备注')
    express_id = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='快递id')
    express_number = Column(CHAR(60), nullable=False, server_default=text("''"), comment='快递单号')
    payment_id = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='支付方式id')
    status = Column(TINYINT, nullable=False, index=True, server_default=text("'0'"), comment='订单状态（0待确认, 1已确认/待支付, 2已支付/待发货, 3已发货/待收货, 4已完成, 5已取消, 6已关闭）')
    pay_status = Column(TINYINT, nullable=False, index=True, server_default=text("'0'"), comment='支付状态（0未支付, 1已支付, 2已退款, 3部分退款）')
    extension_data = Column(LONGTEXT, comment='扩展展示数据')
    buy_number_count = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='购买商品总数量')
    increase_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='增加的金额')
    preferential_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='优惠金额')
    price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='订单单价')
    total_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='订单总价(订单最终价格)')
    pay_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='已支付金额')
    refund_price = Column(DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"), comment='退款金额')
    returned_quantity = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='退货数量')
    client_type = Column(CHAR(30), nullable=False, server_default=text("''"), comment='客户端类型（pc, h5, ios, android, alipay, weixin, baidu）取APPLICATION_CLIENT_TYPE常量值')
    order_model = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='订单模式（0销售型, 1展示型, 2自提点, 3虚拟销售）')
    is_under_line = Column(TINYINT, nullable=False, server_default=text("'0'"), comment='是否线下支付（0否，1是）')
    pay_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='支付时间')
    confirm_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='确认时间')
    delivery_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='发货时间')
    cancel_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='取消时间')
    collect_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='收货时间')
    close_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='关闭时间')
    comments_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='评论时间')
    is_comments = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='商家是否已评论（0否, 大于0评论时间）')
    user_is_comments = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='用户是否已评论（0否, 大于0评论时间）')
    is_delete_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='商家是否已删除（0否, 大于0删除时间）')
    user_is_delete_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='用户是否已删除（0否, 大于0删除时间）')
    add_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='添加时间')
    upd_time = Column(INTEGER, nullable=False, server_default=text("'0'"), comment='更新时间')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
