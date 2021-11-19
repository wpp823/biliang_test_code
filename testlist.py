from functools import reduce

list1 = [
    {'dd': "dd"}, {"dd": "dd"}, 11, 22, 33, 44, 55, 55, 66
]
# print(list1)
# print(list(set(list1)))


def duplicate_remove(data_list):
    # data_list = [{'id': '000'}, {'id': '000'}]
    run_function = lambda x, y: x if y in x else x + [y]
    return reduce(run_function, [[], ] + data_list)



print(duplicate_remove(list1))


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    intervals_sorted = sorted(intervals, key=lambda x: x[0])
    result = []
    for interval in intervals_sorted:
        # result中最后一个区间的右值>=新区间的左值，说明两个区间有重叠
        if result and result[-1][1] >= interval[0]:
            # 将result中最后一个区间更新为合并之后的新区间
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result


if '__main__' == __name__:
    intervals = [['11:10', '13:20'], ['11:20', '14:20'], ['15:10', '16:20']]
    print(merge(intervals))