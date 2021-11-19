import time

import arrow

e_time_begin = '7:50'
e_time_end = '8:50'

d_time_begin = '9:00'
d_time_end = '15:00'

print(e_time_begin < e_time_end)
print(e_time_begin > e_time_end)
# d_time_begin_3 = '6:00'
# d_time_end_4 = '7:00'

if e_time_end > d_time_begin:

    tiems = e_time_begin + '-' + d_time_end
    print(tiems)
elif e_time_end < d_time_begin:
    pass
elif e_time_begin > d_time_begin:
    pass
elif d_time_end < e_time_begin:
    pass

# price_list = [0]
# hotval_list = [0]

# 价格列表
price_list = []
if not price_list:
    print(True)
    price_list = [0]
else:
    print(False)

print(price_list)
pay_time = "2021-11-08 17:16:18"
time1 = arrow.get(pay_time).replace(tzinfo='+0800')
print(time1)
