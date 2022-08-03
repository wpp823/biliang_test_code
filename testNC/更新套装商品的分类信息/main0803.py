import pandas as pd

excel_file_path = "./pro_080301_v2.xls"
wx_product_sheet_name = "wx_product_data"
xlkk_product_sheet_name = "xlkk_product_data"


def update_suit_category():
    """更新套装的分类信息"""

    df_wx_product = pd.read_excel(excel_file_path, sheet_name=wx_product_sheet_name).fillna("")
    df_ext_product = pd.read_excel(excel_file_path, sheet_name=xlkk_product_sheet_name).fillna("")

    # 过滤套装code
    df_wx_product = df_wx_product[df_wx_product["spu_code"].str.startswith("P_TZ_")]
    # 过滤分类为空
    df_wx_product = df_wx_product[df_wx_product["category"] == ""]

    need_sync_spu_codes = df_wx_product["spu_code"].unique().tolist()

    for spu_code in need_sync_spu_codes:

        suit_products = df_wx_product[df_wx_product["spu_code"] == spu_code]
        category_list = []
        # for product in suit_products.:
        for index, row in suit_products.iterrows():

            sku_code = row["code"]
            if not sku_code.startswith("K_TZ_"):
                category = df_ext_product[df_ext_product["code"] == sku_code].iloc[0]["category"]

                category_list.append(category)

        suit_category = "|".join(category_list)

        print(f"{spu_code}:{suit_category}")


if __name__ == '__main__':
    update_suit_category()
