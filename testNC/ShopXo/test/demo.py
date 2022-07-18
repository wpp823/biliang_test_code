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
from dao.sxo_consts import SxoConstsDao
from my_log import get_logger

log = get_logger()


const_dao= SxoConstsDao(log=log)

data = const_dao.get_express_info(express_name="顺丰快递")

print(data)
pass