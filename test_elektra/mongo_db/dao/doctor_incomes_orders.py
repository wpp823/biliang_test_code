__author__ = 'xiaozc'

import random

import arrow

# from mongo_db.model.doctor_incomes_orders import DoctorIncomesOrdersModel, ProductDataObj
from test_elektra.mongo_db.model.doctor_incomes_orders import *



__author__ = 'xiaozc'

class DoctorIncomesOrdersDao():
    # 医生收益订单

    def __init__(self, log):
        self.log = log
        self.collection = 'doctor_incomes_orders'

    def add_incomes_order(self, order_type: str, from_order_id: str, from_order_pay_at: str, from_doctor_id: str,
                          partner_id: str, agent_id: str,
                          doctor_id: str, user_id: str, desc: str, cost: int, note_id: str, thread_id: str,
                          transfer_status: str, product_data: dict = None, award_code: str = None):
        """
        添加收益订单
        @param order_type:
        @param from_order_id:
        @param from_order_pay_at::
        @param from_doctor_id:
        @param partner_id:
        @param agent_id:
        @param doctor_id:
        @param user_id:
        @param desc:
        @param cost:
        @param note_id:
        @param thread_id:
        @param transfer_status:
        @param product_data:
        @param award_code:
        @return:
        """
        try:

            now = arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')
            info = {
                DoctorIncomesOrdersModel.incomes_order_id.name: '{}{}'.format(arrow.now(tz='+08:00').strftime('%Y%m%d%H%M%S%f'), random.randint(1000, 9999)),
                DoctorIncomesOrdersModel.order_type.name: order_type,
                DoctorIncomesOrdersModel.from_order_id.name: from_order_id,
                DoctorIncomesOrdersModel.from_order_pay_at.name: from_order_pay_at,
                DoctorIncomesOrdersModel.from_doctor_id.name: from_doctor_id,
                DoctorIncomesOrdersModel.partner_id.name: partner_id,
                DoctorIncomesOrdersModel.agent_id.name: agent_id,
                DoctorIncomesOrdersModel.doctor_id.name: doctor_id,
                DoctorIncomesOrdersModel.user_id.name: user_id,
                DoctorIncomesOrdersModel.desc.name: desc,
                DoctorIncomesOrdersModel.cost.name: cost,
                DoctorIncomesOrdersModel.note_id.name: note_id,
                DoctorIncomesOrdersModel.thread_id.name: thread_id,
                DoctorIncomesOrdersModel.transfer_status.name: transfer_status,
                DoctorIncomesOrdersModel.create_at.name: now,
                DoctorIncomesOrdersModel.update_at.name: now,
            }
            if product_data:
                info[DoctorIncomesOrdersModel.product_data.name] = ProductDataObj(**product_data)

            if award_code:
                info[DoctorIncomesOrdersModel.award_code.name] = award_code

            info_obj = DoctorIncomesOrdersModel(**info)

            res = DoctorIncomesOrdersModel.save(info_obj)

        except Exception as e:
            if self.log:
                self.log.exception('[add_incomes_order]')
            return False
        return res

    def get_doctor_pending_orders(self, doctor_id: str, fields: list):
        """
        获取医生所有待付款收益订单
        @param doctor_id:
        @param fields:
        @return:
        """
        fit = {
            DoctorIncomesOrdersModel.doctor_id.name: doctor_id,
            DoctorIncomesOrdersModel.transfer_status.name: DoctorIncomesOrdersModel.TRANSFER_STATUS_PENDING
        }

        res = DoctorIncomesOrdersModel.objects(__raw__=fit).only(*fields)
        return res


    def set_orders_withdrawal(self, income_order_ids: list):
        """
        批量设置订单提现
        @param income_order_ids:
        @param payment_data:
        @return:
        """

        fit = {
            DoctorIncomesOrdersModel.incomes_order_id.name: {'$in': income_order_ids},
            DoctorIncomesOrdersModel.transfer_status.name: DoctorIncomesOrdersModel.TRANSFER_STATUS_PENDING
        }

        update_data = {
            DoctorIncomesOrdersModel.transfer_status.name: DoctorIncomesOrdersModel.TRANSFER_STATUS_WITHDRAWAL,
            DoctorIncomesOrdersModel.update_at.name: arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')
        }

        update_info = {
            '$set': update_data
        }

        return DoctorIncomesOrdersModel.objects(__raw__=fit).update(__raw__=update_info)

    def set_orders_success(self, income_order_ids: list, transfer_type: str, payment_data: dict):
        """
        批量设置订单成功付款
        @param income_order_ids:
        @param payment_data:
        @return:
        """

        fit = {
            DoctorIncomesOrdersModel.incomes_order_id.name: {'$in': income_order_ids},
            DoctorIncomesOrdersModel.transfer_status.name: DoctorIncomesOrdersModel.TRANSFER_STATUS_WITHDRAWAL
        }

        update_data = {
            DoctorIncomesOrdersModel.transfer_status.name: DoctorIncomesOrdersModel.TRANSFER_STATUS_SUCCESS,
            DoctorIncomesOrdersModel.transfer_type.name: transfer_type,
            DoctorIncomesOrdersModel.payment_data.name: payment_data,
            DoctorIncomesOrdersModel.update_at.name: arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')
        }

        update_info = {
            '$set': update_data
        }

        return DoctorIncomesOrdersModel.objects(__raw__=fit).update(__raw__=update_info)


    def get_doctor_orders(self, doctor_id, fields: list, transfer_status: str or list = None,
                          sort='-{}'.format(DoctorIncomesOrdersModel.create_at.name), begin=0, limit=0, get_count=False):
        """
        获取医生收益订单列表
        @param doctor_id:
        @param fields:
        @param transfer_status:
        @param sort:
        @param begin:
        @param limit:
        @param get_count:
        @return:
        """

        fit = {
            DoctorIncomesOrdersModel.doctor_id.name: doctor_id,
        }
        if transfer_status:
            if isinstance(transfer_status, list):
                fit[DoctorIncomesOrdersModel.transfer_status.name] = {'$in': transfer_status}
            else:
                fit[DoctorIncomesOrdersModel.transfer_status.name] = transfer_status

        if get_count:
            return DoctorIncomesOrdersModel.objects(__raw__=fit).count()

        sort_list = [sort, '-id']
        if int(limit) == 0:
            res = DoctorIncomesOrdersModel.objects(__raw__=fit).only(*fields).order_by(*sort_list)
        else:
            res = DoctorIncomesOrdersModel.objects(__raw__=fit).only(*fields).order_by(*sort_list).skip(int(begin)).limit(int(limit))

        return res

    def get_doctor_order_cost_total(self, doctor_id,  transfer_status: str or list = None):
        """
        获取医生收益总数
        @param doctor_id:
        @param transfer_status: 转帐状态
        @return:
        """

        fit = {
            DoctorIncomesOrdersModel.doctor_id.name: doctor_id,
        }
        if transfer_status:
            if isinstance(transfer_status, list):
                fit[DoctorIncomesOrdersModel.transfer_status.name] = {'$in': transfer_status}
            else:
                fit[DoctorIncomesOrdersModel.transfer_status.name] = transfer_status

        pipeline = [
            {'$match': fit},
            {
                '$group': {
                    '_id': "cost",
                    "total": {
                        "$sum": "$cost"
                    },
                }
            },
        ]

        res = DoctorIncomesOrdersModel.objects().aggregate(*pipeline)
        total = 0
        if res:
            for data in res:
                total = data['total']
                break
        return total

    def get_by_product_order_id(self, from_order_id: str, fields: list, get_refund: bool = False):
        """
        根据产品订单获取数据
        @param from_order_id:
        @param fields:
        @param get_refund: 获取退款订单
        @return:
        """
        fit = {
            DoctorIncomesOrdersModel.order_type.name: DoctorIncomesOrdersModel.ORDER_TYPE_PRODUCT,
            DoctorIncomesOrdersModel.from_order_id.name: from_order_id
        }
        if get_refund:
            fit[DoctorIncomesOrdersModel.cost.name] = {"$lt": 0}

        res = DoctorIncomesOrdersModel.objects(__raw__=fit).only(*fields).first()
        return res


    def set_product_order_transfer_status(self, from_order_id: str, transfer_status: str):
        """
        设置产品推荐收益单状态
        @param from_order_id:
        @param transfer_status:
        @param product_price:
        @param cost:
        @return:
        """
        fit = {
            DoctorIncomesOrdersModel.order_type.name: DoctorIncomesOrdersModel.ORDER_TYPE_PRODUCT,
            DoctorIncomesOrdersModel.from_order_id.name: from_order_id
        }

        update_data = {
            DoctorIncomesOrdersModel.transfer_status.name: transfer_status,
            DoctorIncomesOrdersModel.update_at.name: arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')
        }

        update_info = {
            '$set': update_data
        }

        return DoctorIncomesOrdersModel.objects(__raw__=fit).update(__raw__=update_info)


    def get_doctor_fans_product_orders(self, doctor_id, user_id, fields: list, transfer_status: str or list = None,
                                       begin_at=None, end_at=None, sort='-{}'.format(DoctorIncomesOrdersModel.create_at.name),
                                       begin=0, limit=0, get_count=False):
        """
        获取医生收益订单列表
        @param doctor_id:
        @param user_id:
        @param fields:
        @param transfer_status:
        @param begin_at:
        @param end_at:
        @param sort:
        @param begin:
        @param limit:
        @param get_count:
        @return:
        """

        fit = {
            DoctorIncomesOrdersModel.doctor_id.name: doctor_id,
            DoctorIncomesOrdersModel.user_id.name: user_id,
            DoctorIncomesOrdersModel.order_type.name: DoctorIncomesOrdersModel.ORDER_TYPE_PRODUCT,
        }
        if transfer_status:
            if isinstance(transfer_status, list):
                fit[DoctorIncomesOrdersModel.transfer_status.name] = {'$in': transfer_status}
            else:
                fit[DoctorIncomesOrdersModel.transfer_status.name] = transfer_status

        if begin_at:
            # 转字符串
            begin_at_str = arrow.get(begin_at).replace(tzinfo='+08:00').format('YYYY-MM-DD HH:mm:ss')
            fit[DoctorIncomesOrdersModel.create_at.name] = {'$gte': begin_at_str}
            if end_at:
                end_at_str = arrow.get(end_at).shift(days=1).replace(tzinfo='+08:00').format('YYYY-MM-DD HH:mm:ss')
                fit[DoctorIncomesOrdersModel.create_at.name].update({'$lt': end_at_str})

        if get_count:
            return DoctorIncomesOrdersModel.objects(__raw__=fit).count()

        if int(limit) == 0:
            res = DoctorIncomesOrdersModel.objects(__raw__=fit).only(*fields).order_by(sort)
        else:
            res = DoctorIncomesOrdersModel.objects(__raw__=fit).only(*fields).order_by(sort).skip(int(begin)).limit(int(limit))

        return res

    def get_doctor_user_product_price_total(self, doctor_id: str, user_id: str, begin_at: str, end_at: str):
        """
        获取医生某锁客用户健康建议销售额总数
        @param doctor_id:
        @param user_id:
        @param begin_at:
        @param end_at:
        @return:
        """
        fit = {
            DoctorIncomesOrdersModel.doctor_id.name: doctor_id,
            DoctorIncomesOrdersModel.user_id.name: user_id,
            DoctorIncomesOrdersModel.order_type.name: DoctorIncomesOrdersModel.ORDER_TYPE_PRODUCT,
            DoctorIncomesOrdersModel.transfer_status.name: {'$in': [DoctorIncomesOrdersModel.TRANSFER_STATUS_PENDING,
                                                                    DoctorIncomesOrdersModel.TRANSFER_STATUS_WITHDRAWAL,
                                                                    DoctorIncomesOrdersModel.TRANSFER_STATUS_SUCCESS]},
            DoctorIncomesOrdersModel.create_at.name: {"$lt": end_at}
        }
        if begin_at:
            fit[DoctorIncomesOrdersModel.create_at.name]["$gte"] = begin_at

        pipeline = [
            {'$match': fit},
            {
                '$group': {
                    '_id': "price_total",
                    "total": {
                        "$sum": "$product_data.product_price"
                    },
                }
            },
        ]

        res = DoctorIncomesOrdersModel.objects().aggregate(*pipeline)
        total = 0
        if res:
            for data in res:
                total = data['total']
                break
        return total


    def agg_user_doctor_product_price_total(self, user_id: str, begin_at: str, end_at: str, include_doctor_ids: list = None):
        """
        统计某用户所有医生健康建议销售额总数
        @param user_id:
        @param begin_at:
        @param end_at:
        @param include_doctor_ids: 指定的医生id列表
        @return:
        """
        fit = {
            DoctorIncomesOrdersModel.user_id.name: user_id,
            DoctorIncomesOrdersModel.order_type.name: DoctorIncomesOrdersModel.ORDER_TYPE_PRODUCT,
            DoctorIncomesOrdersModel.transfer_status.name: {'$in': [DoctorIncomesOrdersModel.TRANSFER_STATUS_PENDING,
                                                                    DoctorIncomesOrdersModel.TRANSFER_STATUS_WITHDRAWAL,
                                                                    DoctorIncomesOrdersModel.TRANSFER_STATUS_SUCCESS]},
            DoctorIncomesOrdersModel.create_at.name: {"$lt": end_at}
        }
        if begin_at:
            fit[DoctorIncomesOrdersModel.create_at.name]["$gte"] = begin_at

        if include_doctor_ids:
            fit[DoctorIncomesOrdersModel.doctor_id.name] = {"$in": include_doctor_ids}

        pipeline = [
            {'$match': fit},
            {"$sort": {DoctorIncomesOrdersModel.create_at.name: 1}},
            {
                '$group': {
                    '_id': {
                        'doctor_id': "$doctor_id"
                    },
                    "total": {
                        "$sum": "$product_data.product_price"
                    },
                    "create_at": {"$first": "$create_at"}
                }
            },
            {"$sort": {'total': -1}},
        ]

        res = DoctorIncomesOrdersModel.objects().aggregate(*pipeline)
        return res


    def get_doctor_product_order_count(self, doctor_id,  begin_at: str, end_at: str, is_first: bool = None):
        """
        获取医生商品收益订单数
        @param doctor_id:
        @param begin_at:
        @param end_at:
        @param is_first:
        @return:
        """

        fit = {
            DoctorIncomesOrdersModel.doctor_id.name: doctor_id,
            DoctorIncomesOrdersModel.order_type.name: DoctorIncomesOrdersModel.ORDER_TYPE_PRODUCT,
            DoctorIncomesOrdersModel.cost.name: {'$gt': 0},
            DoctorIncomesOrdersModel.create_at.name: {
                "$gte": begin_at,
                "$lte": end_at
            }
        }
        if isinstance(is_first, bool):
            fit['{}.{}'.format(DoctorIncomesOrdersModel.product_data.name, ProductDataObj.is_first.name)] = is_first

        count = DoctorIncomesOrdersModel.objects(__raw__=fit).count()
        return count


    def agg_users_product_order_count(self,  user_ids: list):
        """
        统计用户商品收益订单数
        @param doctor_id:
        @param user_ids:
        @return:
        """

        fit = {
            DoctorIncomesOrdersModel.order_type.name: DoctorIncomesOrdersModel.ORDER_TYPE_PRODUCT,
            DoctorIncomesOrdersModel.cost.name: {'$gt': 0},
            DoctorIncomesOrdersModel.user_id.name: {"$in": user_ids}
        }

        pipeline = [
            {'$match': fit},
            {
                '$group': {
                    "_id": "$user_id",
                    "count": {"$sum":1}
                }
            },
        ]

        res = DoctorIncomesOrdersModel.objects().aggregate(*pipeline)
        return list(res) if res else []


    def agg_doctor_product_order_day_statis(self,  doctor_id: str, begin_at: str, end_at: str, is_first: bool = None):
        """
        统计用户商品收益订单数
        @param doctor_id:
        @param begin_at:
        @param end_at:
        @param is_first:    是否首购
        @return:
        """

        fit = {
            DoctorIncomesOrdersModel.doctor_id.name: doctor_id,
            DoctorIncomesOrdersModel.order_type.name: DoctorIncomesOrdersModel.ORDER_TYPE_PRODUCT,
            DoctorIncomesOrdersModel.cost.name: {'$gt': 0},
            DoctorIncomesOrdersModel.create_at.name: {
                "$gte": begin_at,
                "$lte": end_at
            }
        }
        if isinstance(is_first, bool):
            fit['{}.{}'.format(DoctorIncomesOrdersModel.product_data.name, ProductDataObj.is_first.name)] = is_first


        pipeline = [
            {'$match': fit},
            {
                "$group": {
                    "_id": {
                        "day": {
                            "$dateToString": {
                                "format": "%Y-%m-%d",
                                "date": {"$toDate": "$create_at"}
                            }
                        }
                    },
                    "count": {"$sum": 1},
                }
            }
        ]

        res = DoctorIncomesOrdersModel.objects().aggregate(*pipeline)

        return res



    def get_product_order(self):
        """
        获取订单数据
        :return:
        """
        fit = {
            DoctorIncomesOrdersModel.order_type.name: DoctorIncomesOrdersModel.ORDER_TYPE_PRODUCT
        }
        order_fields = [DoctorIncomesOrdersModel.product_data.name]
        res = DoctorIncomesOrdersModel.objects(__raw__=fit).only(*order_fields)
        return res

    def update_order_is_first(self, wx_order_id, is_first):
        """
        更新是否是首单

        :param wx_order_id:
        :param is_first:
        :return:
        """

        fit = {
            f"{DoctorIncomesOrdersModel.product_data.name}.{ProductDataObj.order_id.name}": wx_order_id
        }
        upd_info = {
            "$set": {
                f"{DoctorIncomesOrdersModel.product_data.name}.{ProductDataObj.is_first.name}": is_first
            }
        }

        res = DoctorIncomesOrdersModel.objects(__raw__=fit).update(__raw__=upd_info)
        return res
