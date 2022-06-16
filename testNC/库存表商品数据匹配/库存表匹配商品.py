import pandas as pd


# 库存表
stock_file_path = "./库存表.xlsx"
df_stock = pd.read_excel(stock_file_path,engine='openpyxl').fillna("")
# 商品数据表
nc_file_path = "./pro_0506001_export_v2.xls"
df_nc_product = pd.read_excel(nc_file_path,sheet_name="xlkk_product_data").fillna("")

product_list = df_nc_product.to_dict(orient="records")
stock_product_list = df_stock.to_dict(orient="records")

l_1_category_dict = {}
l_2_category_dict = {}
for s_product in stock_product_list:
    title = s_product.get("品名")
    specs = s_product.get("规格")

    # countries = ['U.*', 'Ch.*']
    countries_regexp = '^({}.*)$'.format(title)
    df_product_info = df_nc_product[df_nc_product.title.str.match(countries_regexp)]
    if df_product_info.empty:
        print(f"{title} 匹配失败")
    print(df_product_info)


df_result = pd.DataFrame(product_list).to_excel("./result.xls")
