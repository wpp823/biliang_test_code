# 1.获取token
# 2.获取账套
# 3.获取商品详情列
# 4.获取订单
import json

import requests


def get_token():
    # 登录参数
    token_request_data = {
        "client_id": '205022',
        "client_secret": '1b16d77089b1e60b3f7c907aa3cc612e',
        "username": '17220202021',
        "password": 'Jdy202101'
    }
    host = 'https://api.kingdee.com'
    path = '/auth/user/access_token'
    url = host + path
    response = requests.post(url, data=token_request_data)
    if response:
        print(response.content.decode())

        token_data = response.json().get("data", {})
        return token_data.get('access_token')


def get_account(access_token):
    # 登录参数

    host = 'https://api.kingdee.com'
    path = '/jdy/sys/accountGroup'
    url = host + path
    data = {
        "access_token": access_token
    }
    response = requests.post(url, data=data)
    if response:
        print(response.content.decode())

        data = response.json().get("data", [])
        # 测试第一个
        account = data[0].get('accountGroups', [])[0]
        print(f"get_account:{account}")
        return account


def get_product_list(account, access_token):
    api_info = f"http://api.kingdee.com/jdy/basedata/material_list?access_token={access_token}"

    data = {
        "search": "",
        "enable": -1,
        "parent": [],
        "starttime": -1,
        "endtime": -1,
        "page": 1,
        "pagesize": 1
    }
    headers = {
        'groupName': account.get("groupName", ""),
        'accountId': account.get("accountId", ""),
        'Content-Type': 'application/json'
    }
    json_data = json.dumps(data)
    # json_data = "{\"search\": \"\", \"enable\": -1, \"parent\": [], \"starttime\": -1, \"endtime\": -1, \"page\": 1, \"pagesize\": 10}"
    response = requests.post(api_info, headers=headers, data=json_data)
    if response:
        print(response.content.decode())

        products = response.json().get("data", {})
        print(f"get_product_list:{products}")
        return products.get("rows", [])


def get_product_info(account, access_token, id):
    api_info = f"http://api.kingdee.com/jdy/basedata/material_detail?access_token={access_token}"

    data = {
        "id": id
    }
    headers = {
        'groupName': account.get("groupName", ""),
        'accountId': account.get("accountId", ""),
        'Content-Type': 'application/json'
    }
    json_data = json.dumps(data)
    response = requests.post(api_info, headers=headers, data=json_data)
    if response:
        print(response.content.decode())

        products = response.json().get("data", {})
        print(f"get_product_list:{products}")
        return products.get("rows", [])


if __name__ == "__main__":
    token = get_token()
    account = get_account(access_token=token)
    product_list = get_product_list(access_token=token, account=account)

    for product in product_list:
        id= product.get("id")
        get_product_info(id=id,account=account,access_token=token)
