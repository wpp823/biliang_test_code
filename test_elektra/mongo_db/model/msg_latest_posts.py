# coding:utf-8
__author__ = 'rk.feng'

import logging  # noqa
import os  # noqa
import typing  # noqa

from mongoengine import *

from app.mongo_db.model.msg import MsgBody


class LatestMsgModel(DynamicDocument):
    """
    用户每个帖子中最新一条消息
    使用场景: 工作台中, 获取医生每个聊天的最新一条消息
    """
    meta = {
        'strict': False,
        "collection": "msg_latest_chat",
        'indexes': [
            {
                "fields": ["doctor_id"],
                'name': '_doctor_id_'
            },
            {
                "fields": ["last_doctor_chat.chat_at"],
                'name': '_last_doctor_chat__chat_at_'
            },
            {
                "fields": ["last_user_chat.chat_at"],
                'name': '_last_user_chat__chat_at_'
            }
        ]
    }

    doctor_id = StringField(help_text='医生id')
    user_id = StringField(help_text='用户id')
    thread_id = StringField(help_text='帖子id, 全局唯一', unique=True)
    thread_type = StringField(help_text='帖子类型')
    create_at = LongField()
    create_at_date = StringField()

    # 额外信息
    chat_name = StringField(help_text="聊天名称")  # fixme 展示时, 使用另一个用户名作为聊天名称, 似乎更优
    avatar = StringField(help_text="头像/图标")

    last_user_chat = EmbeddedDocumentField(MsgBody, help_text="user_id 看到的最后一条消息")  # 用户(私聊, 应用, AI 助理)
    last_doctor_chat = EmbeddedDocumentField(MsgBody, help_text="doctor_id 看到的最后一条消息")  # 医生
