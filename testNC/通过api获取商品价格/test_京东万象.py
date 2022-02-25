import requests

from my_log import get_logger

log= get_logger()
url = 'https://way.jd.com/TONGLI/MDetailGetDetail'
params = {
    'num_iid' : '600759989300',
    'appkey' : 'ccdef7f10fe0a01cff1e48728f6eb315'
}

response = requests.post(url, params)
json_msg = response.json()

log.info(json_msg)
log.info(response.text)
