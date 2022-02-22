#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2021/12/23 22:43
# @Author  : wyy
# @Email   : wpp_work_mail@163.com
# @File    : main.py
# @Software: PyCharm


from pymongo import MongoClient

MONGO_HOST_PART = "mongodb://admin:a.123456@127.0.0.1"
MONGO_HOST_AUTH_DB = "admin"
MONGO_HOST_REPLICA_SET = None
database = 'mytest'

# connect(host=f"{MONGO_HOST_PART}/{database}?authSource={MONGO_HOST_AUTH_DB}")
conn = MongoClient(host=f"{MONGO_HOST_PART}/{database}?authSource={MONGO_HOST_AUTH_DB}")
my_col = conn["hello"]
# my_col.my_col
print(conn.database_names())

