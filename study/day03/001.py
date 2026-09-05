# while 循环求任意值的平均
print("请输入任意个数的值,输入q结束:")
a = 0
sum = 0
count = 0
while True:
    count = count + 1
    a=input("请输入第"+str(count)+"个值：")
    if a == "q":
        break
    sum = sum + int(a)
count = count - 1
average = sum/count
print("平均值为：",average)