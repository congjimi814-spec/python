# 元组 tuple 与列表类似
# 可重复 有序 定义完成后不可修改

# 定义
a1 = ()          #空元组
a2 = tuple()     #空元组
a3 = (10,)       #单元素元组
print(type(a1))

# 索引访问
b = (10,30,50,90,10,'ciallo')
print(b[0])
print(b[-1])

# 方法 :
# count()       查找出现次数
print(b.count(10))

# index()       查找第一次出现位置
print(b.index(10))

 