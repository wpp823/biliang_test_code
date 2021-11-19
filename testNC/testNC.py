import json

import requests

SS_SPU_NEED_EDIT_ONLINE = 0  # 获取线上数据
SS_SPU_NEED_EDIT_DRAFT = 1  # 获取草稿数据

# 商品状态
SS_SPU_STATUS_ON = 5  # 上架
SS_SPU_STATUS_INIT = 0  # 初始值
SS_SPU_STATUS_RECY = 6  # 回收站
SS_SPU_STATUS_DELE = 9  # 逻辑删除
SS_SPU_STATUS_OFF = 11  # 自主下架
SS_SPU_STATUS_VIOL = 13  # 违规下架/风控系统下架
SS_SPU_STATUS_OUT = 12  # 售磬下架

SPU_STATUS = [
    SS_SPU_STATUS_ON,
    SS_SPU_STATUS_INIT,
    SS_SPU_STATUS_RECY,
    SS_SPU_STATUS_DELE,
    SS_SPU_STATUS_OFF,
    SS_SPU_STATUS_VIOL,
    SS_SPU_STATUS_OUT
]


def get_product_id_list(status: int, page: int = 1):
    url = 'http://127.0.0.1:18851/in/mnc/api/v1/spu/products'
    # ?keyword=&

    page_size = 9

    params_data = {
        "status": status,
        "page": page,
        "page_size": page_size,
        "need_edit_spu": SS_SPU_NEED_EDIT_ONLINE,
    }
    res = requests.request(method="GET", url=url, headers='', params=params_data, timeout=9999999)
    item_raw = res.json().get("data", [])

    if item_raw:

        item_raw = res.json().get("data", [])

        print(res.json())
        for item in item_raw:
            product_id = item.get("product_id", None)
            aync_product_spu_data(product_id=product_id)
        page += 1
        # get_product_id_list(page=page,status=status)


def aync_product_spu_data(product_id):
    # 更新数据
    sync_url = 'http://127.0.0.1:18851/in/mnc/api/v1/spu/product/sync'
    data = {
        "product_id": product_id
    }
    res = requests.request(method="POST", url=sync_url, data=data, timeout=9999999)

    if res and res.status_code == 200:
        print(res.json())


if __name__ == "__main__":
    for status in SPU_STATUS:
        print(status)
        get_product_id_list(status=status)
