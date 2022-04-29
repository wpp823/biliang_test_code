import time

import requests

ORDER_STATUS_PEND = 10  # 待付款
ORDER_STATUS_COLL = 15  # 拼团活动支付成功等待成团中
ORDER_STATUS_RECV = 16  # 支付成功等待商家接单中(同城配送, 线下自提)
ORDER_STATUS_TO_WRIT = 17  # 支付成功待核销
ORDER_STATUS_TO_SHIP = 20  # 待发货
ORDER_STATUS_PART_SHIP = 21  # 部分发货
ORDER_STATUS_TO_RECE = 30  # 待收货
ORDER_STATUS_COMP = 100  # 完成
ORDER_STATUS_COMP_CANC = 200  # 全部商品售后之后，订单取消
ORDER_STATUS_OVER_TIME = 250  # 用户主动取消或待付款超时取消

STATUS_LIST = [
    ORDER_STATUS_PEND,
    ORDER_STATUS_COLL,
    ORDER_STATUS_RECV,
    ORDER_STATUS_TO_WRIT,
    ORDER_STATUS_TO_SHIP,
    ORDER_STATUS_PART_SHIP,
    ORDER_STATUS_TO_RECE,
    ORDER_STATUS_COMP,
    ORDER_STATUS_COMP_CANC,
    ORDER_STATUS_OVER_TIME

]


def get_order_id_list(start_pay_time, end_pay_time, status, page, page_size, source):
    url = 'http://127.0.0.1:18851/in/mnc/api/v1/order/list'
    # ?keyword=&

    page_size = 9

    params_data = {
        "start_update_time": start_pay_time,
        "end_update_time": end_pay_time,
        "status": status,
        "page": page,
        "page_size": page_size,
        "source": source
    }
    res = requests.request(method="GET", url=url, headers='', params=params_data, timeout=9999999)
    item_raw = res.json().get("data", [])

    if item_raw:
        item_raw = res.json().get("data", [])

        print(res.json())
        for item in item_raw:
            order_id = item.get("order_id", None)
            sync_order_data(order_id=order_id)

        # page += 1
        # get_order_id_list(page=page)


def sync_order_data(order_id):
    # 更新数据
    # order_id = 1440606056991475
    sync_url = 'http://127.0.0.1:18851/in/mnc/api/v1/order/sync'
    data = {
        "order_id": order_id
    }
    print(data)
    res = requests.request(method="POST", url=sync_url, data=data, timeout=9999999)

    if res and res.status_code == 200:
        print(res.json())


def get_begin_at():
    sync_url = 'http://127.0.0.1:18851/in/mnc/api/v1/order/sync/max/time'
    data = {}
    res = requests.request(method="GET", url=sync_url, data=data, timeout=9999999)

    if res and res.status_code == 200:
        print(res.json())
        data = res.json().get('data', "")
        if data.get("update_time"):
            return data.get("update_time")


if __name__ == "__main__":
    start_update_time = get_begin_at()
    if not start_update_time:
        start_update_time = "2021-01-01 00:00:00"
    print(start_update_time)
    end_update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(end_update_time)
    for order_status in STATUS_LIST:
        start_update_time = "2022-04-01 10:00:00"
        end_update_time = "2022-04-26 00:00:00"
        status = order_status
        page = 1
        page_size = "10"
        source = "1"
        print(status)
        get_order_id_list(start_update_time, end_update_time, status, page, page_size, source)
