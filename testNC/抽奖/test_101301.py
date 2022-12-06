my_list = [11, 12, 13]
my_tuple = (21, 22, 23)
print([x for x in zip(my_list, my_tuple)])

data = dict(zip(my_list, my_tuple))
print(data)

my_dic = {31: 2, 32: 4, 33: 5}
my_set = {41, 42, 43, 44}
print([x for x in zip(my_dic)])
my_pychar = "python"
my_shechar = "shell"
print([x for x in zip(my_pychar, my_shechar)])