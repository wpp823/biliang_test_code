import requests

from my_log import get_logger

log = get_logger()
get_ext_urls = 'http://127.0.0.1:18851/in/mnc/api/v1/product/price/urls'
update_ext_urls = 'http://127.0.0.1:18851/in/mnc/api/v1/product/price'
product_ext_url_info = requests.get(get_ext_urls)

if product_ext_url_info:
    url_data = product_ext_url_info.json()
    urls = url_data.get("data")
    for msg in urls:
        product_id = msg.get("product_id", None)
        sku_id = msg.get("sku_id", None)
        ext_url = msg.get("ext_url", "")

        params ={
            "product_id":product_id,
            "sku_id":sku_id,
            "ext_url":ext_url
        }
        log.info(params)

        req_data = requests.post(update_ext_urls,params=params)
        log.info(req_data.json())
