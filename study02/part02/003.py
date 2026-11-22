# 循环
# while循环
# case1:
i = 0
while i < 5:
    print(f"ciallo~ {i}")
    i +=1
print("循环结束")


# for循环-for增强
# case1:
char = "ciallo ~"
for _ in char:
    print(_)

# range:
# range(end) 0~end-1,step = 1
# range(start, end) start~end-1,step = 1 
# range(start, end, step) start~end-1, step为步长

# case2 1到100 奇数之和:
sum = 0
for i in range(1, 101, 2):
    sum += i
print(f"{sum}")

# case2 100到500 3的倍数之和
sum = 0
for i in range(100, 501):
    if i % 3 == 0:
        sum += i
print(f"{sum}")