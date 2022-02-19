#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_maplocal.py
@time:2020/11/29
"""
from mitmproxy import http
import re
from mitmproxy import ctx


# def request(flow: http.HTTPFlow):
#     # 修改判断条件
#     if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
#         # 打开保存在本地的数据文件
#         with open("/Users/chenshifeng/MyCode/PythonCode/SFDSZL/interface/quote.json") as f:
#             # 创造一个 response
#             flow.response = http.HTTPResponse.make(
#                 200,  # (optional) status code
#                 # 读取文件中数据作为返回内容
#                 f.read(),
#                 # 指定返回数据的类型
#                 {"Content-Type": "application/json"}  # (optional) headers
#             )


# coding: utf-8
# modify_response.py



def response(flow):
    """修改应答数据
    """
    if '/js/index.' in flow.request.url:
        # 屏蔽selenium检测
        for webdriver_key in ['webdriver', '__driver_evaluate', '__webdriver_evaluate', '__selenium_evaluate', '__fxdriver_evaluate', '__driver_unwrapped', '__webdriver_unwrapped',
                              '__selenium_unwrapped', '__fxdriver_unwrapped', '_Selenium_IDE_Recorder', '_selenium', 'calledSelenium', '_WEBDRIVER_ELEM_CACHE', 'ChromeDriverw',
                              'driver-evaluate', 'webdriver-evaluate', 'selenium-evaluate', 'webdriverCommand', 'webdriver-evaluate-response', '__webdriverFunc',
                              '__webdriver_script_fn', '__$webdriverAsyncExecutor', '__lastWatirAlert', '__lastWatirConfirm', '__lastWatirPrompt', '$chrome_asyncScriptInfo',
                              '$cdc_asdjflasutopfhvcZLmcfl_']:
            ctx.log.info('Remove "{}" from {}.'.format(webdriver_key, flow.request.url))
            flow.response.text = flow.response.text.replace('"{}"'.format(webdriver_key), '"NO-SUCH-ATTR"')
        flow.response.text = flow.response.text.replace('t.webdriver', 'false')
        flow.response.text = flow.response.text.replace('ChromeDriver', '')