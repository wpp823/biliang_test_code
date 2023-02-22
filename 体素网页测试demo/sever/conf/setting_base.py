SERVICE_NAME = "nightcrawler"    # 服务名称，要与yaml中的service的名称一致。

REDIS_IP = '192.168.1.230'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = 'Pzzh4Admin'
SESSION_REDIS_DB = 1    # session存储的redis_db位置。

MONGO_HOST_PART = ""
MONGO_HOST_AUTH_DB = "admin"
MONGO_HOST_REPLICA_SET = None

MONGO_HOST = MONGO_HOST_PART + "/" + MONGO_HOST_AUTH_DB
MONGO_DB_NAME = 'nightcrawler'

#微信小商店(东东抢小程序)的配置
# MINISHOP_APPID = 'wx2bbecad4956ebe8d'
# MINISHOP_SERCET = '23ca1b478461e50e42cd16e5a013f80d'

# 小量康康小程序
MINISHOP_APPID = 'wxe6b89bd3689d4f57'
MINISHOP_SERCET = 'b34116aec3a483d081306541196efbc9'

EXECUTOR_MAX_COUNT = 10

SESSION_USER_KEY = 'nc_user'
SID_NAME = 'NightSessionID'

import logging
def getLogging():
    return logging.getLogger("nightcrawler")

TEST_SERVER = True


# 依赖的微服务地址
DEP_SID_NAME = "BeastSessionID"  # 依赖的session_id的Key，其值在cookie中。
DEP_HOSTNAME = 'allmark.local.com'


DEP_SCARLET_SERVER_NAME = '192.168.1.230'
DEP_SCARLET_SERVER_PORT = 17921
DEP_SCARLET_HOSTNAME = 'allmark.local.com'

DEP_THINE_SERVER_NAME = '192.168.1.230'
DEP_THING_SERVER_PORT = 17911
DEP_THING_HOSTNAME = None

DEP_BEAST_SERVER_NAME = '192.168.1.230'
# DEP_BEAST_SERVER_NAME = '127.0.0.1'
DEP_BEAST_SERVER_PORT = 18951
DEP_BEAST_HOSTNAME = None


# 包含测试商品
TEST_PRODUCT = True
