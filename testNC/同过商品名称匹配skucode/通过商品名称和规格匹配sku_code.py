import pandas as pd

excel_file_path = "./商城产品总表0402.xls"

product_list = pd.read_excel(excel_file_path, sheet_name="产品功效和分类 (中文功效码)").fillna("")
category_list = pd.read_excel(excel_file_path, sheet_name="用途").fillna("")
df_products = pd.read_excel("./正式服_042101_export_data_v2.xls").fillna("")

product_list = product_list.to_dict(orient="records")
l_1_category_dict = {}
l_2_category_dict = {}
for product in product_list:
    title = product.get("产品名")
    category = product.get("用途")
    specs = product.get("规格")

    df_data1 = df_products[df_products.title == title]

    sku_data = df_data1[df_data1.sku_name == specs]["code"].values
    if not sku_data.size:
        continue
    product["sku_code"] = sku_data[0]

df_result = pd.DataFrame(product_list).to_excel("./result.xls")
