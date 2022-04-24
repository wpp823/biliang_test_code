import requests

from my_log import get_logger

log = get_logger()

def sync_sal_order():
    """
    同步销售单

    """


    base_url = 'http://127.0.0.1:18851'

    ids_path_info = '/in/mnc/api/v1/jindie/sal/order'
    sync_jindie_path_info = '/in/mnc/api/v1/jindie/sal/order'
    get_ids_url = base_url + ids_path_info
    sync_order_url = base_url + sync_jindie_path_info

    log.info("[sync_sal_order][begin]")
    #
    # client = jindie.JindieClient(service_name=DEP_NC_SERVER_NAME, log=log, port=DEP_NC_SERVER_PORT,
    #                              header_host=DEP_NC_HOSTNAME, headers=None)
    try:
        order_ids = requests.get(url=get_ids_url)

        # order_ids = client.get_sal_orders()

        if order_ids:
            for order_id in order_ids:
                data = {
                    "order_id": order_id
                }
                sync_sal_order_result = requests.post(url=sync_order_url, data=data)

                if sync_sal_order_result:
                    log.info("[sync_sal_order_result_ok][order_id:{}]".format(order_id))
                else:
                    log.info("[sync_sal_order_result_fail][order_id:{}]".format(order_id))
        else:
            log.info("[sync_sal_order][no_order_need_sync][order_ids:{}]".format(order_ids))
    except:
        log.exception("[sync_sal_order]")

    log.info("[sync_sal_order][end]")
