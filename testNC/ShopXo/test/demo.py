# from model.sxo_order import SxoOrderModel
#
# data = SxoOrderModel.status.name
# print(data)
# print(SxoOrderModel.express_number.key)
# upd_info = {
#     SxoOrderModel.id.name: 1111,
#     SxoOrderModel.status.name: 3,
#     SxoOrderModel.express_id.name: 1,
#     SxoOrderModel.express_number.name: "",
#     SxoOrderModel.delivery_time.name: 23123123123,
#     SxoOrderModel.upd_time.name: 23123123123
# }
# print(upd_info)
#
# pass
# from dao.sxo_consts import SxoConstsDao
# from my_log import get_logger
#
# log = get_logger()
#
#
# const_dao= SxoConstsDao(log=log)
#
# data = const_dao.get_express_info(express_name="顺丰快递")
#
# print(data)
# pass

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
MYSQL_HOST_NAME = "127.0.0.1"
MYSQL_HOST_PORT = "3306"
MYSQL_USER_NAME = "root"
MYSQL_PASSWORD = "a.123456"

engine = create_engine(f'mysql+pymysql://{MYSQL_USER_NAME}:{MYSQL_PASSWORD}@{MYSQL_HOST_NAME}:{MYSQL_HOST_PORT}/shopxo_loacl',
                       echo=True,
                       pool_size=5,
                       pool_recycle=3600,
                       pool_pre_ping=True
                       )

from model.test_model import TestModel, Base

Base.metadata.create_all(engine) #创建表结构

test_1 = TestModel(
    warehouse_id=10,
    goods_id=22,
    md5_key="ddasdad"
)

test_2 = TestModel(
    warehouse_id=10,
    goods_id=22,
    md5_key="ddasdad"
)

conn = sessionmaker(bind=engine)()

print(conn)
conn.add(test_1)
conn.commit()
print("===============add1")

conn.add(test_2)
conn.commit()


print("===============add2")
conn.close()
