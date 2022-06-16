import time

import arrow

data_end_at = "2022-05-28T19:45:00+00:00"

update_time = "2022-05-13T19:44:41+00:00"

data_end_at = arrow.get(data_end_at)  # 当前执行任务的结束的时间范围

update_time = arrow.get(update_time)  # 订单数据的更新时间

diff_time = (data_end_at-update_time).total_seconds()
print(diff_time<5*60)

print(diff_time)