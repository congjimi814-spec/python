# list常见内置功能
a = [10,12,60,"ABC",True,False]

# append:在列表尾部追加元素  对象.方法名(数据)
a.append(None)
print(a)

# insert:在指定位置插入元素  对象.方法名(索引,数据)
a.insert(0,'ciallo~')
print(a)

# remove:删除指定元素  对象.方法名(数据)
a.remove(12)
print(a)

# pop:删除指定索引的元素,默认删除最后一个元素  对象.方法名(索引)
a.pop(0)
print(a)

# sort:对列表进行排序  对象.方法名()
# reverse:对列表进行反转  对象.方法名()
c = [1,3,5,2,4]
print(c)
c.sort()
print(c)
c.reverse()
print(c)

# 常用函数:min();max();sum();len()
print(min(c))
print(max(c))
print(sum(c)/len(c))