__author__ = 'xiaozc'

from typing import List

import arrow
import shortuuid

from test_beast.mongo_db.model.user_coin_records import UserCoinRecordsModel


class UserCoinRecordsDao():

    def __init__(self, log):
        self.log = log
        self.collection = 'user_coin_records'

    def add_coin(self, user_id: str, coin_type: str, coin: int, from_at: str,now_date:str):
        """
        添加健康币
        :param user_id:
        :param coin_type:
        :param coin:
        :param from_at:
        :return:
        """
        try:

            # now = arrow.now(tz='+08:00').format('YYYY-MM-DD HH:mm:ss')
            data = {
                UserCoinRecordsModel.record_id.name: 'r_{}'.format(shortuuid.random(12)),
                UserCoinRecordsModel.coin_type.name: coin_type,
                UserCoinRecordsModel.user_id.name: user_id,
                UserCoinRecordsModel.coin.name: int(coin),
                UserCoinRecordsModel.from_at.name: from_at,
                UserCoinRecordsModel.status.name: UserCoinRecordsModel.COIN_STATUS_NORMAL,
                UserCoinRecordsModel.create_at.name: now_date,
            }
            data_obj = UserCoinRecordsModel(**data)
            res = UserCoinRecordsModel.save(data_obj)

        except Exception as e:
            if self.log:
                self.log.exception('[add_coin]')
            return False
        return res

    def get_coin_total(self, user_id: str):
        """
        获取用户总积分

        """
        coin_total = 0
        fit = {
            UserCoinRecordsModel.user_id.name: user_id,
            UserCoinRecordsModel.status.name: UserCoinRecordsModel.COIN_STATUS_NORMAL,
        }
        pipeline = [
            {
                '$group': {
                    "_id": "${}".format(UserCoinRecordsModel.user_id.name),
                    "sum": {"$sum": "${}".format(UserCoinRecordsModel.coin.name)},
                }
            }
        ]

        data = UserCoinRecordsModel.objects(__raw__=fit).aggregate(*pipeline)
        if data:
            data = list(data)
            coin_total = data[0]['sum'] if len(data) > 0 else 0

        return coin_total

    def get_coin_records(self, begin: int, limit: int, user_id: str, fields: List):
        """
        获取健康币记录

        """
        fit = {
            UserCoinRecordsModel.user_id.name: user_id
        }
        begin = int(begin)
        limit = int(limit)

        res = UserCoinRecordsModel.objects(__raw__=fit).only(*fields).skip(begin).limit(limit)

        return res

    def get_user_sign_in(self, user_id: str, start_date: str, end_date: str,fields: List):
        """
        获取用户某一段时间的签到记录
        :param user_id:
        :param start_date:
        :param end_date:
        :param fields:
        :return:
        """

        fit = {
            UserCoinRecordsModel.user_id.name: user_id,
            UserCoinRecordsModel.create_at.name:{
                "$gte":start_date, "$lte": end_date
            }
        }
        sort = '-create_at'

        res = UserCoinRecordsModel.objects(__raw__=fit).only(*fields).order_by(sort)

        return res
