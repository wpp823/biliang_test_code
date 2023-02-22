import arrow
import pymongo

from my_log import get_logger

log = get_logger()


def add_order_product_exts_data():
    """更新订单商品扩展字段数据"""

    pro_host = "mon7"  # 正式服v4
    dev_host = ""
    pro_client = pymongo.MongoClient(host=pro_host, port=3717)
    dev_client = pymongo.MongoClient(host=dev_host, port=27017)

    start_time = '2022-01-01 00:00:00'
    now_time = arrow.now(tz="+08:00").format('YYYY-MM-DD HH:mm:ss')

    # order_fields = [OrderModel.order_id.name, OrderModel.order_detail.name, OrderModel.products_ext.name, OrderModel.openid.name]
    db_beast = pro_client["beast"]
    table_user_beast = db_beast["users"]

    db_nig = pro_client["nightcrawler"]
    # db_nig = dev_client["nightcrawler"]
    table_orders = db_nig["orders"]

    order_infos = table_orders.find({
        "create_time": {
            "$gte": start_time, "$lte": now_time
        }
    })

    for order_info in order_infos:
        order_id = order_info.get("order_id")
        # if order_id != 1200201196290009:
        #     continue
        try:
            products_ext_infos = order_info.get("products_ext", [])
            xlkk_ext_info = order_info.get("xlkk_ext_info", {})
            real_product_infos = xlkk_ext_info.get("real_product_infos", [])
            # 更新products_ext
            if products_ext_infos:
                new_products_ext = []
                for ext_info in products_ext_infos:

                    referrer_doctor_id = ext_info.get("referrer_doctor_id")
                    if referrer_doctor_id == "_sys_superior_":
                        user_info = {
                            "user_role": "_sys_superior_"
                        }
                    else:
                        user_info = table_user_beast.find({
                            "user_id": referrer_doctor_id
                        }).limit(1)

                        user_info = user_info.next()

                    if not user_info:
                        log.error(f"user_error,order_id:{order_id}user_info:{user_info}")
                        continue

                    user_role = user_info.get("user_role", "")
                    beneficiary_role = ext_info.get("beneficiary_role")

                    if user_role == "nurse" and beneficiary_role == "nurse":
                        ext_info["referrer_doctor_id"] = "_sys_superior_"
                        ext_info["beneficiary_role"] = "_sys_superior_"

                    # else:
                    #     ext_info["referrer_user_id"] = referrer_doctor_id
                    #     ext_info["beneficiary_role"] = user_role
                    #
                    # ext_info["referrer_role"] = user_role
                    # ext_info["referrer_user_id"] = referrer_doctor_id
                    # ext_info["share_id"] = None

                    new_products_ext.append(ext_info)

                upd_result = table_orders.update_one(
                    filter={
                        "order_id": int(order_id)
                    },
                    update={
                        "$set": {
                            'products_ext': new_products_ext
                        }
                    }
                )
                upd_count = upd_result.modified_count
                log.info(f"products_ext:update_one order_id:{order_id},new_products_ext:{new_products_ext},upd_count:{upd_count}")
            # 更新xlkk_ext_info real_product_infos
            if real_product_infos:
                new_real_product_infos = []
                for real_product_info in real_product_infos:
                    referrer_doctor_id = real_product_info.get("referrer_doctor_id")

                    if referrer_doctor_id == "_sys_superior_":
                        user_info = {
                            "user_role": "_sys_superior_"
                        }
                    else:
                        user_info = table_user_beast.find({
                            "user_id": referrer_doctor_id
                        }).limit(1)
                        user_info = user_info.next()

                    if not user_info:
                        log.error(f"user_error,order_id:{order_id}user_info:{user_info}")
                        continue
                    user_role = user_info.get("user_role", "")
                    beneficiary_role = real_product_info.get("beneficiary_role")

                    if user_role == "nurse" and beneficiary_role == "nurse":
                        real_product_info["referrer_doctor_id"] = "_sys_superior_"
                        real_product_info["beneficiary_role"] = "_sys_superior_"

                    # else:
                    #     real_product_info["referrer_user_id"] = referrer_doctor_id
                    #     real_product_info["beneficiary_role"] = user_role

                    # real_product_info["beneficiary_role"] = user_role
                    # real_product_info["referrer_user_id"] = referrer_doctor_id
                    #
                    # real_product_info["referrer_role"] = user_role
                    # real_product_info["share_id"] = None

                    new_real_product_infos.append(real_product_info)

                upd_result = table_orders.update_one(
                    filter={
                        "order_id": int(order_id)
                    },
                    update={
                        "$set": {
                            'xlkk_ext_info.real_product_infos': new_real_product_infos
                        }
                    }
                )
                upd_count = upd_result.modified_count

                log.info(f"products_ext:update_one order_id:{order_id},new_real_product_infos:{new_real_product_infos},upd_count:{upd_count}")
        except:
            log.exception(order_id)
            continue

    pro_client.close()
    dev_client.close()
    log.info("end")


if __name__ == '__main__':
    add_order_product_exts_data()
