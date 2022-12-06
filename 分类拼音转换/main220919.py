import pypinyin

category_list = [
    {'cate_id': 'CA_mia4nbu4ca3izhua1ng', 'name': '面部彩妆', 'children_list': [

        {'cate_id': 'L2_CA_fe3ndi3', 'name': '粉底'},
        {'cate_id': 'L2_CA_zhe1xia2', 'name': '遮瑕'},
        {'cate_id': 'L2_CA_di4ngzhua1ng', 'name': '定妆'},
        {'cate_id': 'L2_CA_ge2li2', 'name': '隔离'}]},
    {'cate_id': 'CA_mia4nbu4hu4fu1', 'name': '面部护肤', 'children_list': [

        {'cate_id': 'L2_CA_xie4zhua1ng', 'name': '卸妆'},
        {'cate_id': 'L2_CA_jie2mia4n', 'name': '洁面'},
        {'cate_id': 'L2_CA_shua3ngfu1', 'name': '爽肤'},
        {'cate_id': 'L2_CA_ji1di3', 'name': '肌底'},
        {'cate_id': 'L2_CA_bu3shui3', 'name': '补水'},
        {'cate_id': 'L2_CA_ba3oshi1', 'name': '保湿'},
        {'cate_id': 'L2_CA_fa2ngsha4i', 'name': '防晒'}]},
    {'cate_id': 'CA_ya3nbu4hu4li3', 'name': '眼部护理', 'children_list': [
        {'cate_id': 'L2_CA_qu4he1iya3nqua1n', 'name': '去黑眼圈'}]},
    {'cate_id': 'CA_go1ngxia4ohu4fu1', 'name': '功效护肤', 'children_list': [
        {'cate_id': 'L2_CA_me3iba2i', 'name': '美白'},
        {'cate_id': 'L2_CA_ka4ngshua1ila3o', 'name': '抗衰老'},
        {'cate_id': 'L2_CA_ka4ngzho4u', 'name': '抗皱'},
        {'cate_id': 'L2_CA_qu1ba1n', 'name': '祛斑'},
        {'cate_id': 'L2_CA_qu4he1ito2u', 'name': '去黑头'},
        {'cate_id': 'L2_CA_qu4jia3ozhi4', 'name': '去角质'},
        {'cate_id': 'L2_CA_shu1hua3nxiu1hu4', 'name': '舒缓修护'}]},
    # 22020919 修改添加分类
    {'cate_id': 'CA_yi1lia2o', 'name': '医疗器械', 'children_list': [
        {'cate_id': 'L2_CA_chua1ngmia4nyu4he2', 'name': '创面愈合'},
        {'cate_id': 'L2_CA_chua1ngmia4nyu4he2', 'name': '防脱发'},
        {'cate_id': 'L2_CA_chua1ngmia4nyu4he2', 'name': '康复理疗'},
        {'cate_id': 'L2_CA_chua1ngmia4nyu4he2', 'name': '外用贴膏'},
        {'cate_id': 'L2_CA_chua1ngmia4nyu4he2', 'name': '家庭常备'},
        {'cate_id': 'L2_CA_chua1ngmia4nyu4he2', 'name': '其他'},

    ]},
    {'cate_id': 'CA_we4ishe1ngyo4ngpi3n', 'name': '中药配方', 'children_list': [
        {'cate_id': 'L2_CA_chu2ju1nyi4ju1n', 'name': '精制饮片'}]},

    {'cate_id': 'CA_we4ishe1ngyo4ngpi3n', 'name': '中西成药', 'children_list': [
        {'cate_id': 'L2_CA_chu2ju1nyi4ju1n', 'name': '止咳平喘'},
        {'cate_id': 'L2_CA_chu2ju1nyi4ju1n', 'name': '降血糖'},
        {'cate_id': 'L2_CA_chu2ju1nyi4ju1n', 'name': '外用'},
        {'cate_id': 'L2_CA_chu2ju1nyi4ju1n', 'name': '五官用药'},
        {'cate_id': 'L2_CA_chu2ju1nyi4ju1n', 'name': '胃肠道'},
        {'cate_id': 'L2_CA_chu2ju1nyi4ju1n', 'name': '心脑血管'},
        {'cate_id': 'L2_CA_chu2ju1nyi4ju1n', 'name': '泌尿系统'},
        {'cate_id': 'L2_CA_chu2ju1nyi4ju1n', 'name': '妇科'},
        {'cate_id': 'L2_CA_chu2ju1nyi4ju1n', 'name': '其他'},
    ]},

    {'cate_id': 'CA_we4ishe1ngyo4ngpi3n', 'name': '卫生用品', 'children_list': [
        {'cate_id': 'L2_CA_chu2ju1nyi4ju1n', 'name': '除菌抑菌'}]},

    {'cate_id': 'CA_me3ifa1hu4fa1', 'name': '美发护发', 'children_list': [
        {'cate_id': 'L2_CA_xi3fa4', 'name': '洗发'},
        {'cate_id': 'L2_CA_hu4fa1', 'name': '护发'},
        {'cate_id': 'L2_CA_to2upi2hu4li3', 'name': '头皮护理'}]},
    {'cate_id': 'CA_she1nti3hu4li3', 'name': '身体护理', 'children_list': [
        {'cate_id': 'L2_CA_mu4yu4', 'name': '沐浴'},
        {'cate_id': 'L2_CA_she1nti3ru3', 'name': '身体乳'}]},
    {'cate_id': 'CA_sho3ubu4hu4li3', 'name': '手部护理', 'children_list': [
        {'cate_id': 'L2_CA_hu4sho3u', 'name': '护手'},
        {'cate_id': 'L2_CA_xi3sho3u', 'name': '洗手'}]},
    {'cate_id': 'CA_chu2nbu4hu4li3', 'name': '唇部护理', 'children_list': [
        {'cate_id': 'L2_CA_hu4chu2n', 'name': '护唇'}]},
    {'cate_id': 'CA_zu2bu4hu4li3', 'name': '足部护理', 'children_list': []}]


def yinjie_2(word):
    """
    返还带声调的拼音字符

    :param word:
    :return: 例如 xia3oyi2ngua4n
    """
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.Style.TONE2):
        s = s + ''.join(i)
    return f"{s}"


new = []
for item in category_list:
    new_children_list = []
    name = item.get("name", None)
    # cate_id = item.get("cate_id", None)
    children_list = item.get("children_list", [])
    cate_id = f"CA_{yinjie_2(name)}"

    if children_list:
        for i_item in children_list:
            i_name = i_item["name"]
            i_cate_id = f"L2_CA_{yinjie_2(i_name)}"
            new_children_list.append(
                {
                    "cate_id": i_cate_id,
                    "name": i_name,
                }
            )

    new.append({
        "cate_id": cate_id,
        "name": name,
        "children_list": new_children_list})

print(new)
