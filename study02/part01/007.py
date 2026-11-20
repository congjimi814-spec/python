# 逻辑 比较运算符
# case1 判断数字是否在10-20
num = int(input("请输入一个数字："))
if(num >= 10 and num <= 20):
    print("YES")
else:
    print("NO")

# case2 判断数字是否不在10-20
num = int(input("请输入一个数字："))
if(num < 10 or num > 20):
    print("YES")
else:
    print("NO")