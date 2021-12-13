from typing import List
import shortuuid
import arrow

from daredevil.朋友圈数据同步.mongo_db.wx_sns import WxSnsModel, PraiseObj


class WxChatSnsDao():
    # 微信朋友圈记录

    def __init__(self, log):
        self.log = log
        self.collection = 'wx_sns'

    def add(self, snsId, from_username, username, nickname, remark_name, createTime, type, shareTitle, stringSeq, content, praise, comment, url, **kwargs):
        wx_sns_obj = WxSnsModel()
        now_at = arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')
        try:
            wx_sns_obj.sns_id = "sns_{}".format(shortuuid.random(12))
            wx_sns_obj.from_username = from_username
            wx_sns_obj.snsId = str(snsId)
            wx_sns_obj.username = username
            wx_sns_obj.nickname = nickname
            wx_sns_obj.remark_name = remark_name
            wx_sns_obj.createTime = createTime
            wx_sns_obj.type = type
            wx_sns_obj.shareTitle = shareTitle
            wx_sns_obj.stringSeq = stringSeq
            wx_sns_obj.content = content
            wx_sns_obj.praise = praise
            wx_sns_obj.comment = comment
            wx_sns_obj.url = url
            wx_sns_obj.create_at = now_at

            res = WxSnsModel.save(wx_sns_obj)

        except Exception as e:
            self.log.exception('[WxMessageDao.add]')
            return False

        return res

    def get_by_snsId(self, from_username: str, snsId: str, fields: List):
        """
        获取朋友圈，通过snsId
        """
        fit = {
            WxSnsModel.from_username.name: from_username,
            WxSnsModel.snsId.name: snsId
        }

        res = WxSnsModel.objects(__raw__=fit).only(*fields).first()
        return res


    def update_praise(self, from_username: str, snsId: str, content: List[PraiseObj]):
        """
        更新点赞好友列表
        """
        fit = {
            WxSnsModel.from_username.name: from_username,
            WxSnsModel.snsId.name: str(snsId)
        }
        update_info = {
            "$set": {
                WxSnsModel.praise.name: content,
            }
        }
        res = WxSnsModel.objects(__raw__=fit).update(__raw__=update_info)
        return res