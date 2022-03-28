#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/3/26 20:45
# @Author  : wyy
# @Email   : wpp_work_mail@163.com
# @File    : 商品批量添加.py
# @Software: PyCharm
import json
from typing import Dict

import redis as redis
import requests

from my_log import get_logger

client_id = '205022'
client_secret = '1b16d77089b1e60b3f7c907aa3cc612e'
username = '17220202021'
password = 'Jdy202101'
host = "https://api.kingdee.com"
http_host = "http://api.kingdee.com"

app_data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "username": username,
    "password": password,
}

log = get_logger()
# redis = get_redis(host="127.0.0.1", password=None, log=log)

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
redis = redis.Redis(host='localhost', port=6379, decode_responses=True)


def fetch_token(params: Dict):
    """
    获取账户信息

    """
    api_path = '/auth/user/access_token'
    full_url = http_host + api_path
    # json_data = json.dumps(params)
    res = requests.get(url=full_url, params=params)
    res_json = res.json()
    access_token = None
    if res:
        ret_data = res.json().get("data", {})
        access_token = ret_data.get("access_token", {})
        redis.set("jindie_api_access_token", access_token, ex=60 * 60)
        log.info(f"fetch_token:{ret_data}")
    return access_token


def get_token():
    api_token = redis.get("jindie_api_access_token")
    if not api_token:
        api_token = fetch_token(app_data)

    return api_token


def get_account(app_token, service_id, account_id):
    """

    """
    api_path = '/jdy/sys/accountGroup'

    full_url = host + api_path + f"?access_token={app_token}"
    # json_data = json.dumps(params)
    res = requests.post(url=full_url)
    ret_data = {}
    if res:
        ret_data = res.json().get("data", [])
        # account_groups = ret_data.get("accountGroups", [])
        for account in ret_data:
            if account.get("serviceId") == service_id:
                for item in account.get("accountGroups", []):
                    if item.get("accountId") == account_id:
                        ret_data = item
                # return account

        log.info(f"get_account:{ret_data}")
    return ret_data


def add_product(account_data):
    """
    添加商品

    """



if __name__ == "__main__":
    token = get_token()
    log.info(f"token:{token}")
    account_data = get_account(token, service_id="7944692913991", account_id='1626231450425742965')
