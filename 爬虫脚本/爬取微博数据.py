from datetime import datetime
from io import BytesIO

import furl as furl
import pandas as pd
import requests

from my_log import get_logger

log = get_logger()


def get_weibo_content(user_id, since_id: str = ""):
    """
    获取用户
    :param since_id:
    :param user_id:
    :return:
    """
    key = 'f86ac6cf6c54b1a144e5a47d22a5b980d0efb36aecc2f5b89d2626fe'
    api = "http://whosecard.com:8081/api/weibo/user/feeds/v1"
    re_result = None

    full_url = f"{api}?key={key}&user_id={user_id}&since_id={since_id}"
    response = requests.get(url=full_url)

    if response:
        data = response.json()
        re_result = data.get("result", {})
        since_id = re_result.get('cardlistInfo', {}).get("since_id")

        log.info(f"get_weibo_content,user_id:{user_id} since_id:{since_id},data:{data}")
    return since_id, re_result


def get_results(user_id, since_id):
    """
    获取指定数量的,符合要求的数据

    :param user_id:
    :param since_id:
    :return:
    """

    since_id, weibo_data = get_weibo_content(user_id=user_id, since_id=since_id)
    weibo_data_cards = weibo_data.get("cards", [])
    weibo_cards = []
    for weibo_card in weibo_data_cards:  # todo
        # 过滤无效内容
        card_type = weibo_card.get("card_type", 0)  # 卡片类型
        if card_type == 9:
            mblog = weibo_card.get("mblog", {})
            created_at = mblog.get("created_at", "")  # wb 创建时间
            # pic_ids = weibo_card.get("pic_ids", [])  # 图片ids
            pic_infos = mblog.get("pic_infos", {})  # wb图片信息的字典
            text = mblog.get("text", "")  # wb图片信息的字典
            retweeted_status = mblog.get("retweeted_status", "")  # 被转发的原微博信息字段，当该微博为转发微博时返回
            if retweeted_status:  # 转发微博跳过
                continue
            content = text  # 文字内容
            time = str(datetime.strptime(created_at, '%a %b %d %H:%M:%S +0800 %Y'))
            source_list = []
            files = []
            # files_byte = []
            for item in pic_infos.values():
                file_url = item.get('original', {}).get("url", "")
                source_list.append(file_url)  # 资源列表
                # 下载文件]
                b_file = requests.get(url=file_url).content
                file_name = './imgs/'+file_url.split('/')[-1]
                with open(file_name,'wb') as ff:
                    ff.write(b_file)

                files.append(file_name)

            weibo_card_item = {
                "time": time,
                "content": content,
                "source_list": "\n".join(source_list),
                "files": "\n".join(files)
            }
            log.info(f"user_id:{user_id}, weibo_card_item:{weibo_card_item}")
            weibo_cards.append(weibo_card_item)

    return since_id, weibo_cards


def main():
    df_list = pd.read_excel("./护肤账号整理.xlsx", engine='openpyxl').fillna("")

    df_weibo_targets = df_list[df_list.来源.str.endswith("微博")].to_dict(orient="records")
    result = './weibo_result.xlsx'
    # count = 100
    # 生成dataframe
    # 分别写入不同sheet
    with pd.ExcelWriter(result) as writer:
        weibo_result_cards = []
        for item in df_weibo_targets:

            count = 100
            since_id = None
            url = item.get("链接")
            user_name = item.get("护肤账号")
            user_id = furl.furl(url).path.segments[1]
            # user_id = "5650696147"  # 测试


            while True:
                since_id, results = get_results(user_id=user_id, since_id=since_id)
                weibo_result_cards.extend(results)
                print(f"--------------{len(weibo_result_cards)}")
                # 判断是否符合数量
                if len(weibo_result_cards) >= count:
                    break

        df_result = pd.DataFrame(data=weibo_result_cards)
        df_result.to_excel(writer, sheet_name=user_name, index=False, header=True)
        writer.save()
        log.info('end')


if __name__ == "__main__":
    main()
