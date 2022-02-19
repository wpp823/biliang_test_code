# coding:utf-8
__author__ = 'rk.feng'

import logging  # noqa
import os  # noqa
import typing  # noqa

from mongoengine import DynamicDocument, StringField, LongField, IntField, DynamicEmbeddedDocument, EmbeddedDocumentField


class OriginalObj(DynamicEmbeddedDocument):
    article_id = IntField(help_text="文章 id")
    doctor_id = StringField(help_text="医生 id")
    doctor_name = StringField(help_text="医生姓名, 优先使用 doctor_id 查找当前的医生姓名.")
    answer = StringField(help_text="原创话术内容")


class AnswerOriginalModel(DynamicDocument):
    """
    图文咨询: 原创文章
    """
    meta = {
        'strict': False,
        "collection": "answer_original",
        'indexes': [
            {
                "fields": ["thread_id"],
                'name': '_thread_id_'
            },
            {
                "fields": ["status"],
                'name': '_status_'
            },
            {
                "fields": ["msg_id"],
                'name': '_msg_id_'
            },
            {
                "fields": ["thread_id", "msg_id"],
                'name': '_u_question_',
                'unique': True
            }
        ]
    }

    STATUS_DEFAULT = 0  # 默认
    STATUS_FEEDBACK = 1  # 医生返回判断错误
    STATUS_RECALL = 2  # 原创撤回

    thread_id = StringField(help_text='会话 id')
    thread_type = StringField(default="consult", help_text='会话类型')

    msg_id = IntField(help_text="会话中 id", default=None)
    msg_content = StringField(help_text="消息内容", default="")
    original_obj = EmbeddedDocumentField(OriginalObj, help_text="原创文章")

    create_at = LongField(help_text="创建时间(消息发送时间), 时间戳")
    create_at_date = StringField(help_text="创建时间")
    update_at = LongField(help_text="最后更新时间, 时间戳")
    update_at_date = StringField(help_text="最后更新时间")

    status = IntField(help_text="状态", default=STATUS_DEFAULT, choices=[STATUS_DEFAULT, STATUS_FEEDBACK, STATUS_RECALL])
