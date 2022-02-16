# coding:utf-8
__author__ = 'rk.feng'

import logging  # noqa
import os  # noqa
import typing  # noqa

from mongoengine import *


class QuestionMissModel(DynamicDocument):
    """
    未答问题
    使用场景: 未答问题处理
    """
    meta = {
        'strict': False,
        "collection": "question_miss",
        'indexes': [
            {
                "fields": ["doctor_id"],
                'name': '_doctor_id_'
            },
            {
                "fields": ["status"],
                'name': '_status_'
            },
            {
                "fields": ["expire"],
                'name': '_expire_'
            },
            {
                "fields": ["create_at"],
                'name': '_create_at_'
            },
            {
                "fields": ["msg_msg_id"],
                'name': '_msg_msg_id_'
            },
            {
                "fields": ["doctor_id", "thread_id", "title_hash"],
                'name': '_u_question_',
                'unique': True
            }
        ]
    }

    STATUS_UNDO = 0  # 未处理
    STATUS_DONE = 1  # 已处理
    EXPIRE_NO = 0  # 未逾期
    EXPIRE_YES = 1  # 已逾期

    doctor_id = StringField(help_text='医生id')
    thread_id = StringField(help_text='帖子id')
    thread_type = StringField(help_text='帖子类型')

    title_hash = StringField(help_text='问题md5')
    title = StringField(help_text='问题')
    msg_id = StringField(help_text='该问题对应的聊天')

    user_id = StringField(help_text='用户id, 提问者')
    user_name = StringField(help_text='用户名称')
    user_avatar = StringField(help_text='用户头像')

    # 就诊者: 可能存在 有 patient_name 但无 patient_id 的情形
    patient_id = StringField(help_text="就诊者 ID; 随访贴才有", default=None)
    patient_name = StringField(help_text="就诊者 名称; 随访贴才有", default=None)

    create_at = LongField(help_text="创建时间, 时间戳")
    create_at_date = StringField(help_text="创建时间")

    status = IntField(help_text="状态", choices=[STATUS_UNDO, STATUS_DONE])
    expire = IntField(help_text="是否逾期", choices=[EXPIRE_NO, EXPIRE_YES])
    msg_msg_id = IntField(help_text="消息队列中 msg_id", default=None)

    # answer_msg_id, answer_msg_info 二选一
    answer_msg_id = StringField(help_text='回答对应的msg_id')
    answer_msg_info = DictField(help_text='回答的信息')
    answer_time = LongField(help_text="处理时间, 时间戳")
    answer_date = StringField(help_text="处理时间")

    # 超纲原因
    miss_info = DictField(default={}, help_text="超纲原因")
