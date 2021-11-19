import requests

SS_SPU_NEED_EDIT_ONLINE = 0  # 获取线上数据
SS_SPU_NEED_EDIT_DRAFT = 1  # 获取草稿数据
NC_PRODUCT_PAGE_SIZE = 100
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
# server_url = "dds-wz9db3743e6de5041152-pub.mongodb.rds.aliyuncs.com"
server_url = "127.0.0.1"


def get_product_id_list(status, page, page_size):
    url = f'http://{server_url}:18851/in/mnc/api/v1/spu/products'
    # ?keyword=&

    page_size = 10

    params_data = {
        "status": status,
        "page": page,
        "page_size": page_size,
        "need_edit_spu": SS_SPU_NEED_EDIT_DRAFT,
    }
    res = requests.request(method="GET", url=url, headers='', params=params_data, timeout=9999999)
    item_raw = res.json().get("data", [])
    print(status)
    print(item_raw)
    return item_raw


def sync_product_spu_data(product_id):
    sync_url = f'http://{server_url}:18851/in/mnc/api/v1/spu/product/sync'
    data = {
        "product_id": product_id
    }
    res = requests.request(method="POST", url=sync_url, data=data, timeout=9999999)

    if res and res.status_code == 200:
        print(res.json())


if __name__ == "__main__":

    for status in SPU_STATUS:
        page_num = 1
        while True:
            res_data = get_product_id_list(status=status, page=page_num, page_size=NC_PRODUCT_PAGE_SIZE)
            if res_data:
                # 获取到商品id列表与mongo中对比，不在列表中，更新商品状态
                product_id = ""
                for item in res_data:
                    try:
                        print(product_id)
                        product_id = item.get("product_id", None)
                        sync_product_spu_data(product_id=product_id)
                    except Exception as e:
                        print(str(e))
                        print("run_sync_product_data,aync_product_spu_data,product_id{}".format(product_id))
                        break
                # 获取一次翻页数据
                page_num += 1
            else:
                break
