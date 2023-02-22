import xmltodict
from mongoengine import *
from pymongo import MongoClient

MONGO_HOST_PART = ""
MONGO_HOST_AUTH_DB = "admin"
MONGO_HOST_REPLICA_SET = None
database = 'daredevil'

# connect(host=f"{MONGO_HOST_PART}/{database}?authSource={MONGO_HOST_AUTH_DB}")
conn = MongoClient(host=f"{MONGO_HOST_PART}/{database}?authSource={MONGO_HOST_AUTH_DB}")
print(conn)

mydb = conn["daredevil"]
mycol = mydb["wx_message"]


# my_condition = {
#     "msg_id" : "bLFzH9EkoPxk"
#     # "type" : 49
# }

my_condition = {"type":49,"msg_content.desc":"[聊天记录]"}
data = mycol.find(my_condition).limit(10)
for item  in  data:

    content = item.get('content')

    # conn.gedb.getCollection('wx_message').find({'msg_desc':/聊天记录/})
    # content = self._content.replace('\n', '').replace('\t', '')
    # content = self._content
    xml_str = content[content.find('<msg'):content.rfind('msg>') + 4]
    xml_dict = xmltodict.parse(xml_str, encoding='utf-8')
    forward_content = xml_dict['msg']['appmsg']['recorditem'].replace('\n', '').replace('\t', '')
    forward_content_dict = xmltodict.parse(forward_content)

    print(forward_content_dict)
    forward_msg_content_list = forward_content_dict['recordinfo']['datalist']['dataitem']
    print(forward_msg_content_list)

    # _msg_content = {
    #     'forward_msg_title': forward_content_dict['recordinfo']['title'],
    #     'forward_msg_desc': forward_content_dict['recordinfo']['desc'],
    #     'forward_msg_content_list': forward_msg_content_list
    # }
    #
    # for item in forward_msg_content_list:
    #     print(item)
    #
    #     msg_source_time = item['sourcename']
    #     msg_source_name = item['sourcename']
    #     talker = item['dataitemsource']['fromusr']
    #
    #     if item['@datatype'] == '1': # 文字消息
    #         msg_type = 'text'
    #         type = '1'
    #         msg_desc = item['datadesc']
    #
    #     elif item['@datatype'] == '2': # 图片数据
    #         pass
    # msg_content = {
    #
    # }
    # forward_msg_content_list_content = {
    #
    # }
    # type_mapping = {
    #             "4": {    # 文章
    #                 'type': 'thread_share',
    #                 # 'desc': '[链接]{}'.format(title)
    #             },
    #             "5": {    # 也是文章
    #                 'type': 'thread_share',
    #                 # 'desc': '[链接]{}'.format(title)
    #             },
    #             "6": {    # 文件
    #                 'type': 'file',
    #                 # 'desc': '[文件]{}'.format(title)
    #             },
    #             "19": {    # 聊天记录
    #                 'type': 'chat_record',
    #                 'desc': '[聊天记录]'
    #             },
    #             "33": {  # 小程序
    #                 'type': 'miniprogram',
    #                 'desc': '[小程序]'
    #             },
    #             "36": {  # 也是小程序
    #                 'type': 'miniprogram',
    #                 'desc': '[小程序]'
    #             },
    #         }
    # for item in forward_content_dict['datalist']:
    #
    #     pass



# print(_msg_content)

# thumburl = xml_dict['msg']['appmsg'].get('thumburl', '')
#
