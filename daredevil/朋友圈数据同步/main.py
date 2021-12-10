import json
import os
import sqlite3
import tempfile
import zipfile

import arrow
import shortuuid
from mongoengine import register_connection, connection

from daredevil.my_log import logger
from daredevil.朋友圈数据同步.mongo_db.wx_sns import WxSnsModel, PraiseObj, CommentObj, UploadUrlObj
from daredevil.朋友圈数据同步.mongo_db.wx_snses import WxChatSnsDao

MONGO_DB_NAME = 'daredevil'
MONGO_HOST_PART = "mongodb://root:Pzzh4Admin@192.168.1.230"
MONGO_HOST_AUTH_DB = "admin"
MONGO_HOST_REPLICA_SET = None

register_connection(db=MONGO_DB_NAME, host=MONGO_HOST_PART, authentication_source=MONGO_HOST_AUTH_DB, replicaset=None, alias=connection.DEFAULT_CONNECTION_NAME)


def do_sync_data(wx_user, offset, limit, cursor):
    # 共5张表，
    table_list = ['rcontact', 'chatroom', 'message', 'ImgInfo2', 'userinfo', "SNS"]

    tables_info = {}
    for table in table_list:
        # 获取表结构
        tables_info[table] = {}
        table_info = cursor.execute('PRAGMA table_info([{}])'.format(table))
        for row in table_info:
            field_name = row[1]
            tables_info[table][row[0]] = field_name

    table_info = tables_info["SNS"]

    # from_username = wx_user['username']
    wx_chat_sns_dao = WxChatSnsDao(log=logger)
    do_find_next = False  # 是否要继续查询
    items = cursor.execute("select * from SNS limit {},{}".format(offset, limit))
    for row in items:
        do_find_next = True
        try:
            logger.info('[do_async_wechat_sns][row: {}]'.format(row))
            row_data = {}
            for key, value in enumerate(row):
                field = table_info[key]
                row_data[field] = value
            # 一般数据
            snsId = row_data['snsId']
            # if snsId == -4707135754750709476:
            sns_data = {
                WxSnsModel.from_username.name: row_data['userName'],
                WxSnsModel.snsId.name: row_data['snsId'],
                WxSnsModel.username.name: row_data['userName'],
                WxSnsModel.nickname.name: row_data['userNickName'],
                WxSnsModel.remark_name.name: row_data['userRemarkName'],
                WxSnsModel.createTime.name: row_data['createTime'],
                WxSnsModel.type.name: row_data['type'],
                WxSnsModel.shareTitle.name: row_data['shareTitle'],
                WxSnsModel.stringSeq.name: row_data['stringSeq'],
                WxSnsModel.content.name: row_data['content'],
                WxSnsModel.url.name: [],
                WxSnsModel.praise.name: [],
                WxSnsModel.comment.name: [],
                WxSnsModel.contentBuf.name: "",
                WxSnsModel.attrBuf.name: "",
            }
            # 列表数据
            praise = row_data.get('praise', None)
            if praise:
                praise_list = json.loads(praise)
                sns_data[WxSnsModel.praise.name] = [PraiseObj(**item) for item in praise_list]
            comment = row_data.get('comment', None)
            if comment:
                comment_list = json.loads(comment)
                sns_data[WxSnsModel.comment.name] = [CommentObj(**item) for item in comment_list]
            urls = row_data.get('urls', None)
            if urls:
                url_list = urls.replace("[", "").replace("]", "").split(',')
                sns_data[WxSnsModel.url.name] = [UploadUrlObj(**{UploadUrlObj.upload_id.name: "", UploadUrlObj.url.name: item})
                                                 for item in url_list]
            # sns_data[WxSnsModel.url.name] = []
            # sns_data[WxSnsModel.praise.name] = []
            # sns_data[WxSnsModel.comment.name] = []
            # 大二进制数据,上传到数据库
            content_buffer = row_data['contentBuf']

            attr_buffer = row_data['attrBuf']

            from_username = row_data['userName']
            sns_info = wx_chat_sns_dao.get_by_snsId(from_username=from_username, snsId=snsId, fields=[WxSnsModel.snsId.name])
            if sns_info:
                logger.info('[do_async_wechat_sns][sns_exists][from_username:{}, msgSvrId:{}]'.format(from_username, snsId, ))

            else:
                # 添加朋友圈
                add_img_res = wx_chat_sns_dao.add(**sns_data)
                logger.info('[do_async_chat_img][add_chat_img][data:{}][{}]'.format(row_data, add_img_res))


        except Exception as e:
            logger.exception('[do_async_chat_img][row:{}]'.format(row))

    if do_find_next:
        new_offset = offset + limit
        do_sync_data(wx_user=wx_user, offset=new_offset, limit=limit, cursor=cursor)

    return


def run_async_chat_sns_img():
    """
    同步微信朋友圈图片
    :param record_id:
    :type record_id:
    :param company_id:
    :type company_id:
    :param user_id:
    :type user_id:
    :param area:
    :type area:
    :param telephone:
    :type telephone:
    :param device_id:
    :type device_id:
    :param batch_id:
    :type batch_id:
    :param file_upload_id:
    :type file_upload_id:
    :param file_upload_url:
    :type file_upload_url:
    :return:
    :rtype:
    """
    # zip_f = urllib.request.urlopen(file_upload_url)
    temp_dir = tempfile.gettempdir()
    #
    # # 解压文件目录
    file_path = "{}/{}_{}".format(temp_dir, int(arrow.now().datetime.timestamp()), shortuuid.random(8))
    # 下载的文件目录
    zip_file_path = ""
    # with open(zip_file_path, 'wb') as f:
    #     f.write(zip_f.read())
    zip_file_path = "./zips/1638842869_a28ftn3o_sns_0_1.zip"
    zip_file = zipfile.ZipFile(zip_file_path)
    zip_list = zip_file.namelist()  # 压缩文件清单，可以直接看到压缩包内的各个文件的明细
    for f in zip_list:  # 遍历这些文件，逐个解压出来，
        zip_file.extract(f, file_path)
    zip_file.close()  # 不能少！
    data_list = []
    for root, dirs, files in os.walk(file_path):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        data_list = []
        for f_name in files:
            f_name_list = f_name.split("_")  # ['snst', '13737752867132616874', '-4708991207135760199', '0.jpg']
            # f_name_list.append(f_name)
            data_list.append(f_name_list[2])
        # 去重
        data_list = list(set(data_list))
        print(data_list)
    ite_dict = {}
    for ite_id in data_list:
        ite_dict[ite_id] = []

        for root, dirs, files in os.walk(file_path):
            for f_name in files:
                f_name_list = f_name.split("_")
                id = f_name_list[2]
                if id == ite_id:
                    ite_dict[ite_id].append([int(f_name_list[-1].replace(".jpg","")), f_name])
    new_dict = {}
    for key,value in ite_dict.items():
        value.sort(key=lambda x:x[0])
        new_dict[key] =value


    print(new_dict)


    print(ite_dict)


if __name__ == "__main__":
    wx_user = {
        "username": "wwwwww"
    }
    offset = 0
    limit = 500

    call_db_file_path = "./sqlite/WeChat.db"

    # 连接数据库
    sqlite_conn = sqlite3.connect(call_db_file_path)
    cursor = sqlite_conn.cursor()
    # do_sync_data(wx_user=wx_user, offset=offset, limit=limit, cursor=cursor)
    # params = {
    #     "record_id": "", "company_id": "", "user_id": "", "area": "", "telephone": "", "device_id": "", "batch_id": "", "file_upload_id": "", "file_upload_url": ""
    # }
    run_async_chat_sns_img()
