import pandas as pd
import pypinyin

file_path = '正式服数据0303.xls'


def yinjie(word):
    """
    返还带声调的拼音字符

    :param word:
    :return: 例如 xia3oyi2ngua4n
    """
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.Style.TONE2):
        s = s + ''.join(i)
    return f"{s}"

new_codes = []

data = pd.read_excel(file_path).fillna('')
brands = data.brand
product_ids = data.product_id.to_list()

out_product_dict = {
    product_id: 'p_' + '_'.join([yinjie(item) for item in data[data.product_id == product_id].brand.to_list()[0].split(',')]) + f'_{index}'
    for index, product_id in enumerate(set(product_ids))
}
new_out_product_ids = [out_product_dict[product_id] for product_id in product_ids]

for index, brand_item in enumerate(brands.to_list()):
    if brand_item:
        new_codes.append('k_' + '_'.join([yinjie(item) for item in brand_item.split(',')]) + f'_{index}')
    else:
        new_codes.append("")

print(new_out_product_ids)
print(new_codes)

data.insert(loc=1,column="out_product_id", value=new_out_product_ids)
data.insert(loc=1, column="code", value=new_codes)

data.to_excel("new.xls")
pass
