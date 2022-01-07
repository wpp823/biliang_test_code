# 2、将时间字符转为int型数据

new_data_list = [1, 2, 3, 4, 5, 8, 9]
# new_data_list = [arrow.get(x, 'YYYY-MM-DD').toordinal() for x in date_list]
sort_new_data_list = sorted(new_data_list, key=lambda x: int(x))
date_len = len(new_data_list)
sign_in_count = 0
for i in range(date_len):
    diff = sort_new_data_list[date_len - 1] - sort_new_data_list[i]
    value_range = len(sort_new_data_list[i:])
    if diff == value_range - 1:
        sign_in_count = value_range
        break

print(sign_in_count)
