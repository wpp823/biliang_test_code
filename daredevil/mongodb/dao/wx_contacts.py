__author__ = 'xiaozc'

import re
import arrow
import shortuuid

# from app.conf.setting import BLACK_USERNAME_REGEX
from daredevil.mongodb.model.wx_contacts import WxContactsModel
from daredevil.mongodb.model.wx_message import WxMessageModel


class WxContactsDao():
    # 微信联系人

    def __init__(self,log):
        self.log = log
        self.collection = 'wx_contacts'

    def add_contact(self, from_username: str, type: int, alis: str, username: str, nickname: str, conRemark: str,
                    smallheadimgurl: str, bigheadimgurl: str, lastupdatetime: int, contactLabel: list,
                    create_user_id: str, device_id: str, batch_id: str, regionCode: str, **kwargs):
        """
        添加微信联系人
        :param from_username:
        :param type:
        :param alis:
        :param username:
        :param nickname:
        :param conRemark:
        :param smallheadimgurl:
        :param bigheadimgurl:
        :param lastupdatetime:
        :param contactLabel:
        :param create_user_id:
        :param device_id:
        :param batch_id:
        :param regionCode: 地区码
        :return:
        """

        try:
            now_at = arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')

            info = {
                WxContactsModel.contact_id.name: shortuuid.random(12),
                WxContactsModel.type.name: type,
                WxContactsModel.from_username.name: from_username,
                WxContactsModel.alis.name: alis,
                WxContactsModel.username.name: username,
                WxContactsModel.nickname.name: nickname,
                WxContactsModel.conRemark.name: conRemark,
                WxContactsModel.smallheadimgurl.name: smallheadimgurl,
                WxContactsModel.bigheadimgurl.name: bigheadimgurl,
                WxContactsModel.lastupdatetime.name: lastupdatetime,
                WxContactsModel.contactLabel.name: contactLabel,
                WxContactsModel.create_at.name: now_at,
                WxContactsModel.update_at.name: now_at,
                WxContactsModel.create_user_id.name: create_user_id,
                WxContactsModel.device_id.name: device_id,
                WxContactsModel.batch_id.name: batch_id,
                WxContactsModel.regionCode.name: regionCode,
            }

            info_obj = WxContactsModel(**info)

            res = WxContactsModel.save(info_obj)

        except Exception as e:
            if self.log:
                self.log.exception('[add_contact]')
            return False
        return res

    def get_contact(self, from_username, username, fields: list):

        fit = {
            WxContactsModel.from_username.name: from_username,
            WxContactsModel.username.name: username,
        }
        res = WxContactsModel.objects(__raw__=fit).only(*fields).first()
        return res

    def get_contact_by_usernames(self, from_username, usernames, fields: list):

        fit = {
            WxContactsModel.from_username.name: from_username,
            WxContactsModel.username.name: {'$in': usernames},
        }
        res = WxContactsModel.objects(__raw__=fit).only(*fields)
        return res

    def update_contact(self, from_username, username, type: int = None, alis: str = None, nickname: str = None,
                       conRemark: str = None, smallheadimgurl: str = None, bigheadimgurl: str = None,
                       lastupdatetime: int = None, contactLabel: list = None, regionCode: str = None,
                       country: str = None, province: str = None, city: str = None):
        """
        更新联系人信息
        :param from_username:
        :param username:
        :param type:
        :param alis:
        :param nickname:
        :param conRemark:
        :param lastupdatetime:
        :param smallheadimgurl:
        :param bigheadimgurl:
        :param contactLabel:
        :param regionCode:
        :param country:
        :param province:
        :param city:
        :return:
        """
        fit = {
            WxContactsModel.from_username.name: from_username,
            WxContactsModel.username.name: username,
        }

        update = {}
        if type is not None:
            update[WxContactsModel.type.name] = type
        if alis:
            update[WxContactsModel.alis.name] = alis
        if nickname:
            update[WxContactsModel.nickname.name] = nickname
        if conRemark:
            update[WxContactsModel.conRemark.name] = conRemark
        if smallheadimgurl:
            update[WxContactsModel.smallheadimgurl.name] = smallheadimgurl
        if bigheadimgurl:
            update[WxContactsModel.bigheadimgurl.name] = bigheadimgurl
        if lastupdatetime is not None:
            update[WxContactsModel.lastupdatetime.name] = lastupdatetime
        if contactLabel is not None:
            update[WxContactsModel.contactLabel.name] = contactLabel
        if regionCode:
            update[WxContactsModel.regionCode.name] = regionCode
        if country:
            update[WxContactsModel.country.name] = country
        if province:
            update[WxContactsModel.province.name] = province
        if city:
            update[WxContactsModel.city.name] = city

        if update:
            update[WxContactsModel.update_at.name] = arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')

            update_info = {
                "$set": update
            }
            return WxContactsModel.objects(__raw__=fit).update(__raw__=update_info)

        return False

    def add_tel_tag(self, from_username, username, tel):
        """
        添加联系人手机号标签
        :param from_username:
        :param username:
        :param tel:
        :return:
        """
        fit = {
            WxContactsModel.from_username.name: from_username,
            WxContactsModel.username.name: username,
        }

        update_info = {
            "$addToSet": {
                WxContactsModel.contactLabel.name: tel
            },
            "$set": {
                WxContactsModel.update_at.name: arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')
            }
        }
        return WxContactsModel.objects(__raw__=fit).update(__raw__=update_info)

    def get_batch_contacts(self, batch_id, fields: list):
        """
        获取批次联系人
        :param batch_id:
        :param fields:
        :return:
        """
        fit = {
            WxContactsModel.batch_id.name: batch_id,
        }
        res = WxContactsModel.objects(__raw__=fit).only(*fields)
        return res

    def get_all_contacts(self, fields: list):
        """
        获取所有联系人
        :param batch_id:
        :param fields:
        :return:
        """
        fit = {}
        res = WxContactsModel.objects(__raw__=fit).only(*fields)
        return res

    def get_contacts_by_nickname(self, from_username, nickname, fields: list):
        """
        昵称获取医生联系人列表
        :param from_username:
        :param nickname:
        :param fields:
        :return:
        """
        fit = {
            WxContactsModel.from_username.name: from_username,
            WxContactsModel.nickname.name: nickname,
            # WxContactsModel.username.name: {"$regex": BLACK_USERNAME_REGEX}
        }
        res = WxContactsModel.objects(__raw__=fit).only(*fields)
        return res

    def search_contacts(self, from_username, exclude_usernames: list, fields: list, key: str = None,
                        country: str = None, province: str = None,
                        city: str = None, sort: str = '-{}'.format(WxContactsModel.create_at.name),
                        begin: int = 0, limit: int = 10, get_count=False):
        """
        搜索联系人, todo 过滤聊天时间
        :param from_username:
        :param fields:
        :param exclude_usernames: 排除的用户列表
        :param key:
        :param country:
        :param province:
        :param city:
        :param sort:
        :param begin:
        :param limit:
        :param get_count:
        :return:
        """
        fit = {
            WxContactsModel.from_username.name: from_username,
            "$and": [
                {
                    WxContactsModel.username.name: {"$nin": exclude_usernames}
                },
                {
                    # WxContactsModel.username.name: {"$regex": BLACK_USERNAME_REGEX}
                }
            ]

            # WxContactsModel.conRemark.name: {"$ne": ""},

        }
        if key:
            fit['$or'] = [
                {
                    WxContactsModel.nickname.name: re.compile(key, flags=re.IGNORECASE)
                },
                {
                    WxContactsModel.conRemark.name: re.compile(key, flags=re.IGNORECASE)
                },
            ]
        if country:
            fit[WxContactsModel.country.name] = country
        if province:
            fit[WxContactsModel.province.name] = province
        if city:
            fit[WxContactsModel.city.name] = city

        if get_count:
            count = WxContactsModel.objects(__raw__=fit).count()
            return count

        if not limit or int(limit) == 0:
            res = WxContactsModel.objects(__raw__=fit).only(*fields).order_by(sort)
        else:
            res = WxContactsModel.objects(__raw__=fit).only(*fields).order_by(sort).skip(int(begin)).limit(int(limit))

        return res

    def get_contact_by_tel(self, from_username, tel, fields: list):
        """
        手机号获取医生联系人信息
        :param from_username:
        :param tel:
        :param fields:
        :return:
        """
        fit = {
            WxContactsModel.from_username.name: from_username,
            WxContactsModel.contactLabel.name: tel,
        }
        res = WxContactsModel.objects(__raw__=fit).only(*fields).first()
        return res

    def set_last_chat_at(self, from_username, username, last_chat_at):

        fit = {
            WxContactsModel.from_username.name: from_username,
            WxContactsModel.username.name: username,
        }
        update_info = {
            "$set": {
                WxContactsModel.last_chat_at.name: last_chat_at
            }
        }
        return WxContactsModel.objects(__raw__=fit).update(__raw__=update_info)

    def set_add_friend_at(self, from_username, username, add_friend_at):

        fit = {
            WxContactsModel.from_username.name: from_username,
            WxContactsModel.username.name: username,
        }
        update_info = {
            "$set": {
                WxContactsModel.add_friend_at.name: add_friend_at
            }
        }
        return WxContactsModel.objects(__raw__=fit).update(__raw__=update_info)

    def get_no_add_friend_at_contacts(self, from_username: str, fields: list):
        """
        获取无添加好友时间的联系人列表
        :param from_username:
        :param fields:
        :return:
        """
        fit = {
            WxContactsModel.from_username.name: from_username,
            WxContactsModel.add_friend_at.name: {"$exists": False},
        }

        return WxContactsModel.objects(__raw__=fit).only(*fields)

    def agg_doctor_prefix_contacts(self, prefix: str, exclude_usernames: list, from_usernames: list = None):
        """
        统计医生联系人备注名指定前缀的联系人
        :param prefix:
        :param exclude_usernames:
        :param from_usernames:
        :return:
        """

        fit = {
            'conRemark': {"$regex": f"^{prefix}"},
            'username': {
                # "$regex": BLACK_USERNAME_REGEX,
                '$nin': exclude_usernames
            }
        }
        if from_usernames:
            fit[WxContactsModel.from_username.name] = {"$in": from_usernames}

        pipeline = [
            {
                '$match': fit
            },
            {'$group': {
                '_id': "$from_username",
                'username_list': {"$push": "$username"},
                "nickname_list": {'$push': "$nickname"},
                "remark_list": {'$push': "$conRemark"},
                "type_list": {'$push': "$type"}
            }}
        ]
        res = WxContactsModel.objects().aggregate(*pipeline)

        return res

    def get_unfans_users(self, fields: list):
        """
        获取非粉用户列表
        :return:
        """

        fit = {
            WxContactsModel.contactLabel.name: "非粉",
        }

        return WxContactsModel.objects(__raw__=fit).only(*fields)

    def update_region_name(self, contact_id: str, region_msg: dict):
        """
               更新联系人地区编码数据
               :param contact_id:
               :param region_msg:
               :return:
               """
        fit = {
            WxContactsModel.contact_id.name: contact_id,
        }

        update_info = {
            "$set":{
                WxContactsModel.country.name: region_msg.get('country', ''),
                WxContactsModel.province.name: region_msg.get('province', ''),
                WxContactsModel.city.name: region_msg.get('city', ''),
            }
        }
        return WxContactsModel.objects(__raw__=fit).update(__raw__=update_info)

    def get_all_list(self):
        fit = {}
        fields = [WxContactsModel.regionName.name,WxContactsModel.contact_id.name]
        return WxContactsModel.objects(__raw__=fit).only(*fields)