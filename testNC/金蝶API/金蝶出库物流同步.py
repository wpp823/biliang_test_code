import arrow
import requests

from my_log import get_logger

log = get_logger()

def sync_sal_outbound_delivery_order():
    """
    同步销售出库单物流
    """

    log.info("[sync_sal_outbound_delivery_order][begin]")
    # client = jindie.JindieClient(service_name=DEP_NC_SERVER_NAME, log=log, port=DEP_NC_SERVER_PORT,
    #                              header_host=DEP_NC_HOSTNAME, headers=None)
    sync_order_url = "http://127.0.0.1:18851/in/mnc/api/v1/jindie/sal/outbound/order/delivery"
    now_at = arrow.now().to(tz="+08:00").timestamp()
    try:
        begin_data = requests.get(url=sync_order_url)

        begin_at = begin_data.json().get("data","")
        begin_at = "2022-04-20 18:32:40"
        if not begin_at:
            begin_at = arrow.now(tz="+08:00").shift(days=-10).timestamp()  # 无数据默认十天之内的发货订单
        else:
            begin_at = arrow.get(begin_at).to(tz="+08:00").timestamp()

        ids_params = {
            "begintime":begin_at,
            "expiretime":now_at

        }
        url_1 = "http://127.0.0.1:18851/in/mnc/api/v1/jindie/sal/outbound/order/list"
        out_order_data = requests.get(url=url_1,params=ids_params)#.get_outbound_order_ids(begintime=begin_at, expiretime=now_at)
        out_order_ids = out_order_data.json().get("data",[])
        for number in out_order_ids:
            data = {
                "number": number,

            }
            sync_sal_order_result = requests.post(url=sync_order_url, data=data)
            if sync_sal_order_result:
                log.info("[sync_sal_outbound_order_result_ok][id:{}]".format(id))
            else:
                log.info("[sync_sal_outbound_order_result_fail][id:{}]".format(id))
        else:
            log.info("[sync_sal_outbound_order][no_order_need_sync][out_order_ids:{}]".format(out_order_ids))
    except:
        log.exception("[sync_sal_outbound_order]")

    log.info("[sync_sal_outbound_order][end]")


if __name__ == "__main__":
    sync_sal_outbound_delivery_order()