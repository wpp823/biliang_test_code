# coding:utf-8
__author__ = 'rk.feng'

import logging  # noqa
import os  # noqa
import typing  # noqa

from mongoengine import *


class AutoIncrementModel(DynamicDocument):
    """
    自增模型
    """
    meta = {
        'strict': False,
        "collection": "auto_increment",
        'indexes': []
    }

    key = StringField(help_text="key", unique=True)
    count = LongField(help_text="当前值")
