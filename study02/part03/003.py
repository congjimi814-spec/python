# list相关:
# case1 双列表合并并去重:
list1 = [1,2,3,7,5]
list2 = [4,5,2,1,8]

for i in list2:
    list1.append(i)   #直接添加
print(list1)

# 合并方法:
new_list_1 = [*list1,*list2]   #解包合并
new_list_2 = list1 + list2   #直接相加

list3 = []
for i in list1:
    if i not in list3:    #(not) in 用法 返回True/False
        list3.append(i)   #去重添加
print(list3)


# case2 生成20以内的平方列表
# 列表推导式方法
list_case2_1 = [i**2 for i in range(1,21)]
print(list_case2_1)


#case3  生成20以内的偶数平方列表
list_case3_1 = [i**2 for i in range(1,21) if i%2 == 0 ]
print(list_case3_1)