from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import create_engine

MYSQL_HOST_NAME = "192.168.1.201"
MYSQL_HOST_PORT = "3308"
MYSQL_USER_NAME = "root"
MYSQL_PASSWORD = "pzzh123456"

engine = create_engine(f'mysql+pymysql://{MYSQL_USER_NAME}:{MYSQL_PASSWORD}@{MYSQL_HOST_NAME}:{MYSQL_HOST_PORT}/shopxo',
                       echo=True,
                       pool_size=5,
                       pool_recycle=3600,
                       pool_pre_ping=True
                       )
metadata = MetaData()
artist = Table('sxo_slide', metadata, autoload=True, autoload_with=engine)
artist.columns
pass
