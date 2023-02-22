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
from daredevil.朋友圈数据同步.mongo_db.wx_sns_img import WxSnsImgModel
from daredevil.朋友圈数据同步.mongo_db.wx_sns_imgs import WxChatSnsImgDao
from daredevil.朋友圈数据同步.mongo_db.wx_snses import WxChatSnsDao

MONGO_DB_NAME = 'daredevil'
MONGO_HOST_PART = ""
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
            praise_list = []
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
                sns_data[WxSnsModel.url.name] = url_list
            # sns_data[WxSnsModel.url.name] = []
            # sns_data[WxSnsModel.praise.name] = []
            # sns_data[WxSnsModel.comment.name] = []
            # 大二进制数据,上传到数据库
            content_buffer = row_data['contentBuf']

            attr_buffer = row_data['attrBuf']

            from_username = row_data['userName']
            sns_info = wx_chat_sns_dao.get_by_snsId(from_username=from_username, snsId=str(snsId), fields=[WxSnsModel.snsId.name])
            if sns_info:
                logger.info('[do_async_wechat_sns][sns_exists][from_username:{}, msgSvrId:{}]'.format(from_username, snsId, ))
                # 更新点赞评论 todo
                if praise:
                    wx_chat_sns_dao.update_praise(from_username=from_username, snsId=str(snsId), content=praise_list)
                # if comment:
                #     wx_chat_sns_dao.update_praise(from_username=from_username, snsId=snsId, )
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


def run_async_chat_sns_img(from_username, device_id, batch_id):
    """
    同步微信朋友圈图片
    :param from_username:
    :type from_username:
    :param device_id:
    :type device_id:
    :param batch_id:
    :type batch_id:
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
    zip_file_path = "./zips/1639130312_3bCMjxm2_sns_107_149.zip"
    zip_file = zipfile.ZipFile(zip_file_path)
    zip_list = zip_file.namelist()  # 压缩文件清单，可以直接看到压缩包内的各个文件的明细
    for f in zip_list:  # 遍历这些文件，逐个解压出来，
        zip_file.extract(f, file_path)
    zip_file.close()  # 不能少！
    data_list = []
    wx_chat_sns_img_dao = WxChatSnsImgDao(log=logger)
    wx_chat_sns_dao = WxChatSnsDao(log=logger)
    for root, dirs, files in os.walk(file_path):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        data_list = []
        for f_name in files:
            f_path = os.path.join(root, f_name)  # 文件路径
            posi = f_name.find('.')
            img_name_list = f_name.split("_")
            if posi != -1:
                suffix = f_name[posi:]
            else:
                suffix = ''
            try:
                snsId = img_name_list[2]
                img_index = f_name[posi - 1:posi]

                # 获取朋友圈记录
                sns_info = wx_chat_sns_dao.get_by_snsId(from_username=from_username, snsId=snsId, fields=[WxSnsModel.snsId.name, WxSnsModel.createTime.name])

                if sns_info:
                    createTime = sns_info.createTime
                    wx_sns_img_obj = wx_chat_sns_img_dao.get_by_sns_id_index(index=int(img_index), sns_id=snsId,from_username=from_username,
                                                                             fields=[WxSnsImgModel.snsId.name, WxSnsImgModel.from_username.name, WxSnsImgModel.img_url.name])

                    # 对应位置存在图片信息，
                    if wx_sns_img_obj and wx_sns_img_obj.img_url:
                        logger.info("[run_async_chat_sns_img_fail],[wx_sns_exist],[snsId:{},img_index:{}]".format(snsId, img_index))
                        continue

                    elif wx_sns_img_obj is None:
                        # 转换后对文件重命名
                        new_file_name = '{}_{}_{}.{}'.format(from_username, snsId, shortuuid.random(8), suffix)
                        # 文件全路径
                        new_file_path = '{}/{}'.format(root, new_file_name)

                        os.rename(f_path, new_file_path)
                        # 上传到oss
                        # upload_url, upload_id = oss_upload_obj.update_path_image(file_path=new_file_path,
                        #                                                          file_name=new_file_name)

                        upload_id = 'upload_{}'.format(shortuuid.random(8))
                        img_url = "www.baidu"
                        # old_upload_id = wx_msg_obj.msg_content.upload_id
                        if upload_id:
                            # 添加上传记录
                            logger.info("[run_async_chat_sns_img_add],[]")

                            add_wx_sns_img(from_username=from_username, snsId=snsId, createTime=createTime, img_index=img_index, img_url=img_url,
                                           upload_id=upload_id, device_id=device_id, batch_id=batch_id)
                            # 删除
                        #     if old_upload_id:
                        #         oss_upload_obj.delete_voice(voice_id=old_upload_id)
                        # if voice_text:
                        #     update_wx_msg_voice_text_svr_id(from_username=from_username, msgSvrId=msgSvrId, text_content=voice_text)
                else:
                    logger.info("[run_async_chat_sns_img_fail],[wx_sns_no_exist],[snsId:{}]".format(snsId))

            except Exception as e:
                logger.exception('[run_async_chat_voice][f_path:{}]'.format(f_path))


def add_wx_sns_img(from_username, snsId, createTime, img_index, img_url, upload_id, device_id, batch_id):
    """
    更新语音消息
    :param batch_id:
    :type batch_id:
    :param img_url:
    :type img_url:
    :param img_index:
    :type img_index:
    :param createTime:
    :type createTime:
    :param snsId:
    :type snsId:
    :param from_username:
    :param upload_id:
    :return:
    """
    wx_sns_img_dao = WxChatSnsImgDao(log=logger)
    # 更新图片消息图片链接
    create_at = arrow.now(tz='+08:00').strftime('%Y-%m-%d %H:%M:%S')
    res = wx_sns_img_dao.add(from_username=from_username, snsId=snsId, createTime=createTime, img_index=img_index, img_url=img_url, upload_id=upload_id,
                             create_at=create_at, device_id=device_id, batch_id=batch_id)
    # logger.info('[update_wx_message_voice][update_msg_voice_url][from_username:{}, msgSvrId:{},'
    #          ' upload_id:{}, voice_url:{}, upload_voice_record_id:{}]'
    #          '[{}]'.format(from_username, msgSvrId, upload_id, upload_url, record_id, res))


if __name__ == "__main__":
    wx_user = {
        "username": "test"
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
    device_id = "test"
    batch_id = "test"
    form_name = "wxid_zqrnihqc3z5q12"
    run_async_chat_sns_img(from_username=form_name, device_id=device_id, batch_id=batch_id)
