from typing import List

import arrow
import shortuuid

from daredevil.朋友圈数据同步.mongo_db.wx_sns_img import WxSnsImgModel


class WxChatSnsImgDao():
    # 微信朋友圈记录

    def __init__(self, log):
        self.log = log
        self.collection = 'wx_sns_img'

    def add(self, from_username, snsId, createTime, img_index, img_url, upload_id, create_at, device_id, batch_id):
        """

        :param from_username:
        :type from_username:
        :param snsId:
        :type snsId:
        :param createTime:
        :type createTime:
        :param img_index:
        :type img_index:
        :param img_url:
        :type img_url:
        :param upload_id:
        :type upload_id:
        :param create_at:
        :type create_at:
        :param device_id:
        :type device_id:
        :param batch_id:
        :type batch_id:
        :return:
        :rtype:
        """
        wx_sns_img_obj = WxSnsImgModel()
        now_at = arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')
        wx_sns_img_obj.sns_img_id = "sns_img_{}".format(shortuuid.random(12))
        wx_sns_img_obj.from_username = from_username
        wx_sns_img_obj.snsId = snsId
        wx_sns_img_obj.createTime = createTime
        wx_sns_img_obj.img_index = img_index
        wx_sns_img_obj.img_url = img_url
        wx_sns_img_obj.upload_id = upload_id
        wx_sns_img_obj.create_at = create_at
        wx_sns_img_obj.update_at = now_at
        wx_sns_img_obj.device_id = device_id
        wx_sns_img_obj.batch_id = batch_id

        try:
            res = WxSnsImgModel.save(wx_sns_img_obj)
        except Exception as e:
            self.log.exception("[WxChatSnsImgDao.add]")
            return False

        return res

    def update(self):
        pass

    def get_by_sns_id_index(self, sns_id: str, index: int,from_username:str, fields: List):
        """
        获取朋友圈图片通过图片顺序和朋友圈id
        """
        fit = {
            WxSnsImgModel.snsId.name: sns_id,
            WxSnsImgModel.from_username.name: from_username,

            WxSnsImgModel.img_index.name: int(index)
        }

        return WxSnsImgModel.objects(__raw__=fit).only(*fields).first()
