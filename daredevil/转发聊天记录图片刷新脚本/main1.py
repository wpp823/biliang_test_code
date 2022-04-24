from app.celery.async_wechat_data import run_async_chat_img

record_1 = {
    "record_id": "JBSiy7uF32ez",
    "user_id": "",
    "upload_type": "wechat_chat_img",
    "batch_id": "20220412_210916",
    "device_id": "d_zzftXkSirACm",
    "area": "86",
    "telephone": "13045879041",
    "upload_id": "upload_7Ago23t2zgQA",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/deeppupil/2022-04-12/1649769118_5pPzdpT5_forward_0.zip",
    "data_begin_at": "2022-04-12 17:43:45",
    "data_end_at": "2022-04-12 21:09:16",
    "remote_ip": "113.110.140.218",
    "async_use_time": 337,
    "status": "finish",
    "create_at": "2022-04-12 21:11:59",
    "update_at": "2022-04-12 22:01:09"
}
QUEUE_ASYNC_WEHCAT_CHAT_IMG = 'async_wechat_chat_img'
task_1 = run_async_chat_img.apply_async([record_1.get("record_id"),
                                         record_1.get("company_id"),
                                         record_1.get("user_id"),
                                         record_1.get("area"),
                                         record_1.get("telephone"),
                                         record_1.get("device_id"),
                                         record_1.get("batch_id"),
                                         record_1.get("upload_id"),
                                         record_1.get("upload_url")],
                                        queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)

# /* 2 createdAt:2022-04-12T10:27:41.000Z*/
record_2 = {
    "record_id": "admGcq4GMuFF",
    "user_id": "",
    "upload_type": "wechat_chat_img",
    "batch_id": "20220412_182656",
    "device_id": "d_c3Sariuky2Qr",
    "area": "86",
    "telephone": "18664390290",
    "upload_id": "",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42777181308252160/1523092304/deeppupil_1649759222527_i4JCAGTX_forward_0.zip",
    "data_begin_at": "2021-01-18 00:00:00",
    "data_end_at": "2022-04-12 18:26:56",
    "remote_ip": "183.48.243.22",
    "async_use_time": 1214,
    "status": "finish",
    "create_at": "2022-04-12 18:27:41",
    "update_at": "2022-04-12 21:48:12"
}
task_2 = run_async_chat_img.apply_async([record_2.get("record_id"),
                                         record_2.get("company_id"),
                                         record_2.get("user_id"),
                                         record_2.get("area"),
                                         record_2.get("telephone"),
                                         record_2.get("device_id"),
                                         record_2.get("batch_id"),
                                         record_2.get("upload_id"),
                                         record_2.get("upload_url")],
                                        queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)

# /* 3 createdAt:2022-04-12T09:53:34.000Z*/
record_3 = {
    "record_id": "Lseo3HM7TCSo",
    "user_id": "",
    "upload_type": "wechat_chat_img",
    "batch_id": "20220412_174746",
    "device_id": "d_9hTpCiTgnScn",
    "area": "86",
    "telephone": "17607676383",
    "upload_id": "upload_6aKAZbUe7zuy",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/deeppupil/2022-04-12/1649757213_WzRkXAC2_forward_0.zip",
    "data_begin_at": "2022-04-11 21:06:47",
    "data_end_at": "2022-04-12 17:47:46",
    "remote_ip": "113.110.140.218",
    "async_use_time": 394,
    "status": "finish",
    "create_at": "2022-04-12 17:53:33",
    "update_at": "2022-04-12 21:47:51"
}
task_3 = run_async_chat_img.apply_async([record_3.get("record_id"),
                                         record_3.get("company_id"),
                                         record_3.get("user_id"),
                                         record_3.get("area"),
                                         record_3.get("telephone"),
                                         record_3.get("device_id"),
                                         record_3.get("batch_id"),
                                         record_3.get("upload_id"),
                                         record_3.get("upload_url")],
                                        queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)
#
# /* 4 createdAt:2022-04-12T09:50:41.000Z*/
# {
# 	"_id" : ObjectId("62554b71f74488000a93dfc8"),
# 	"record_id" : "FC4GLqewpUFY",
# 	"user_id" : "",
# 	"upload_type" : "wechat_chat_img",
# 	"batch_id" : "20220412_174320",
# 	"device_id" : "d_xxH9WsBBgDf5",
# 	"area" : "86",
# 	"telephone" : "18681452807",
# 	"upload_id" : "upload_5W43ciPnwSed",
# 	"upload_url" : "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/deeppupil/2022-04-12/1649757040_anFzccNY_forward_0.zip",
# 	"data_begin_at" : "2022-04-11 21:10:28",
# 	"data_end_at" : "2022-04-12 17:43:20",
# 	"remote_ip" : "113.110.140.218",
# 	"async_use_time" : 315,
# 	"status" : "finish",
# 	"create_at" : "2022-04-12 17:50:41",
# 	"update_at" : "2022-04-12 21:47:30"
# }

record_4 = {
    "record_id": "FC4GLqewpUFY",
    "user_id": "",
    "upload_type": "wechat_chat_img",
    "batch_id": "20220412_174320",
    "device_id": "d_xxH9WsBBgDf5",
    "area": "86",
    "telephone": "18681452807",
    "upload_id": "upload_5W43ciPnwSed",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/deeppupil/2022-04-12/1649757040_anFzccNY_forward_0.zip",
    "data_begin_at": "2022-04-11 21:10:28",
    "data_end_at": "2022-04-12 17:43:20",
    "remote_ip": "113.110.140.218",
    "async_use_time": 315,
    "status": "finish",
    "create_at": "2022-04-12 17:50:41",
    "update_at": "2022-04-12 21:47:30"

}
task_4 = run_async_chat_img.apply_async([record_4.get("record_id"),
                                         record_4.get("company_id"),
                                         record_4.get("user_id"),
                                         record_4.get("area"),
                                         record_4.get("telephone"),
                                         record_4.get("device_id"),
                                         record_4.get("batch_id"),
                                         record_4.get("upload_id"),
                                         record_4.get("upload_url")],
                                        queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)
#
# /* 5 createdAt:2022-04-12T09:49:05.000Z*/
# {
# 	"_id" : ObjectId("62554b11f74488000a93dfb6"),
# 	"record_id" : "PnauwF2jZrmX",
# 	"user_id" : "",
# 	"upload_type" : "wechat_chat_img",
# 	"batch_id" : "20220412_174740",
# 	"device_id" : "d_SfaoYmMkUvzv",
# 	"area" : "86",
# 	"telephone" : "15626510370",
# 	"upload_id" : "",
# 	"upload_url" : "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42767451374415872/2029775964/deeppupil_1649756944267_hXnqSKyN_forward_0.zip",
# 	"data_begin_at" : "2021-01-18 00:00:00",
# 	"data_end_at" : "2022-04-12 17:47:40",
# 	"remote_ip" : "183.48.243.22",
# 	"async_use_time" : 74,
# 	"status" : "finish",
# 	"create_at" : "2022-04-12 17:49:05",
# 	"update_at" : "2022-04-12 21:46:34"
# }
record_5 = {
    "record_id": "PnauwF2jZrmX",
    "user_id": "",
    "upload_type": "wechat_chat_img",
    "batch_id": "20220412_174740",
    "device_id": "d_SfaoYmMkUvzv",
    "area": "86",
    "telephone": "15626510370",
    "upload_id": "",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42767451374415872/2029775964/deeppupil_1649756944267_hXnqSKyN_forward_0.zip",
    "data_begin_at": "2021-01-18 00:00:00",
    "data_end_at": "2022-04-12 17:47:40",
    "remote_ip": "183.48.243.22",
    "async_use_time": 74,
    "status": "finish",
    "create_at": "2022-04-12 17:49:05",
    "update_at": "2022-04-12 21:46:34"

}
task_5 = run_async_chat_img.apply_async([record_5.get("record_id"),
                                         record_5.get("company_id"),
                                         record_5.get("user_id"),
                                         record_5.get("area"),
                                         record_5.get("telephone"),
                                         record_5.get("device_id"),
                                         record_5.get("batch_id"),
                                         record_5.get("upload_id"),
                                         record_5.get("upload_url")],
                                        queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)
#
# /* 6 createdAt:2022-04-12T09:46:17.000Z*/
# {
# 	"_id" : ObjectId("62554a69f74488000a93df9b"),
# 	"record_id" : "gehBLFRs2pEx",
# 	"user_id" : "",
# 	"upload_type" : "wechat_chat_img",
# 	"batch_id" : "20220412_174345",
# 	"device_id" : "d_zzftXkSirACm",
# 	"area" : "86",
# 	"telephone" : "13045879041",
# 	"upload_id" : "upload_6daaCW2QGuRa",
# 	"upload_url" : "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/deeppupil/2022-04-12/1649756776_qQQZCYAU_forward_0.zip",
# 	"data_begin_at" : "2022-04-11 21:09:00",
# 	"data_end_at" : "2022-04-12 17:43:45",
# 	"remote_ip" : "113.110.140.218",
# 	"async_use_time" : 313,
# 	"status" : "finish",
# 	"create_at" : "2022-04-12 17:46:17",
# 	"update_at" : "2022-04-12 21:46:12"
# }
record_6 = {
    "record_id": "gehBLFRs2pEx",
    "user_id": "",
    "upload_type": "wechat_chat_img",
    "batch_id": "20220412_174345",
    "device_id": "d_zzftXkSirACm",
    "area": "86",
    "telephone": "13045879041",
    "upload_id": "upload_6daaCW2QGuRa",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/deeppupil/2022-04-12/1649756776_qQQZCYAU_forward_0.zip",
    "data_begin_at": "2022-04-11 21:09:00",
    "data_end_at": "2022-04-12 17:43:45",
    "remote_ip": "113.110.140.218",
    "async_use_time": 313,
    "status": "finish",
    "create_at": "2022-04-12 17:46:17",
    "update_at": "2022-04-12 21:46:12"

}
task_6 = run_async_chat_img.apply_async([record_6.get("record_id"),
                                         record_6.get("company_id"),
                                         record_6.get("user_id"),
                                         record_6.get("area"),
                                         record_6.get("telephone"),
                                         record_6.get("device_id"),
                                         record_6.get("batch_id"),
                                         record_6.get("upload_id"),
                                         record_6.get("upload_url")],
                                        queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)
#
# /* 7 createdAt:2022-04-12T09:21:02.000Z*/
# {
# 	"_id" : ObjectId("6255447ef74488000a93df64"),
# 	"record_id" : "EMLnyVru262d",
# 	"user_id" : "",
# 	"upload_type" : "wechat_chat_img",
# 	"batch_id" : "20220412_170219",
# 	"device_id" : "d_c3Sariuky2Qr",
# 	"area" : "86",
# 	"telephone" : "15626512230",
# 	"upload_id" : "",
# 	"upload_url" : "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42758860999421952/-1788763981/deeppupil_1649754195266_YjSGXdbr_forward_0.zip",
# 	"data_begin_at" : "2021-01-18 00:00:00",
# 	"data_end_at" : "2022-04-12 17:02:19",
# 	"remote_ip" : "183.48.243.22",
# 	"async_use_time" : 318088,
# 	"status" : "finish",
# 	"create_at" : "2022-04-12 17:21:02",
# 	"update_at" : "2022-04-12 21:33:04"
# }
record_7 = {
    "record_id": "EMLnyVru262d",
    "user_id": "",
    "upload_type": "wechat_chat_img",
    "batch_id": "20220412_170219",
    "device_id": "d_c3Sariuky2Qr",
    "area": "86",
    "telephone": "15626512230",
    "upload_id": "",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42758860999421952/-1788763981/deeppupil_1649754195266_YjSGXdbr_forward_0.zip",
    "data_begin_at": "2021-01-18 00:00:00",
    "data_end_at": "2022-04-12 17:02:19",
    "remote_ip": "183.48.243.22",
    "async_use_time": 318088,
    "status": "finish",
    "create_at": "2022-04-12 17:21:02",
    "update_at": "2022-04-12 21:33:04"

}
task_7 = run_async_chat_img.apply_async([record_7.get("record_id"),
                                         record_7.get("company_id"),
                                         record_7.get("user_id"),
                                         record_7.get("area"),
                                         record_7.get("telephone"),
                                         record_7.get("device_id"),
                                         record_7.get("batch_id"),
                                         record_7.get("upload_id"),
                                         record_7.get("upload_url")],
                                        queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)
#
# /* 8 createdAt:2022-04-12T08:32:33.000Z*/
# {
# 	"_id" : ObjectId("62553921f74488000a93df23"),
# 	"record_id" : "dtnZ9xbeAnM9",
# 	"user_id" : "",
# 	"upload_type" : "wechat_chat_img",
# 	"batch_id" : "20220412_161737",
# 	"device_id" : "d_c3Sariuky2Qr",
# 	"area" : "86",
# 	"telephone" : "15626512230",
# 	"upload_id" : "",
# 	"upload_url" : "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42747608310935552/-1788763981/deeppupil_1649751512574_XahdAcAc_forward_0.zip",
# 	"data_begin_at" : "2021-01-18 00:00:00",
# 	"data_end_at" : "2022-04-12 16:17:37",
# 	"remote_ip" : "183.48.243.22",
# 	"async_use_time" : 73821,
# 	"status" : "finish",
# 	"create_at" : "2022-04-12 16:32:33",
# 	"update_at" : "2022-04-12 20:10:30"
# }
record_8 = {
    "record_id": "dtnZ9xbeAnM9",
    "user_id": "",
    "upload_type": "wechat_chat_img",
    "batch_id": "20220412_161737",
    "device_id": "d_c3Sariuky2Qr",
    "area": "86",
    "telephone": "15626512230",
    "upload_id": "",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42747608310935552/-1788763981/deeppupil_1649751512574_XahdAcAc_forward_0.zip",
    "data_begin_at": "2021-01-18 00:00:00",
    "data_end_at": "2022-04-12 16:17:37",
    "remote_ip": "183.48.243.22",
    "async_use_time": 73821,
    "status": "finish",
    "create_at": "2022-04-12 16:32:33",
    "update_at": "2022-04-12 20:10:30"

}
task_8 = run_async_chat_img.apply_async([record_8.get("record_id"),
                                         record_8.get("company_id"),
                                         record_8.get("user_id"),
                                         record_8.get("area"),
                                         record_8.get("telephone"),
                                         record_8.get("device_id"),
                                         record_8.get("batch_id"),
                                         record_8.get("upload_id"),
                                         record_8.get("upload_url")],
                                        queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)
#
# /* 9 createdAt:2022-04-12T08:04:40.000Z*/
# {
# 	"_id" : ObjectId("62553298f74488000a93df02"),
# 	"record_id" : "R57fZ6uS9Sns",
# 	"user_id" : "",
# 	"upload_type" : "wechat_chat_img",
# 	"batch_id" : "20220412_154727",
# 	"device_id" : "d_c3Sariuky2Qr",
# 	"area" : "86",
# 	"telephone" : "18594207159",
# 	"upload_id" : "",
# 	"upload_url" : "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42738683800907776/-1925218446/deeppupil_1649749650388_XqFh8GgU_forward_0.zip",
# 	"data_begin_at" : "2011-01-18 00:00:00",
# 	"data_end_at" : "2022-04-11 17:15:33",
# 	"remote_ip" : "47.105.115.66",
# 	"async_use_time" : 1,
# 	"status" : "finish",
# 	"create_at" : "2022-04-12 16:04:40",
# 	"update_at" : "2022-04-12 16:19:32"
# }
record_9 = {
    "record_id": "R57fZ6uS9Sns",
    "user_id": "",
    "upload_type": "wechat_chat_img",
    "batch_id": "20220412_154727",
    "device_id": "d_c3Sariuky2Qr",
    "area": "86",
    "telephone": "18594207159",
    "upload_id": "",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42738683800907776/-1925218446/deeppupil_1649749650388_XqFh8GgU_forward_0.zip",
    "data_begin_at": "2011-01-18 00:00:00",
    "data_end_at": "2022-04-11 17:15:33",
    "remote_ip": "47.105.115.66",
    "async_use_time": 1,
    "status": "finish",
    "create_at": "2022-04-12 16:04:40",
    "update_at": "2022-04-12 16:19:32"

}
task_9 = run_async_chat_img.apply_async([record_9.get("record_id"),
                                         record_9.get("company_id"),
                                         record_9.get("user_id"),
                                         record_9.get("area"),
                                         record_9.get("telephone"),
                                         record_9.get("device_id"),
                                         record_9.get("batch_id"),
                                         record_9.get("upload_id"),
                                         record_9.get("upload_url")],
                                        queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)
#
# /* 10 createdAt:2022-04-12T07:55:19.000Z*/
# {
# 	"_id" : ObjectId("62553067f74488000a93df00"),
# 	"record_id" : "LQjaXox3RiPr",
# 	"user_id" : "",
# 	"upload_type" : "wechat_chat_img",
# 	"batch_id" : "20220412_154726",
# 	"device_id" : "d_c3Sariuky2Qr",
# 	"area" : "86",
# 	"telephone" : "18594207159",
# 	"upload_id" : "",
# 	"upload_url" : "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42738683800907776/-1925218446/deeppupil_1649749650388_XqFh8GgU_forward_0.zip",
# 	"data_begin_at" : "2021-01-18 00:00:00",
# 	"data_end_at" : "2022-04-12 15:47:26",
# 	"remote_ip" : "183.48.243.22",
# 	"async_use_time" : 38132,
# 	"status" : "finish",
# 	"create_at" : "2022-04-12 15:55:19",
# 	"update_at" : "2022-04-12 16:02:59"
# }
record_10 = {
    "record_id": "LQjaXox3RiPr",
    "user_id": "",
    "upload_type": "wechat_chat_img",
    "batch_id": "20220412_154726",
    "device_id": "d_c3Sariuky2Qr",
    "area": "86",
    "telephone": "18594207159",
    "upload_id": "",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42738683800907776/-1925218446/deeppupil_1649749650388_XqFh8GgU_forward_0.zip",
    "data_begin_at": "2021-01-18 00:00:00",
    "data_end_at": "2022-04-12 15:47:26",
    "remote_ip": "183.48.243.22",
    "async_use_time": 38132,
    "status": "finish",
    "create_at": "2022-04-12 15:55:19",
    "update_at": "2022-04-12 16:02:59"

}
task_10 = run_async_chat_img.apply_async([record_10.get("record_id"),
                                          record_10.get("company_id"),
                                          record_10.get("user_id"),
                                          record_10.get("area"),
                                          record_10.get("telephone"),
                                          record_10.get("device_id"),
                                          record_10.get("batch_id"),
                                          record_10.get("upload_id"),
                                          record_10.get("upload_url")],
                                         queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)
#
# /* 11 createdAt:2022-04-12T06:47:59.000Z*/
# {
# 	"_id" : ObjectId("6255209ff74488000a93deeb"),
# 	"record_id" : "yC7PqVaNkpgK",
# 	"user_id" : "",
# 	"upload_type" : "wechat_chat_img",
# 	"batch_id" : "20220412_143809",
# 	"device_id" : "d_c3Sariuky2Qr",
# 	"area" : "86",
# 	"telephone" : "18594207159",
# 	"upload_id" : "",
# 	"upload_url" : "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42721252315426816/-1925218446/deeppupil_1649745493807_q7riy2yR_forward_0.zip",
# 	"data_begin_at" : "2021-01-18 00:00:00",
# 	"data_end_at" : "2022-04-12 14:38:09",
# 	"remote_ip" : "183.48.243.22",
# 	"async_use_time" : 153424,
# 	"status" : "finish",
# 	"create_at" : "2022-04-12 14:47:59",
# 	"update_at" : "2022-04-12 15:00:10"
# }
record_11 = {
    "record_id": "yC7PqVaNkpgK",
    "user_id": "",
    "upload_type": "wechat_chat_img",
    "batch_id": "20220412_143809",
    "device_id": "d_c3Sariuky2Qr",
    "area": "86",
    "telephone": "18594207159",
    "upload_id": "",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42721252315426816/-1925218446/deeppupil_1649745493807_q7riy2yR_forward_0.zip",
    "data_begin_at": "2021-01-18 00:00:00",
    "data_end_at": "2022-04-12 14:38:09",
    "remote_ip": "183.48.243.22",
    "async_use_time": 153424,
    "status": "finish",
    "create_at": "2022-04-12 14:47:59",
    "update_at": "2022-04-12 15:00:10"

}
task_11 = run_async_chat_img.apply_async([record_11.get("record_id"),
                                          record_11.get("company_id"),
                                          record_11.get("user_id"),
                                          record_11.get("area"),
                                          record_11.get("telephone"),
                                          record_11.get("device_id"),
                                          record_11.get("batch_id"),
                                          record_11.get("upload_id"),
                                          record_11.get("upload_url")],
                                         queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)
#
# /* 12 createdAt:2022-04-12T01:36:17.000Z*/
# {
# 	"_id" : ObjectId("6254d7913e53f6000a7a0d8d"),
# 	"record_id" : "h5fpZQvudkMf",
# 	"user_id" : "",
# 	"upload_type" : "wechat_chat_img",
# 	"batch_id" : "20220412_092620",
# 	"device_id" : "d_c3Sariuky2Qr",
# 	"area" : "86",
# 	"telephone" : "13045879041",
# 	"upload_id" : "",
# 	"upload_url" : "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42386597032685568/50648248/deeppupil_1649665818226_9mnhHcow_forward_0.zip",
# 	"data_begin_at" : "2011-01-18 00:00:00",
# 	"data_end_at" : "2022-04-11 17:15:33",
# 	"remote_ip" : "47.105.115.66",
# 	"async_use_time" : 1,
# 	"status" : "finish",
# 	"create_at" : "2022-04-12 09:36:17",
# 	"update_at" : "2022-04-12 10:11:49"
# }

record_12 = {
    "record_id": "h5fpZQvudkMf",
    "user_id": "",
    "upload_type": "wechat_chat_img",
    "batch_id": "20220412_092620",
    "device_id": "d_c3Sariuky2Qr",
    "area": "86",
    "telephone": "13045879041",
    "upload_id": "",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42386597032685568/50648248/deeppupil_1649665818226_9mnhHcow_forward_0.zip",
    "data_begin_at": "2011-01-18 00:00:00",
    "data_end_at": "2022-04-11 17:15:33",
    "remote_ip": "47.105.115.66",
    "async_use_time": 1,
    "status": "finish",
    "create_at": "2022-04-12 09:36:17",
    "update_at": "2022-04-12 10:11:49"

}
task_12 = run_async_chat_img.apply_async([record_12.get("record_id"),
                                          record_12.get("company_id"),
                                          record_12.get("user_id"),
                                          record_12.get("area"),
                                          record_12.get("telephone"),
                                          record_12.get("device_id"),
                                          record_12.get("batch_id"),
                                          record_12.get("upload_id"),
                                          record_12.get("upload_url")],
                                         queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)
# 转发记录中的文件
file_record_1 = {
    "record_id": "zEwce3Kyygjz",
    "user_id": "",
    "upload_type": "wechat_chat_forward_record_files",
    "batch_id": "20220412_154726",
    "device_id": "d_c3Sariuky2Qr",
    "area": "86",
    "telephone": "18594207159",
    "upload_id": "",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42738626821287936/-1925218446/deeppupil_1649749650388_XqFh8GgU_forwardVideoFile_0.zip",
    "data_begin_at": "2021-01-18 00:00:00",
    "data_end_at": "2022-04-12 15:47:26",
    "remote_ip": "183.48.243.22",
    "async_use_time": 3035,
    "status": "finish",
    "create_at": "2022-04-12 15:54:30",
    "update_at": "2022-04-12 16:02:33"
}
file_task_1 = run_async_chat_img.apply_async([file_record_1.get("record_id"),
                                              file_record_1.get("company_id"),
                                              file_record_1.get("user_id"),
                                              file_record_1.get("area"),
                                              file_record_1.get("telephone"),
                                              file_record_1.get("device_id"),
                                              file_record_1.get("batch_id"),
                                              file_record_1.get("upload_id"),
                                              file_record_1.get("upload_url")],
                                             queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)
file_record_2 = {
    "record_id": "gfigAb68kdRz",
    "user_id": "",
    "upload_type": "wechat_chat_forward_record_files",
    "batch_id": "20220412_143809",
    "device_id": "d_c3Sariuky2Qr",
    "area": "86",
    "telephone": "18594207159",
    "upload_id": "",
    "upload_url": "https://allmark.oss-cn-shenzhen.aliyuncs.com/scarlet/temp/self_upload/42721190944370688/-1925218446/deeppupil_1649745493807_q7riy2yR_forwardVideoFile_0.zip",
    "data_begin_at": "2021-01-18 00:00:00",
    "data_end_at": "2022-04-12 14:38:09",
    "remote_ip": "183.48.243.22",
    "async_use_time": 2246,
    "status": "finish",
    "create_at": "2022-04-12 14:45:12",
    "update_at": "2022-04-12 14:50:45"
}

file_task_2 = run_async_chat_img.apply_async([file_record_2.get("record_id"),
                                              file_record_2.get("company_id"),
                                              file_record_2.get("user_id"),
                                              file_record_2.get("area"),
                                              file_record_2.get("telephone"),
                                              file_record_2.get("device_id"),
                                              file_record_2.get("batch_id"),
                                              file_record_2.get("upload_id"),
                                              file_record_2.get("upload_url")],
                                             queue=QUEUE_ASYNC_WEHCAT_CHAT_IMG)
