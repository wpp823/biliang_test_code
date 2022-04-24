import requests


def sync_sal_inbound_order():
    """
    同步销售退货单
    """

    print("[sync_sal_inbound_order][begin]")
    base_url = 'http://127.0.0.1:18851'

    ids_path_info = '/in/mnc/api/v1/jindie/sal/inbound/order'
    sync_jindie_path_info = '/in/mnc/api/v1/jindie/sal/inbound/order'
    get_ids_url = base_url + ids_path_info
    sync_order_url = base_url + sync_jindie_path_info

    try:

        order_id_info = requests.get(url=get_ids_url)

        if order_id_info:
            order_ids = order_id_info.json().get("data",[])
            for order_id in order_ids:
                data = {
                    "aftersale_order_id": order_id
                }
                sync_sal_inbound_order_result = requests.post(url=sync_order_url, data=data)
                if sync_sal_inbound_order_result:
                    print("[sync_sal_inbound_order_result_ok][order_id:{}]".format(order_id))
                else:
                    print("[sync_sal_inbound_order_result_fail][order_id:{}]".format(order_id))
        else:
            print("[sync_sal_inbound_order][no_order_need_sync][order_ids:{}]".format(order_id_info))
    except:
        print("[sync_sal_inbound_order]")
        pass

    print("end")


if __name__ == "__main__":
    sync_sal_inbound_order()
