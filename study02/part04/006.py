# lambda 匿名函数

add = lambda x,y: x+y
print(add(12,61))

# case: 列表根据字符个数排序
data_list =["C++","C","Python","Jack",'PHP',"JavaScript"]
print(data_list)

data_list.sort(key=lambda item : len(item))
print(data_list)