from base.base import mysql_conn_session
from model.sxo_order_aftersale import SxoOrderAftersaleModel
from model.sxo_order_detail import SxoOrderDetailModel


@mysql_conn_session
def get_order_detail_buy_number(conn, af_order_id):
    """
    获取订单详情表中对应的购买数量

    :return:
    """
    fit = {
        SxoOrderAftersaleModel.id.name: int(af_order_id)
    }
    # data_1 = conn.query(SxoOrderAftersaleModel).filter_by(**fit).first()
    fields = [SxoOrderDetailModel.buy_number]
    order_details_info = conn.query(*fields).\
        join(SxoOrderAftersaleModel, SxoOrderAftersaleModel.order_detail_id == SxoOrderDetailModel.id). \
        filter_by(**fit).first()
    # conn.commit()
    print(order_details_info[0])


if __name__ == '__main__':
    get_order_detail_buy_number(af_order_id=126)
