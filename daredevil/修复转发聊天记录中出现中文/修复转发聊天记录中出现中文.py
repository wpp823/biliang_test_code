import arrow
import pymongo

import my_log


def repair_source_time(log):
    """更新标签对应消息时间"""
    dev_host = "mongodb://root:@--pub.mongodb.rds.aliyuncs.com"  # 测试服
    pro_host = "mongodb://root:@blmonogdbv4.mongodb.rds.aliyuncs.com:3717"  # 正式服v4
    client = pymongo.MongoClient(host=dev_host, port=3717)
    db = client['daredevil']

    wx_msg_table = db["wx_message"]

    log.info("begin")

    need_repair_contents = wx_msg_table.find({
        "msg_content.forward_msg_content_list.msg_source_time": {
            "$regex": '午'
        }
    })

    for wx_msg in need_repair_contents:
        forward_msg_content_list = wx_msg["msg_content"]["forward_msg_content_list"]

        for forward_msg_content in forward_msg_content_list:
            msg_source_time = forward_msg_content.get("msg_source_time", None)
            msg_id = wx_msg["msg_id"]
            data_id = forward_msg_content["data_id"]
            if "下午" in msg_source_time or "上午" in msg_source_time:
                time_2 = msg_source_time.replace("下午", "PM").replace("上午", "AM")
                msg_source_time = arrow.get(time_2, ["YYYY-M-D AH:mm", "YYYY-M-D H:mmA"]).format("YYYY-MM-DD HH:mm:ss")
                upd_result = wx_msg_table.update_one(
                    filter={
                        "msg_id": msg_id,
                        "msg_content.forward_msg_content_list.data_id": data_id,
                    },
                    update={
                        "$set": {
                            'msg_content.forward_msg_content_list.$.msg_source_time': msg_source_time
                        }
                    },
                    # array_filters=[{"i.tag_from": msg_id}]
                )
                upd_count = upd_result.modified_count

                log.info(f"repair_source_time:msg_id: {msg_id},data_id:{data_id} msg_source_time:{msg_source_time},modified_count:{upd_count}")


if __name__ == '__main__':
    log = my_log.get_logger()
    repair_source_time(log=log)


