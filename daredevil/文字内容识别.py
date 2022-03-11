
# coding:utf-8
__author__ = 'rk.feng'

import logging  # noqa
import os  # noqa
import typing  # noqa
import unittest  # noqa


from white_queen_nlp import jieba_utils

if __name__ == '__main__':
    jieba_obj = jieba_utils.load_jieba()
    d = jieba_utils.DiseaseCutV3(logger=logging.getLogger(), jieba=jieba_obj)

    s_list = [
        # "怎么办",
        "高血压和高血脂, 要注意什么"
    ]
    print(d.parse_disease_words(s_list))
    for d_w_list in d.parse_disease_words(s_list):
        print(d_w_list)