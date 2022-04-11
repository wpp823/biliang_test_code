import arrow as arrow
import pandas as pd
import pypinyin

file_path = './sku_code22040201.xls'


def yinjie(word):
    """
    返还带声调的拼音字符

    :param word:
    :return: 例如 xia3oyi2ngua4n
    """

    a = pypinyin.pinyin(word, style=pypinyin.FIRST_LETTER)

    b = []
    for i in range(len(a)):
        b.append(str(a[i][0]).upper())
    c = ''.join(b)
    return c


new_codes = []
now_at = arrow.now(tz="+08:00").format("YYMMDD")
df_data = pd.read_excel(file_path).fillna('')
df_data2 = pd.read_excel("./test_0406.xls").fillna('')
brands = df_data2.brand

table = df_data.merge(df_data2, left_on='product_id', right_on='product_id', how='left').fillna('')

product_ids = table.product_id.to_list()

out_product_dict = {
    product_id: 'P_' + '_'.join([yinjie(item) for item in table[table.product_id == product_id].brand.to_list()[0].split(',')])+f"_{now_at}" + f'_{index}'
    for index, product_id in enumerate(set(product_ids))
}
new_out_product_ids = [out_product_dict[product_id] for product_id in product_ids]

for index, brand_item in enumerate(brands.to_list()):
    if brand_item:
        new_codes.append('K_' + '_'.join([yinjie(item) for item in brand_item.split(',')])+f"_{now_at}" + f'_{index}')
    else:
        new_codes.append("")

print(new_out_product_ids)
print(new_codes)

df_data.insert(loc=1,column="spu_code", value=new_out_product_ids)
# df_data.insert(loc=1, column="new_code", value=new_codes)

df_data.to_excel(f"new{now_at}.xls")
pass
