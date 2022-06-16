import pandas as pd

df_jd_stock = pd.read_excel('jd-20220601094006024.xls', engine='xlrd').fillna("")
df_wx_stock = pd.read_excel('pro_060101_v2.xls', sheet_name="wx_product_data").fillna("")

contrast_result = "result.xls"
col_name = ["spu_code","title"]
df_wx_stock = df_wx_stock
# 清洗微信数据
df_spu_code_list = df_wx_stock[df_wx_stock.spu_code != ''].drop_duplicates(['spu_code'], keep='first', inplace=False)["spu_code"]

for spu_code in df_spu_code_list:
    print(spu_code)
    # 获取微信商品数据
    if spu_code.startswith("P_TZ_"):
        product_infos = df_wx_stock[df_wx_stock.spu_code == spu_code]
        # 过滤套装中其他商品
        product_infos = product_infos[product_infos.code.str.startswith("K_TZ_")]
    else:

        product_infos = df_wx_stock[df_wx_stock.spu_code == spu_code]

        # [not df_wx_stock.code.str.startswith("K_TZ_")]


pass
