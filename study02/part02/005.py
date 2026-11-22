# 随机数
import random

random_number = random.randint(1,100)
number = int(input("请输入一个1到100之间的整数:"))
while True:
    if number < random_number:
        print("你输入的数字小了")
        number = int(input("请重新输入一个整数:"))
    elif number > random_number:
        print("你输入的数字大了")
        number = int(input("请重新输入一个整数:"))
    else:
        print(f"正确,数字为{random_number}")
        break