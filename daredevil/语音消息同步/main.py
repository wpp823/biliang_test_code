import os
import tempfile
import zipfile

import arrow
import shortuuid

from daredevil.语音消息同步.baidu_asr_tool import BaiduAsrTool


def test(file_upload_url, from_username):
    file_upload_url = r"https:\\allmark.oss-cn-shenzhen.aliyuncs.com\scarlet\temp\deeppupil\2021-12-07\1638842868_cFsLQDTg_voice_0_2.zip"
    temp_dir = tempfile.gettempdir()
    # 解压文件目录
    file_path = "{}/{}_{}".format(temp_dir, int(arrow.now().datetime.timestamp()), shortuuid.random(8))
    # 下载的文件目录
    # zip_file_path = "{}.zip".format(file_path)
    #
    # zip_f = urllib.request.urlopen(file_upload_url)
    # zip_f = ""
    zip_file_path = "1638842868_cFsLQDTg_voice_0_2.zip"
    # with open(zip_file_path, 'wb') as f:
    #     f.write(zip_f.read())

    zip_file = zipfile.ZipFile(zip_file_path)
    zip_list = zip_file.namelist()  # 压缩文件清单，可以直接看到压缩包内的各个文件的明细
    for f in zip_list:  # 遍历这些文件，逐个解压出来，
        zip_file.extract(f, file_path)
    zip_file.close()  # 不能少！

    print('[file_path:{}]'.format(file_path))

    # oss_upload_obj = BaseUploadOss(company_id=company_id, user_id=user_id, log=log)

    # wx_message_dao = WxMessageDao(log=log)
    # 遍历文件
    for root, dirs, files in os.walk(file_path):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        for f_name in files:
            f_path = os.path.join(root, f_name)  # 文件路径
            print("源文件：{}".format(f_path))
            posi = f_name.find('.')
            if posi != -1:
                msgSvrId = f_name[:posi]
                suffix = f_name[posi:]
            else:
                msgSvrId = f_name
                suffix = ''
                # wx_msg_obj = wx_message_dao.get_msg_info(from_username=from_username, msgSvrId=str(msgSvrId),
                #                                          fields=[WxMessageModel.msg_id.name,
                #                                                  WxMessageModel.msg_type.name,
                #                                                  WxMessageModel.msg_content.name])
                # 有文字内容就不需要更新，避免重复识别
                # if wx_msg_obj.msg_content.text:
                #     continue

                # elif wx_msg_obj and wx_msg_obj.msg_type == 'voice':
                # 上传语音到oss
            # 新文件名称
            # new_file_name = '{}/{}_{}_{}{}'.format(root,from_username, msgSvrId, shortuuid.random(8), suffix)
            # # 重命名
            # os.rename(f_path, new_file_name)

            # fixme 测试
            # '/Users/wyy/Desktop/codes/mytest/daredevil/语音消息同步/silk_client'
            path_current = os.path.abspath(r".") + "/silk_client"
            commod = "sh  {}/converter.sh {} {}".format(path_current, f_path, "pcm")
            print("cmd :{}".format(commod))
            # commod = "sh converter.sh {} {}".format(amr_file, "pcm")
            os.system(commod)
            # 转换完成后的pcm文件名
            # 转换后对文件重命名
            pcm_file_name = os.path.join(root, msgSvrId) + ".pcm"
            new_file_name = '{}_{}_{}.{}'.format(from_username, msgSvrId, shortuuid.random(8), "pcm")
            # 文件全路径
            new_pcm_file_name = '{}/{}'.format(root, new_file_name)

            # new_pcm_file_name = '{}/{}_{}_{}.{}'.format(root,from_username, msgSvrId, shortuuid.random(8), "pcm")
            os.rename(pcm_file_name, new_pcm_file_name)
            print("new_pcm_file_name :{}".format(new_pcm_file_name))
            # 将转换完的数据上传到oss
            # upload_url, upload_id = oss_upload_obj.update_path_image(file_path=f_path,
            #                                                          file_name=new_pcm_file_name)
            # old_upload_id = wx_msg_obj.msg_content.upload_id
            # 语音识别
            baidu_client = BaiduAsrTool()
            voice_text_res = baidu_client.get_voice_text(voice_file_path=root,voice_file_name=new_file_name)
            # # 删除源amr文件
            os.remove(f_path)
            if voice_text_res:
                voice_text = ' '.join(voice_text_res)
                print(voice_text)
            else:
                print("errr")


if __name__ == '__main__':
    file_upload_url = r"https:\\allmark.oss-cn-shenzhen.aliyuncs.com\scarlet\temp\deeppupil\2021-12-07\1638842868_cFsLQDTg_voice_0_2.zip"

    from_username = "6KGEWF54gX57"
    test(file_upload_url, from_username)
