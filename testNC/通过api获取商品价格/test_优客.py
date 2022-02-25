import requests

from my_log import get_logger

log= get_logger()
app_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2YWx1ZSI6InlrenMxMjM0NTZ3ZWJ2YWx1ZSIsIm5hbWUiOiJiaWxpYW5nMTIzNCIsIm5iZiI6MTY0NTU4Mzg4NywiZXhwIjoxOTYxMTE2Njg3LCJpc3MiOiIxMzczNzExNThAcXEuY29tIiwiYXVkIjoiMTM3MzcxMTU4QHFxLmNvbSJ9._P-Mb1f5vak6Jmz3S4KfiWtTvCMg3XC4ovIT4wjBprU"

# itemid = 606740156728 无促销价返还'skus': [{'skuid': '4438549425106', 'sale_price': '298', 'origin_price': None, 'stock': '200', 'props_ids': '147956252:75367145'}]
# itemid = 589726457718
# itemid = 626648472514
itemid = 610982260060
# url = f'http://api.youkezhushou.com/api/taobao/itemv2?itemid={itemid}&token={app_token}'
url = 'http://api.youkezhushou.com/api/taobao/itemv2'
params = {
    'itemid' : itemid,
    'token' : app_token
}

response = requests.get(url,params=params)
json_msg = response.json()

log.info(json_msg)
log.info(response.text)
