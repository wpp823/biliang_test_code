# coding:utf-8
__author__ = 'rk.feng'

import logging  # noqa
import os  # noqa
import typing  # noqa
from enum import Enum

import arrow
from mongoengine import *


class MsgType(str, Enum):
    AI_ASSISTANT = "ai_assistant"  # AI 助理
    ONE_ONE_CHAT = "one_one_chat"  # 私聊

    APP_QUESTION_MISS = "app_question_miss"  # 应用: 未答问题
    APP_APPROVE = "app_approve"  # 应用: 审批
    APP_PHONE = "app_phone"  # 应用: 手机
    APP_WECHAT = "app_wechat"  # 应用: 微信
    APP_STATISTICS = "app_statistics"  # 应用: 统计
    APP_DIARY = "app_diary"  # 应用: 日记
    APP_ARTICLE = "app_article"  # 应用: 文章
    APP_QA = "app_qa"  # 应用: 问答
    APP_FRIENDS = "app_circle_of_friends"  # 应用: 朋友圈

    # 客服独有的应用
    APP_EMPLOY_TASK = "icongzt_cgwt1"  # 任务助手

    @classmethod
    def build_app_thread_id(cls, msg_type: 'MsgType', user_id: str) -> str:
        """ 创建应用的会话 id """
        return "{}_{}".format(msg_type, user_id)

    @classmethod
    def build_o2o_thread_id(cls, doctor_id: str, user_id: str) -> str:
        """ 创建 一对一 会话 id """
        return "o2o_{}_{}".format(doctor_id, user_id)

    @classmethod
    def build_employ_app_thread_id(cls, msg_type: 'MsgType', user_id: str, doctor_id: str) -> str:
        """ 创建应用的会话 id """
        return "{}_{}_{}".format(msg_type, user_id, doctor_id)


class AppConfig:
    APP_QUESTION_MISS = {"id": MsgType.APP_QUESTION_MISS, "name": "未答问题"}
    APP_APPROVE = {"id": MsgType.APP_APPROVE, "name": "审批"}
    APP_WECHAT = {"id": MsgType.APP_WECHAT, "name": "微信"}

    APP_STATISTICS = {"id": MsgType.APP_STATISTICS, "name": "统计"}
    APP_PHONE = {"id": MsgType.APP_PHONE, "name": "手机"}
    APP_FRIENDS = {"id": MsgType.APP_FRIENDS, "name": "朋友圈"}
    APP_QA = {"id": MsgType.APP_QA, "name": "问答"}
    APP_DIARY = {"id": MsgType.APP_DIARY, "name": "日记"}
    APP_ARTICLE = {"id": MsgType.APP_ARTICLE, "name": "文章"}

    app_list = [
        APP_STATISTICS,
        APP_PHONE,
        # APP_FRIENDS,
        APP_QA,
        APP_DIARY,
        APP_ARTICLE,
    ]


# 未答问题卡片
class MsgCard:
    type_name = "msg_card"  # 未答问题卡片

    def __init__(self, name: str, image: str, create_at: arrow.Arrow, op_name: str, target_url: str):
        self.name = name
        self.image = image
        self.create_at = create_at
        self.op_name = op_name
        self.target_url = target_url

    def to_msg(self) -> dict:
        """ """
        return {
            "name": self.name,
            "image": self.image,
            "create_at": self.create_at.format("M月D日"),
            "op_name": self.op_name,
            "target_url": self.target_url,
        }


class MsgBody(DynamicEmbeddedDocument):
    chat_at = LongField()  # 聊天时间, 时间戳
    chat_at_date = StringField()  # 聊天时间
    msg_type = StringField(help_text="消息会话: 消息类型")  # 消息会话: 消息类型
    chat_msg = DictField()  # 聊天内容

    @property
    def simple_text(self):
        """ """
        from app.conf.setting import IMAGE_MAS_CARD_ARTICLE_ADD_QUESTION

        if self.msg_type == "msg_card":
            default_name = self.chat_msg.get("name", "")

            if IMAGE_MAS_CARD_ARTICLE_ADD_QUESTION:
                if self.chat_msg.get("image") == IMAGE_MAS_CARD_ARTICLE_ADD_QUESTION:
                    return "[问答库追加1条问题]"

            return default_name

        if self.msg_type == "text" or self.msg_type == "action_desc":
            return self.chat_msg.get("desc", "")

        if self.msg_type == "miniprogram":
            return self.chat_msg.get("title", "")

        if self.msg_type == "inquiry_application":
            return "{}{}".format(
                "" if not self.chat_msg.get("patient_name") else f"{self.chat_msg.get('patient_name')}的",
                self.chat_msg["name"]
            )

        # fixme not finish


class Env(DynamicEmbeddedDocument):
    thread_id = StringField(help_text="会话 id")
    thread_type = StringField(help_text="会话类型")
    name = StringField(help_text="会话名称")

    def build_at_dict(self, ) -> dict:
        return {
            "thread_id": self.thread_id,
            "type": self.thread_type,
            "name": self.name,
        }


class MsgFrom(DynamicEmbeddedDocument):
    user_id = StringField()
    nickname = StringField()
    avatar = StringField()
    role = StringField()  # 角色: 医生, 病人, 人工助理, 未答问题


class Refer(DynamicEmbeddedDocument):
    msg_id = StringField()
    content_lite = EmbeddedDocumentField(MsgBody)
    msg_from = EmbeddedDocumentField(MsgFrom)


class MsgSource(DynamicEmbeddedDocument):
    thread_id = StringField()
    msg_id = StringField()
    chat_at = StringField()


class Receiver(DynamicEmbeddedDocument):
    STATUS_UNREAD = 0  # 未读
    STATUS_HAVE_READ = 1  # 已读

    user_id = StringField()
    status = IntField(help_text="消息状态", choices=[STATUS_UNREAD, STATUS_HAVE_READ])


class MsgListModel(DynamicDocument):
    """
    消息模型: 存储所有的消息
    使用场景: 医生获取所有消息
    模型说明: 一个会话, 一条消息. 会话中成员, 写入到 receiver_list 中.
    """
    meta = {
        'strict': False,
        "collection": "msg_list",
        'indexes': [
            {
                "fields": ["at.thread_id"],
                'name': '_at__thread_id_'
            },
        ]
    }

    msg_id = IntField(help_text="消息 ID: 在消息对话中创建的 id. 该值全局唯一, 且自增", unique=True)

    msg_body = EmbeddedDocumentField(MsgBody)  # 消息会话: 消息实体. 注意, 消息本身不能修改
    at = EmbeddedDocumentField(Env)  # 消息会话: 会话环境
    refer = EmbeddedDocumentField(Refer)  # 消息会话: 引用消息
    msg_from = EmbeddedDocumentField(MsgFrom)  # 消息会话: 消息来源
    receiver_list = ListField(EmbeddedDocumentField(Receiver))  # 接收者(会话中的成员)
    source_data = DictField()  # 源信息: 原始会话

    def to_msg(self) -> dict:
        """ 生成消息协议数据 """
        # note: 不存在 to 接收者

        data = {
            "msg_version": "1.0",
            "tags": [],
            "msg_id": str(self.msg_id),
            "msg_type": self.msg_body.msg_type,

            # 消息体
            "create_at": arrow.get(self.msg_body.chat_at).to("Asia/Shanghai").format("YYYY/MM/DD HH:mm:ss"),
            "content": self.msg_body.chat_msg,
        }

        # from
        if self.msg_from:
            data["from"] = self.msg_from.to_mongo().to_dict()
        else:
            data["from"] = {}

        # 会话环境
        # fixme 会话名称, 实时生成
        if self.at:
            data["at"] = self.at.build_at_dict()
        else:
            data["at"] = {}

        # fixme debug
        if not data["at"] and not data["at"]["name"]:
            data["at"]["name"] = "会话名称待定"

        # 引用
        if self.refer:
            data["refer"] = self.refer.to_mongo().to_dict()
        else:
            data["refer"] = {}

        return data
