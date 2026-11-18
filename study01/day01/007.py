# if条件
money = input("请输入金额：")
money = int(money)
if money>10:
    print("吃得起饭")
elif money>6:
    print("凑合能吃")
else:
    print("吃不起饭")