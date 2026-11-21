# if 条件判断
# case1 判断闰年
year = int(input("年份:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}是闰年")
else :
    print(f"{year}不是闰年")



# case2 判断三角形
a,b,c = int(input("边长a:")),int(input("边长b:")),int(input("边长c:"))

if a + b > c and a + c > b and b + c > a:
    print("可以构成三角形")
    if a == b and b == c:
        print("等边三角形")
    elif a == b or a == c or b == c:
        print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("不能构成三角形")