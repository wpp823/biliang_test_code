import logging
import os
from logging.handlers import TimedRotatingFileHandler

import arrow
from mongoengine import register_connection, connection

from conf.user_coin_conf import COIN_SIGN_IN_CONFIG
from test_beast.mongo_db.dao.user_coin_records import UserCoinRecordsDao


def get_logger(name, log_path='/var/log', level=logging.INFO):
    log_format = '%(asctime)s - %(name)s:%(filename)s:%(lineno)d - %(levelname)s - %(message)s'

    logger = logging.getLogger(name)
    logger.setLevel(level)
    if logger.handlers:
        # or else, as I found out, we keep adding handlers and duplicate messages
        pass
    else:
        if not os.path.exists(log_path):
            os.mkdir(log_path)

        file_log_path = os.path.join(log_path, name)

        trf_param = {
            "filename": file_log_path,
            "when": 'MIDNIGHT',
            "encoding": "utf8"
        }

        file_handle = logging.handlers.TimedRotatingFileHandler(**trf_param)
        file_handle.setLevel(level)
        formatter = logging.Formatter(log_format)
        file_handle.setFormatter(formatter)
        logger.addHandler(file_handle)
        # 输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        logger.addHandler(ch)

    return logger


def add_test_coin(user_id: str, coin_type: str, coin: int, from_at: str, now_date: str):
    log = get_logger(name='test_beast', log_path='./')
    user_coin_rec_dao = UserCoinRecordsDao(log=log)
    try:
        res = user_coin_rec_dao.add_coin(user_id=user_id, coin_type=coin_type, coin=coin, from_at=from_at, now_date=now_date)

        if res:
            log.info(f"add_coin_ok :{user_id},{coin_type},{coin}")
        else:
            log.error(f"add_fail:{user_id},{coin_type},{coin}")
    except:
        log.exception("add_test_coin")


if __name__ == "__main__":
    MONGO_DB_NAME = 'beast'
    MONGO_HOST_PART = "mongodb://root:Pzzh4Admin@192.168.1.230"
    MONGO_HOST_AUTH_DB = "admin"
    MONGO_HOST_REPLICA_SET = None

    register_connection(db=MONGO_DB_NAME, host=MONGO_HOST_PART, authentication_source=MONGO_HOST_AUTH_DB, replicaset=None, alias=connection.DEFAULT_CONNECTION_NAME)

    # log = get_logger(name='tes_beast.log', log_path='./', )

    test_user_id = 'u_4rB4zX6Fag'
    test_coin_type = 'sign_in'
    test_coin = COIN_SIGN_IN_CONFIG
    test_from_at = 'test_python'
    now = arrow.now(tz='+08:00').shift(days=-33).format('YYYY-MM-DD HH:mm:ss')
    add_test_coin(user_id=test_user_id, coin_type=test_coin_type, coin=test_coin[2].get("coin"), from_at=test_from_at, now_date=now)
    # for i in range(31):
    #     now = arrow.now(tz='+08:00').shift(days=-i).format('YYYY-MM-DD HH:mm:ss')
    #     add_test_coin(user_id=test_user_id, coin_type=test_coin_type, coin=test_coin[i].get("coin"), from_at=test_from_at, now_date=now)
