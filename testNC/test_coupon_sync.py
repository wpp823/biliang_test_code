import time

import requests

STATUS_DRAFT = 1  # 草稿
STATUS_TAKE_EFFECT = 2  # 生效
STATUS_BE_OVERDUE = 3  # 过期
STATUS_TO_VOID = 4  # 已作废
STATUS_TO_DELETE = 5  # 删除
STATUS_OVER_OR_VOID = 200  # 过期 or 作废的券

COUPON_STATUS = [
    # STATUS_DRAFT,
    # STATUS_TAKE_EFFECT,
    STATUS_BE_OVERDUE,
    # STATUS_TO_VOID,
    # STATUS_TO_DELETE,
    # STATUS_OVER_OR_VOID
]


def get_coupon_id_list(start_create_time, end_create_time, status, page):
    url = 'http://127.0.0.1:18851/in/mnc/api/v1/coupon/list'
    # ?keyword=&

    page_size = 9

    params_data = {
        "start_create_time": start_create_time,
        "end_create_time": end_create_time,
        "status": status,
        "page": page,
        "page_size": page_size,
    }
    res = requests.request(method="GET", url=url, headers='', params=params_data, timeout=9999999)
    item_raw = res.json().get("data", [])

    if item_raw:
        item_raw = res.json().get("data", [])

        print(res.json())
        for coupon_id in item_raw:
            # coupon_id = item.get("coupon_id", None)
            sync_coupon_data(coupon_id=coupon_id)

        # page += 1
        # get_order_id_list(page=page)


def sync_coupon_data(coupon_id):
    # 更新数据
    # order_id = 1440606056991475
    sync_url = 'http://127.0.0.1:18851/in/mnc/api/v1/coupon/sync'
    data = {
        "coupon_id": coupon_id
    }
    print(data)
    res = requests.request(method="POST", url=sync_url, data=data, timeout=9999999)

    if res and res.status_code == 200:
        print(res.json())


def get_begin_at():
    sync_url = 'http://127.0.0.1:18851/in/mnc/api/v1/coupon/sync/max/time'
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
    for order_status in COUPON_STATUS:
        # start_update_time = "2021-12-01 10:00:00"
        # end_update_time = "2022-01-05 00:00:00"
        status = order_status
        page = 1
        page_size = "10"
        print(status)
        get_coupon_id_list(start_update_time, end_update_time, status, page)
