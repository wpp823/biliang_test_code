import re

from mongoengine import connect

from daredevil.mongodb.dao.wx_contacts import WxContactsDao
from daredevil.mongodb.dao.wx_message import WxMessageDao
from daredevil.mongodb.model.wx_contacts import WxContactsModel
from daredevil.mongodb.model.wx_region_code import region_code_dict


def by_line_read(file_name):
    with open(file_name) as f:  # 打开文件
        line = f.readline()  # 读取一行内容
        while line:
            yield line
            line = f.readline()  # 不断循环读取


def conversion_region(region_code):
    # read = by_line_read('../resource/mmregioncode_zh_CN.txt')
    region_data = {}
    # 处理数据变为字典
    # msg_list = [data.replace('\n', '') for data in read]
    # # print(msg_list)
    # country_list = []
    # city_list = []
    # province_list = []
    #
    # province_pattern = ''
    #
    # for item in msg_list:
    #     if '_' not in item:
    #         country_list.append(item)
    #     elif re.match(r'^[A-Z]*_.*_.*\|.*', item):
    #         city_list.append(item)
    #     else:
    #         province_list.append(item)
    # # print(country_list)
    # # print(province_list)
    # # print(city_list)
    #
    # region_code_list = []
    # for country_item in country_list:
    #     item_list = country_item.split('|')
    #
    #     # country_dict[country_code] = country_name
    #
    #     country_dict = {
    #         'country_code': item_list[0],
    #         'country_name': item_list[1],
    #         'province_list':[]
    #     }
    #
    #     for province in province_list:
    #         province_name = province.split('|')[1]
    #         province_code = province.split('|')[0].split('_')[1]
    #         if country_dict['country_code'] in province:
    #             province_dict = {
    #                 'province_code': province_code,
    #                 'province_name': province_name,
    #                 # province_code:province_name,
    #                 'city_list': []
    #             }
    #
    #             for city in city_list:
    #                 city_name = city.split('|')[1]
    #                 city_code = city.split('|')[0].split('_')[2]
    #                 if province_code in city:
    #                     city_dict = {
    #                         'city_code': city_code,
    #                         'city_name': city_name,
    #                         # city_code:city_name
    #                     }
    #                     province_dict['city_list'].append(city_dict)
    #                 # print(province_dict)
    #             country_dict['province_list'].append(province_dict)
    #     region_code_list.append(country_dict)
    # with open('../mongodb/model/data','a') as wx_code:
    #     wx_code.write(str(region_code_list))

    region_code_list = region_code_dict
    req_msg_list = region_code.split('_')

    if len(req_msg_list) == 1:
        req_msg_list = [region_code]
    print(req_msg_list)

    for region in region_code_list:
        if region.get(req_msg_list[0], None):
            region_data['country'] = region[req_msg_list[0]]

            if len(req_msg_list) >= 2:
                for province_list in region["province_list"]:
                    if req_msg_list[1] == province_list['province_code']:
                        region_data['province'] = province_list['province_name']

                        if len(req_msg_list) >= 3:
                            for cities in province_list['city_list']:
                                if req_msg_list[2] == cities['city_code']:
                                    region_data['city'] = cities['city_name']
                                    break

    return region_data


if __name__ == '__main__':

    MONGO_HOST_PART = "mongodb://root:@192.168.1.230"
    MONGO_HOST_AUTH_DB = "admin"
    MONGO_HOST_REPLICA_SET = None
    database = 'daredevil'

    conn = connect(host=f"{MONGO_HOST_PART}/{database}?authSource={MONGO_HOST_AUTH_DB}")
    print(conn)

    my_db = conn["daredevil"]
    my_col = my_db["wx_contacts"]
    WxContacts = WxContactsModel()
    my_condition = {"regionCode": {"$ne": None}}
    # my_condition = {"contact_id":"fFQKJTXzidN7"}
    data = my_col.find(my_condition)
    # {"regionCode": {'$ne': null, $exists: true}, "type": 1}

    result = 0
    for item in data:
        contact_id = item.get('contact_id')
        region_code = item.get('regionCode')

        if region_code != '':
            print(contact_id)
            region_msg = conversion_region(region_code)
            if region_msg:
                msg_obj = WxContactsDao()
                res = msg_obj.update_region_name(contact_id=contact_id, region_msg=region_msg)
                result += int(res)
                print(region_msg)
            # pass
    print(result)
