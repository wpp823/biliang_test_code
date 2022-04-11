import pandas as pd
import requests
from bs4 import BeautifulSoup

from my_log import get_logger


def export_product_component():
    """
    爬取护肤品成分，导出到excel

    :return:
    """

    # new_table_col_name = ["product_id", "sku_id", "filing_no", "component_name_cn", "component_name_en", "effect", "function", "hazard", "activity", "safety"]
    new_data_list = []
    product_data = pd.read_excel("product_msg_CosMeDna.xls").fillna("")
    for item in product_data.to_dict(orient="records"):

        cosmedna_url = item.get("cosmedna_url", "")
        log.info(f"cosmedna_url:{cosmedna_url}")
        if cosmedna_url:
            res = requests.get(cosmedna_url)
            soup = BeautifulSoup(res.content.decode("utf-8"), 'lxml')
            title_node = soup.find('title')

            filing_no = title_node.contents[0].split(' ')[2]
            table_node = soup.find_all('tr')
            for idx, tr in enumerate(table_node):
                if idx != 0:
                    row_data = {
                        "product_id": item.get("product_id", ""),
                        "sku_id": item.get("sku_id", ""),
                        "title": item.get("title", ""),
                        "cosmedna_url": cosmedna_url,
                        "filing_no": filing_no,
                        "component_name_cn": "",
                        "component_name_en": "",
                        "effect": "",
                        "function": "",
                        "hazard": "",
                        "activity": "",
                        "safety": ""
                    }

                    tds = tr.find_all('td')
                    row_data["effect"] = tds[1].get_text()
                    row_data["function"] = tds[2].get_text()
                    row_data["hazard"] = tds[3].get_text()
                    row_data["safety"] = tds[5].get_text()

                    for index, td_item in enumerate(tds):
                        if index == 0:
                            names_div = td_item.find_all("div")
                            if tds[0].get_text() == "成分收集中":
                                row_data["component_name_en"] = row_data["component_name_cn"] = names_div[0].get_text()
                            else:
                                row_data["component_name_cn"] = names_div[0].get_text()
                                row_data["component_name_en"] = names_div[1].get_text() if len(names_div) == 2 else ''
                        elif index == 4:
                            img = td_item.find_all("imgs")
                            if img:
                                row_data["activity"] = img[0].get("src")[5:-4]
                        else:
                            pass
                    log.info(f"new_row_data ： {row_data}")
                    new_data_list.append(row_data)
        else:   # 无链接商品
            row_data = {
                "product_id": item.get("product_id", ""),
                "sku_id": item.get("sku_id", ""),
                "title": item.get("title", ""),
                "cosmedna_url": cosmedna_url,
                "filing_no": '',
                "component_name_cn": "",
                "component_name_en": "",
                "effect": "",
                "function": "",
                "hazard": "",
                "activity": "",
                "safety": ""
            }
            new_data_list.append(row_data)

    # 插入新的sheet里
    component_df = pd.DataFrame(new_data_list)
    component_df.to_excel("product_msg_CosMeDna_component.xls")
    # with pd.ExcelWriter('product_msg_CosMeDna.xls',mode='a', engine='openpyxl') as writer:
    #     component_df.to_excel(writer, sheet_name='成分数据')
    # writer.save()
    # writer.close()
    # log.info("end")


if __name__ == "__main__":
    log = get_logger()
    export_product_component()
