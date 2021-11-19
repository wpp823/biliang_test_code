

__author__ = 'xiaozc'

import copy
import arrow
import shortuuid
import re
from daredevil.mongodb.model.wx_message import WxMessageModel, WxMessageContentObj, WxMessageReferObj


class WxMessageDao():
    # 微信聊天记录

    def __init__(self):
        # self.log = log
        self.collection = 'wx_message'

    def update_msg_img_url(self, from_username, msgSvrId, upload_id: str, img_url: str, upload_img_record_id: str):
        """
        更新图片地址
        :param from_username:
        :param msgSvrId:
        :param upload_id:
        :param img_url:
        :param upload_img_record_id:
        :return:
        """
        fit = {
            WxMessageModel.from_username.name: from_username,
            WxMessageModel.msgSvrId.name: str(msgSvrId),
            WxMessageModel.msg_type.name: 'image',
        }

        update_info = {
            "$set": {
                '{}.{}'.format(WxMessageModel.msg_content.name, WxMessageContentObj.upload_id.name): upload_id,
                '{}.{}'.format(WxMessageModel.msg_content.name, WxMessageContentObj.url.name): img_url,
                WxMessageModel.upload_img_record_id.name: upload_img_record_id,
                WxMessageModel.update_at.name: arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')
            }
        }
        return WxMessageModel.objects(__raw__=fit).update(__raw__=update_info)


    def update_refer_msg_img_url(self, from_username, refer_msg_id, upload_id: str, img_url: str, upload_img_record_id: str):
        """
        更新引用消息图片地址
        :param from_username:
        :param refer_msg_id:
        :param upload_id:
        :param img_url:
        :param upload_img_record_id:
        :return:
        """
        fit = {
            WxMessageModel.from_username.name: from_username,
            '{}.{}'.format(WxMessageModel.refer.name, WxMessageReferObj.msg_id.name): refer_msg_id,
            '{}.{}'.format(WxMessageModel.refer.name, WxMessageReferObj.msg_type.name): 'image',
        }

        update_info = {
            "$set": {
                '{}.{}.{}'.format(WxMessageModel.refer.name, WxMessageReferObj.content_lite.name, WxMessageContentObj.upload_id.name): upload_id,
                '{}.{}.{}'.format(WxMessageModel.refer.name, WxMessageReferObj.content_lite.name, WxMessageContentObj.url.name): img_url,
                '{}.{}'.format(WxMessageModel.refer.name, WxMessageReferObj.upload_img_record_id.name): upload_img_record_id,
                WxMessageModel.update_at.name: arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')
            }
        }
        return WxMessageModel.objects(__raw__=fit).update(__raw__=update_info)

    def update_msg_content(self,msg_id,msg_content):
        """
        更新转发数据内容
        :param msg_id:
        :param msg_content:
        :return:
        """
        fit = {
            WxMessageModel.msg_id.name: msg_id,
        }

        update_info = {
            "$set": {
                # WxMessageModel.msg_content.name : msg_content,

                WxMessageModel.update_at.name: arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S'),
                "{}.{}".format(WxMessageModel.msg_content.name,WxMessageContentObj.forward_msg_desc.name): msg_content['forward_msg_desc'],
                "{}.{}".format(WxMessageModel.msg_content.name,WxMessageContentObj.forward_msg_title.name): msg_content['forward_msg_title'],
                "{}.{}".format(WxMessageModel.msg_content.name,WxMessageContentObj.forward_msg_content_list.name): msg_content['forward_msg_content_list']
            }
        }
        return WxMessageModel.objects(__raw__=fit).update(__raw__=update_info)