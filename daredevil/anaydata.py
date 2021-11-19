import collections
import urllib

import xmltodict

from daredevil.mongodb.dao.wx_message import WxMessageDao
from daredevil.mongodb.model.wx_message import WxMessageForwardObj, WxMsgForwardContentObj

from mongoengine import connect


def format_49_data(content,msg_id):
    """
    解析content内容，从type判断类型
    :return:
    """

    # content = self._content.replace('\n', '').replace('\t', '')
    # content = self._content
    xml_str = content[content.find('<msg'):content.rfind('msg>') + 4]
    xml_dict = xmltodict.parse(xml_str, encoding='utf-8')
    # print('=========xml_dict=====')
    # print(xml_dict)

    # data_content = xml_dict['msg']['appmsg']['recordinfo']
    forward_content_dict = xmltodict.parse(xml_dict['msg']['appmsg']['recorditem'])
    forward_msg_data_list = forward_content_dict['recordinfo']['datalist'].get('dataitem',[])
    if (type(forward_msg_data_list)) is not list:
        forward_msg_data_list = [forward_msg_data_list]
    #
    # print("forward_msg_data_list")
    # print(type(forward_msg_data_list))
    # print(forward_msg_data_list)


    forward_msg_content_list = [analysis_forward_msg_data(data_item,msg_id) for data_item in forward_msg_data_list]
    # forward_msg_content_list = analysis_forward_msg_data(forward_msg_data_list)
    # for data_item in forward_msg_data_list:
    #     print(data_item)
    #     forward_msg_content_list.append(data_item)
    # print("forward_msg_content_list")
    # print('forward_content_dict')
    # print(forward_content_dict)

    _msg_content = {
        'forward_msg_title': xml_dict['msg']['appmsg']['title'],
        'forward_msg_desc': forward_content_dict['recordinfo']['desc'],
        'forward_msg_content_list': forward_msg_content_list
    }
    return _msg_content


def analysis_forward_msg_data(forward_msg_data_item,msg_id):
    # 转发消息解析
    # print("forward_msg_data_item")
    # print(forward_msg_data_item)
    # print(type(forward_msg_data_item))
    # print(forward_msg_data_item.get('@datatype',False))
    msg_forward = {'type': int(forward_msg_data_item['@datatype']),
                   'msg_source_time': forward_msg_data_item['sourcetime'],
                   'msg_source_name': forward_msg_data_item['sourcename']}


    talker = forward_msg_data_item['dataitemsource'].get('fromusr',None)

    msg_forward['talker'] = talker if talker else forward_msg_data_item['dataitemsource'].get('realchatname',None)
    # print(msg_forward['talker'])

    # if msg_forward['type'] == 1:
    #     # 文本消息
    #     msg_forward['msg_desc'] = forward_msg_data_item['datadesc']
    #     msg_forward['msg_type'] = 'text'
    #
    #     msg_forward['msg_content_lite'] = {
    #         'desc': forward_msg_data_item['datadesc']
    #     }
    # elif msg_forward['type'] == 2:
    #     msg_forward['msg_type'] = 'image'
    #     msg_forward['msg_desc'] = '[图片]'
    #     msg_forward['msg_content_lite'] = {
    #         WxMsgForwardContentObj.desc.name: '图片',
    #         WxMsgForwardContentObj.upload_id.name: '',
    #         WxMsgForwardContentObj.url.name: '',
    #         WxMsgForwardContentObj.type.name: 'normal'
    #     }
    # elif msg_forward['type'] == 8:
    #     msg_forward['msg_type'] = 'file'
    #     msg_forward['msg_desc'] = '[文件]'
    #     msg_forward['msg_content_lite'] = {
    #         'desc': '[文件]'
    #     }
    # elif msg_forward['type'] == 6:
    #     msg_forward['msg_type'] = 'location'
    #     msg_forward['msg_desc'] = '[位置]'
    #     msg_forward['msg_content_lite'] = {
    #         'desc': '[位置]'
    #     }
    # elif msg_forward['type'] == 4:
    #     msg_forward['msg_type'] = 'video'
    #     msg_forward['msg_desc'] = '[视频]'
    #     msg_forward['msg_content_lite'] = {
    #         'desc': '视频'
    #     }
    # elif msg_forward['type'] == 5:
    #     url = forward_msg_data_item['weburlitem']["url"]
    #     url_encode = urllib.parse.quote(url).replace('/', '%2f')
    #     msg_forward['msg_type'] = 'thread_share'
    #     msg_forward['msg_desc'] = '[链接]'
    #     msg_forward['msg_content_lite'] = {
    #         WxMsgForwardContentObj.name.name: forward_msg_data_item['weburlitem']["title"],
    #         WxMsgForwardContentObj.desc.name: forward_msg_data_item['weburlitem']["desc"],
    #         WxMsgForwardContentObj.uri.name: "xlkk://weview2?url={}".format(url_encode),
    #         WxMsgForwardContentObj.image.name: '',
    #     }
    # elif msg_forward['type'] == 17:
    #     msg_forward['msg_type'] = 'text'
    #     msg_forward['msg_desc'] = '[聊天记录]'
    #     msg_forward['msg_content_lite'] = {
    #         'desc': '转发聊天记录'
    #     }
    # elif msg_forward['type'] == 22:
    #     # url = forward_msg_data_item['weburlitem']["url"]
    #     # url_encode = urllib.parse.quote(url).replace('/', '%2f')
    #     msg_forward['msg_type'] = 'thread_share'
    #     msg_forward['msg_desc'] = '[链接]'
    #     msg_forward['msg_content_lite'] = {
    #         # WxMsgForwardContentObj.name.name: forward_msg_data_item['weburlitem']["datatitle"],
    #         WxMsgForwardContentObj.desc.name: '链接',
    #         # WxMsgForwardContentObj.uri.name: "xlkk://weview2?url={}".format(url_encode),
    #         # WxMsgForwardContentObj.image.name: '',
    #     }
    # elif msg_forward['type'] == 19:
    #
    #     msg_forward['msg_type'] = 'mini'
    #     msg_forward['msg_desc'] = '[链接]'
    #     msg_forward['msg_content_lite'] = {
    #         WxMsgForwardContentObj.desc.name: '链接',
    #
    #     }
    # else:
    #     # if str(msg_forward['type']) not in ('3','4','5','17','22'):
    #     print("不支持消息内容")
    #     print(msg_id)
    #     print(msg_forward['type'])
    #     print(forward_msg_data_item)
    #     msg_forward['msg_type'] = '不支持消息内容'
    #     msg_forward['msg_desc'] = '[不支持消息内容]'
    #     msg_forward['msg_content_lite'] = {
    #         'desc': '[不支持消息内容]'
    #     }
    if msg_forward['type'] == 1:
        # 文本消息
        msg_forward['msg_desc'] = forward_msg_data_item['datadesc']
        msg_forward['msg_type'] = 'text'
        msg_forward['msg_content_lite'] = {
            WxMsgForwardContentObj.desc.name: forward_msg_data_item['datadesc']
        }
    elif msg_forward['type'] == 2:
        msg_forward['msg_type'] = 'image'
        msg_forward['msg_desc'] = '[图片]'
        msg_forward['msg_content_lite'] = {
            WxMsgForwardContentObj.desc.name: '图片',
            WxMsgForwardContentObj.upload_id.name: '',
            WxMsgForwardContentObj.url.name: '',
            WxMsgForwardContentObj.type.name: 'normal'

        }
    elif msg_forward['type'] == 8:
        # todo 待前端支持该类型再转换
        # msg_forward['msg_type'] = 'file'
        # msg_forward['msg_desc'] = '[文件]'
        # msg_forward['msg_content_lite'] = {
        #     WxMsgForwardContentObj.desc.name: '[文件]',  # 描述
        #     WxMsgForwardContentObj.title.name: '',  # 标题
        #     WxMsgForwardContentObj.url.name: '',  # 链接
        #     WxMsgForwardContentObj.image.name: '',  # 封面图片
        #
        # }
        msg_forward['msg_type'] = 'text'
        msg_forward['msg_desc'] = '[文件]'
        msg_forward['msg_content_lite'] = {
            WxMsgForwardContentObj.desc.name: '[文件]',  # 描述

        }
    elif msg_forward['type'] == 6:
        # todo 待前端支持该类型再转换
        # msg_forward['msg_type'] = 'location'
        msg_forward['msg_type'] = 'text'
        msg_forward['msg_desc'] = '[位置]'
        msg_forward['msg_content_lite'] = {
            WxMsgForwardContentObj.desc.name: '[位置]',  # 描述
        }
    elif msg_forward['type'] == 4:
        # todo 待前端支持该类型再转换
        # msg_forward['msg_type'] = 'location'
        msg_forward['msg_type'] = 'text'
        msg_forward['msg_desc'] = '[视频]'
        msg_forward['msg_content_lite'] = {
            WxMsgForwardContentObj.desc.name: '[视频]',  # 描述
        }
    elif msg_forward['type'] == 5:
        url = forward_msg_data_item['link']
        url_encode = urllib.parse.quote(url).replace('/', '%2f')
        msg_forward['msg_type'] = 'thread_share'
        msg_forward['msg_desc'] = '[链接]'
        msg_forward['msg_content_lite'] = {
            WxMsgForwardContentObj.title.name: forward_msg_data_item['weburlitem']["title"],
            WxMsgForwardContentObj.desc.name: forward_msg_data_item['weburlitem']["desc"],
            WxMsgForwardContentObj.uri.name: "xlkk://weview2?url={}".format(url_encode),
            WxMsgForwardContentObj.image.name: '',
        }
    elif msg_forward['type'] == 17:
        msg_forward['msg_type'] = 'text'
        msg_forward['msg_desc'] = '[聊天记录]'
        msg_forward['msg_content_lite'] = {
            'desc': '转发聊天记录'
        }
    elif msg_forward['type'] == 19:
        # todo 待前端支持该类型再转换
        # msg_forward['msg_type'] = 'miniprogram'
        msg_forward['msg_type'] = 'text '
        msg_forward['msg_desc'] = '[小程序]'
        msg_forward['msg_content_lite'] = {
            WxMsgForwardContentObj.desc.name: '小程序',
        }
    else:
        msg_forward['msg_type'] = 'text'
        msg_forward['msg_desc'] = '[不支持消息内容]'
        msg_forward['msg_content_lite'] = {
            'desc': '[不支持消息内容]'
        }

    return msg_forward


if __name__ == "__main__":

    MONGO_HOST_PART = "mongodb://root:Pzzh4Admin@192.168.1.230"
    MONGO_HOST_AUTH_DB = "admin"
    MONGO_HOST_REPLICA_SET = None
    database = 'daredevil'

    # connect(host=f"{MONGO_HOST_PART}/{database}?authSource={MONGO_HOST_AUTH_DB}")
    conn = connect(host=f"{MONGO_HOST_PART}/{database}?authSource={MONGO_HOST_AUTH_DB}")
    print(conn)

    my_db = conn["daredevil"]
    my_col = my_db["wx_message"]

    my_condition = {"type": 49, "msg_content.desc": "[聊天记录]"}
    # my_condition = {"msg_id": "SBwjaKMGgU8W"}
    data = my_col.find(my_condition)
    result = 0
    for item in data:
        msg_id = item.get('msg_id')
        content = item.get('content')
        # print("msg_id")
        # print(msg_id)
        msg_data = format_49_data(content,msg_id)

        msg_obj = WxMessageDao()
        res = msg_obj.update_msg_content(msg_id=msg_id, msg_content=msg_data)
        result += int(res)

    print(result)