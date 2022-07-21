from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MYSQL_HOST_NAME = "39.108.5.214"
MYSQL_HOST_PORT = "33090"
MYSQL_USER_NAME = "root"
MYSQL_PASSWORD = "pzzh123456"
SHOPXO_DATABASE_NAME = "shopxo_dev"



class ShopBase:
    def __init__(self, log):
        self.log = log
        self._engine = create_engine(f'mysql+pymysql://{MYSQL_USER_NAME}:{MYSQL_PASSWORD}@{MYSQL_HOST_NAME}:{MYSQL_HOST_PORT}/{SHOPXO_DATABASE_NAME}',
                                     echo=True,
                                     pool_size=5,
                                     pool_recycle=3600,
                                     pool_pre_ping=True
                                     )

        self.session = sessionmaker(self._engine)()  # 构建session对象


engine = create_engine(f'mysql+pymysql://{MYSQL_USER_NAME}:{MYSQL_PASSWORD}@{MYSQL_HOST_NAME}:{MYSQL_HOST_PORT}/{SHOPXO_DATABASE_NAME}',
                       echo=False,
                       pool_size=5,
                       pool_recycle=3600,
                       pool_pre_ping=True)


def mysql_conn_session(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        conn_pool = sessionmaker(bind=engine)
        conn = conn_pool()
        response = func(conn, *args, **kwargs)
        conn.close()
        return response

    return wrapper
