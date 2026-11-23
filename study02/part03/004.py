# 字符串 str
# 特点:正反向索引;不可变性;有序性;可迭代性(遍历)
# 切片操作 序列对象[开始索引(默认0):结束索引(默认-1):步长(默认1)]
str = "ciallo"

# 索引
print(str)
print(str[0],str[2],str[5])

# 遍历
for i in str:
    print(i)

# 切片
print(str[0:2])
print(str[0:-1:2])
print(str[-1:-7:-1])  #反转