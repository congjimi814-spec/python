# set 集合
# 无序的(不支持下标索引访问) 不可重复(自动去重)!!! 可修改 

# 定义
s1 = {'A','B','C'}
s2 = set()              #空集合

s3 = {3,5,6,4,9,3,5,6}
print(s3)

# 方法
s_1 = {1,2,3,4}
s_2 = {3,4,5,6}

# add()             添加元素
s_1.add(5)
print(s_1)

# remove()          移除指定元素(不存在会报错)
s_1.remove(5)
print(s_1)

# pop()             随机删除并返回
s_1_pop = s_1.pop()
print(s_1)
print(s_1_pop)      #删除的元素

# clear()           清空集合
s_1.clear()
print(s_1)

# difference()      求两集合的差集(含1不含2)   -
s_1 = {1,2,3,4}
s_2 = {3,4,5,6}
print(s_1.difference(s_2))
print(s_2.difference(s_1))

# union()           求两集合并集   |
print(s_1.union(s_2))

# intersection()    求两集合交集  &
print(s_1.intersection(s_2))


# 集合推导式写法
# 变量名称 = {i表达式 for i in 列表}
# 变量名称 = {i表达式 for i in 列表 if 条件}