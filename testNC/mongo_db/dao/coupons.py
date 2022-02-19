from typing import List

import shortuuid

from app.mongo_db.model.coupon import CouponModel, DiscountInfoObj, ExtInfoObj, DiscountConditionObj, CouponInfoObj, StockInfoObj, PromoteInfoObj, ReceiveInfoObj, ValidInfoObj, ReceiveObj, \
    UserCouponsModel, UserCouponObj, UserCouponExtInfoObj
from app.util.shop.coupon import CouponItem, UserCouponItem


class CouponDao():

    def __init__(self, log):
        self.log = log

    def add(self, coupon_item: CouponItem):
        """
        添加优惠券

        :param coupon_item:
        :type coupon_item:
        :return:
        :rtype:
        """
        coupon_obj = CouponModel()
        try:
            coupon_obj.coupon_id = coupon_item.coupon_id
            coupon_obj.type = coupon_item.type
            coupon_obj.status = coupon_item.status
            coupon_obj.update_time = coupon_item.update_time
            coupon_obj.create_time = coupon_item.create_time

            if coupon_item.stock_info:
                coupon_obj.stock_info = StockInfoObj(**coupon_item.stock_info)

            # 优惠券具体信息
            coupon_info = coupon_item.coupon_info
            if coupon_info:
                coupon_obj.coupon_info = CouponInfoObj(
                    name=coupon_info.get("name", None),
                    ext_info=ExtInfoObj(**coupon_info.get("ext_info", None)),
                    promote_info=PromoteInfoObj(**coupon_info.get("promote_info", None)),
                    receive_info=ReceiveInfoObj(**coupon_info.get("receive_info", None)),
                    valid_info=ValidInfoObj(**coupon_info.get("valid_info", None)),
                )
                if coupon_item.get("receives", None):
                    coupon_obj.receives = [ReceiveObj(**receive) for receive in coupon_item.get("receives", [])]

                discount_info = coupon_info.get("discount_info", None)
                if discount_info:
                    discount_condition = discount_info.get("discount_condition", None)
                    coupon_obj.coupon_info.discount_info = DiscountInfoObj(
                        discount_fee=discount_info.get("discount_fee", None),
                        discount_num=discount_info.get("discount_num", None)  # 换算规则，5000=5折，7000=7折，范围是1000-10000，必须是100的
                    )
                    if discount_condition:
                        coupon_obj.coupon_info.discount_info.discount_condition = DiscountConditionObj(**discount_condition)

            res = coupon_obj.save()
        except Exception as e:
            if self.log:
                self.log.exception('[CouponDao.add],[fail],[coupon_item:{}]'.format(coupon_item))
            return False
        return res

    def update(self, coupon_id: int, coupon_item: CouponItem):
        """
        更新优惠券

        :param coupon_item:
        :type coupon_item:
        :param coupon_id:
        :type coupon_id:
        :return:
        :rtype:
        """
        fit = {
            CouponModel.coupon_id.name: int(coupon_id)
        }
        update_info = {
            "$set": coupon_item
        }
        try:
            res = CouponModel.objects(__raw__=fit).update(__raw__=update_info)
        except Exception as e:
            self.log.exception("[CouponDao.update],[fail],[coupon_id]:{},coupon_item:{}]".format(coupon_id, coupon_item))
            return False
        return res

    def get_recyclable_coupons_by_coupon_ids(self, coupon_ids: List[int], fields: list):
        '''
        通过优惠券ID获取可回收的优惠券,
        条件是，可回收值大于0且回收时间为空

        :param coupon_ids:
        :param fields:
        :return:
        '''
        res = []
        if not coupon_ids:
            return res

        try:
            fit = {
                CouponModel.coupon_id.name: {"$in": [int(c_id) for c_id in coupon_ids]},
                CouponModel.receives.name: {
                    '$elemMatch': {
                        ReceiveObj.recyclable_val.name: {"$gt": 0},
                        ReceiveObj.receive_at.name: {"$ne": None},
                    }
                }
            }
            res = CouponModel.objects(__raw__=fit).only(*fields)
        except Exception as e:
            self.log.exception("[CouponDao.get_recieiveable_coupons_by_coupon_ids][coupon_id]:{}]".format(coupon_ids))
            return False
        return res

    def get_by_coupon_ids(self, coupon_ids: List[int], fields: list):
        '''
        批量获取优惠券
        :param coupon_ids:
        :param fields:
        :return:
        '''

        res = []
        if not coupon_ids:
            return res

        try:
            fit = {
                CouponModel.coupon_id.name: {"$in": [int(c_id) for c_id in coupon_ids]}
            }
            res = CouponModel.objects(__raw__=fit).only(*fields)
        except Exception as e:
            self.log.exception("[CouponDao.get_by_coupon_ids][coupon_id]:{}]".format(coupon_ids))
            return False
        return res

    def get_by_coupon_id(self, coupon_id: int, fields: List):
        """
        获取优惠券

        :param fields:
        :type fields:
        :param coupon_id:
        :type coupon_id:
        :return:
        :rtype:
        """
        fit = {
            CouponModel.coupon_id.name: int(coupon_id)
        }
        try:
            res = CouponModel.objects(__raw__=fit).only(*fields).first()
        except Exception as e:
            self.log.exception("[CouponDao.get_by_coupon_id],[fail],[coupon_id]:{}]".format(coupon_id))
            return False
        return res

    def get_not_auto_at_by_coupon_id(self, coupon_id: int, fields: List):
        """
        获取未进行过自动退款的优惠券

        :param fields:
        :type fields:
        :param coupon_id:
        :type coupon_id:
        :return:
        :rtype:
        """
        fit = {
            CouponModel.coupon_id.name: int(coupon_id),
            "{}.{}".format(CouponModel.receives.name, ReceiveObj.overdue_auto_at.name): {
                "$in": [None, '']
            }
        }
        try:
            res = CouponModel.objects(__raw__=fit).only(*fields).first()
        except Exception as e:
            self.log.exception("[CouponDao.get_not_auto_at_by_coupon_id],[fail],[coupon_id]:{}]".format(coupon_id))
            return False
        return res

    def get_max_update_time(self):
        """
        获取优惠券最大更新时间

        :return:
        :rtype:
        """
        fit = {
            "{}.{}".format(CouponModel.receives.name, ReceiveObj.overdue_auto_at.name): {
                "$in": [None, '']
            }
        }
        fields = [CouponModel.update_time.name]
        res = ""
        sort = "-{}.{}".format(CouponModel.receives.name, ReceiveObj.overdue_auto_at.name)
        try:
            res = CouponModel.objects(__raw__=fit).only(*fields).order_by(sort).first()
            if res:
                return res.update_time
        except:
            self.log.exception('[CouponDao.get_max_update_time]')
        return res

    def update_receive(self, coupon_id: int, user_id, open_id, create_at, receive_at):
        """
        更新用户领用记录

        :param coupon_id:
        :type coupon_id:
        :param user_id:
        :type user_id:
        :param open_id:
        :type open_id:
        :param create_at:
        :type create_at:
        :param receive_at:
        :type receive_at:
        :return:
        :rtype:
        """
        fit = {
            CouponModel.coupon_id.name: coupon_id,
        }
        update_info = {
            "$addToSet": {
                CouponModel.receives.name: {
                    f'{ReceiveObj.user_id.name}': user_id,
                    f'{ReceiveObj.open_id.name}': open_id,
                    f'{ReceiveObj.create_at.name}': create_at,
                    f'{ReceiveObj.receive_at.name}': receive_at,
                    f'{ReceiveObj.receive_id.name}': f"cr_{shortuuid.random(10)}",
                }
            }
        }
        res = None
        try:
            res = CouponModel.objects(__raw__=fit).update(__raw__=update_info)
        except:
            self.log.exception('[CouponDao.update_receive]')
        return res

    def get_receive(self, coupon_id: int, user_id, fields: List):
        """
        获取领用信息

        :param fields:
        :type fields:
        :param coupon_id:
        :type coupon_id:
        :param user_id:
        :type user_id:
        :return:
        :rtype:
        """
        fit = {
            CouponModel.coupon_id.name: coupon_id,
            f"{CouponModel.receives.name}.{ReceiveObj.user_id.name}": user_id,
        }
        res = None
        try:
            res = CouponModel.objects(__raw__=fit).only(*fields)
        except:
            self.log.exception('[CouponDao.update_receive]')
        return res

    def update_recyclable_at(self, coupon_id: int, receive_id: str, receive_at: str):
        '''
        更新某个张优惠券的回收时间，表明其已被回收。
        :param receive_id:
        :param receive_at:  [str]2020-12-23 12:34:56
        :return:
        '''

        res = None
        try:
            cond = {
                CouponModel.coupon_id.name: int(coupon_id),
                f"{CouponModel.receives.name}.{ReceiveObj.receive_id.name}": receive_id
            }

            update_info = {
                "$set": {
                    f"{CouponModel.receives.name}.$.{ReceiveObj.receive_at.name}": receive_at
                }
            }
            res = CouponModel.objects(__raw__=cond).update(__raw__=update_info)
        except:
            self.log.exception(f'[CouponDao.update_recyclable_at][coupon_id:{coupon_id}, receive_id:{receive_id}, '
                               f'receive_at:{receive_at}]')
        return res

    def update_recyclable_val(self, coupon_id: int, open_id, val, order_id):
        """
        更新某个人某张优惠券的可回收余额

        :param coupon_id:
        :type coupon_id:
        :param open_id:
        :type open_id:
        :param val:
        :type val:
        :param order_id:
        :type order_id:
        :return:
        :rtype:
        """

        fit = {
            CouponModel.coupon_id.name: coupon_id,
            CouponModel.receives.name: {
                "$elemMatch": {
                    ReceiveObj.open_id.name: open_id,
                    ReceiveObj.order_id.name: order_id
                }
            }
        }

        update_info = {
            "$set": {
                f"{CouponModel.receives.name}.$.{ReceiveObj.recyclable_val.name}": val
            }
        }
        res = None
        try:
            res = CouponModel.objects(__raw__=fit).update(__raw__=update_info)
        except:
            self.log.exception('[CouponDao.update_recyclable_val]')
        return res

    def update_coupon_order_id(self, coupon_id: int, order_id, openid):
        """
        更新后台创建的 订单的order_id 信息

        :param openid:
        :type openid:
        :param coupon_id:
        :type coupon_id:
        :param order_id:
        :type order_id:
        :return:
        :rtype:
        """

        fit = {
            CouponModel.coupon_id.name: coupon_id,
            f"{CouponModel.receives.name}.{ReceiveObj.open_id.name}": openid,
        }

        update_info = {
            "$set": {
                f"{CouponModel.receives.name}.$.{ReceiveObj.order_id.name}": order_id
            }
        }
        res = None
        try:
            res = CouponModel.objects(__raw__=fit).update(__raw__=update_info)
        except:
            self.log.exception('[CouponDao.update_coupon_order_id]')
        return res

    def get_overdue_coupon_ids(self, start_create_time, end_create_time, fields: List):
        """
        获取过期优惠券

        :param fields:
        :type fields:
        :param start_create_time:
        :type start_create_time:
        :param end_create_time:
        :type end_create_time:
        :return:
        :rtype:
        """

        fit = {
            CouponModel.status.name: CouponModel.STATUS_BE_OVERDUE,
            CouponModel.create_time.name: {
                "$gte": start_create_time,
                "$lte": end_create_time
            }
        }
        res = CouponModel.objects(__raw__=fit).only(*fields)
        return res

    def get_rec_coupon_openids(self, start_create_time, end_create_time, begin, limit) -> List:
        """
        获取已领取的优惠券的用户openid

        :param limit:
        :type limit:
        :param begin:
        :type begin:
        :param start_create_time:
        :type start_create_time:
        :param end_create_time:
        :type end_create_time:
        :return: [opeid,.....]
        :rtype:
        """
        begin = int(begin)
        limit = int(limit)
        fit = {
            CouponModel.create_time.name: {
                "$gte": start_create_time,
                "$lte": end_create_time
            },
            CouponModel.receives.name: {"$exists": True},
        }
        pipeline = [
            {"$match": fit},
            {"$unwind": "${}".format(CouponModel.receives.name)},
            {"$group": {"_id": {"openid": '${}.{}'.format(CouponModel.receives.name,ReceiveObj.open_id.name)}}},
            {"$skip": begin},
            {"$limit": limit}]
        open_ids = []
        try:
            res = CouponModel.objects.aggregate(*pipeline)
            for item in res:
                if item:
                    open_ids.append(item.get("_id",{}).get("openid",''))

        except Exception as e:
            self.log.exception("[CouponDao.get_rec_coupon_openids_fail][start_create_time:{},end_create_time:{},begin:{},limit:{}]"
                               .format(start_create_time,end_create_time,begin,limit))
        return open_ids

    def update_overdue_auto_at(self, coupon_id: int, receive_id: str, overdue_auto_at: str, overdue_auto_val: int):
        '''
        更新某个张优惠券的自动过期 回收时间,返还金额，表明其已被过期自动回收。

        :param overdue_auto_val:
        :type overdue_auto_val:
        :param overdue_auto_at:
        :type overdue_auto_at:
        :param coupon_id:
        :type coupon_id:
        :param receive_id:
        :param overdue_auto_at:  [str]2020-12-23 12:34:56
        :return:
        '''

        res = None
        try:
            cond = {
                CouponModel.coupon_id.name: int(coupon_id),
                f"{CouponModel.receives.name}.{ReceiveObj.receive_id.name}": receive_id
            }

            update_info = {
                "$set": {
                    f"{CouponModel.receives.name}.$.{ReceiveObj.overdue_auto_at.name}": overdue_auto_at,
                    f"{CouponModel.receives.name}.$.{ReceiveObj.overdue_auto_val.name}": overdue_auto_val
                }
            }
            res = CouponModel.objects(__raw__=cond).update(__raw__=update_info)
        except:
            self.log.exception(f'[CouponDao.update_overdue_auto_at][coupon_id:{coupon_id}, receive_id:{receive_id}, '
                               f'receive_at:{overdue_auto_at}]')
        return res


class UserCouponDao():

    def __init__(self, log):
        self.log = log

    def add(self, user_coupons: List[UserCouponItem], openid: str):
        """
        添加用户优惠券

        :param openid:
        :type openid:
        :param user_coupons:
        :type user_coupons:
        :return:
        :rtype:
        """
        user_coupons_obj = UserCouponsModel()
        try:
            user_coupons_obj.openid = openid
            user_coupons_obj.coupons = [
                UserCouponObj(
                    coupon_id=user_coupon.coupon_id,
                    status=user_coupon.status,
                    create_time=user_coupon.create_time,
                    update_time=user_coupon.update_time,
                    start_time=user_coupon.start_time,
                    end_time=user_coupon.end_time,
                    order_id=user_coupon.order_id,
                    discount_fee=user_coupon.discount_fee,
                    ext_info=UserCouponExtInfoObj(
                        use_time=user_coupon.ext_info.get("use_time", None)
                    ) if user_coupon.ext_info else None
                )
                for user_coupon in user_coupons]

            res = user_coupons_obj.save()
        except Exception as e:
            if self.log:
                self.log.exception('[CouponDao.add],[fail],[coupon_item:{},openid:{}]'.format(user_coupons, openid))
            return False
        return res
