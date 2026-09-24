# 文件的读取
# f = open("study/day06/test.txt", "r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()


# with open("study/day06/test.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)



# with open("study/day06/test.txt", "r", encoding="utf-8") as f:
#     print(f.readline())   # 读取一行
#     print(f.readline())   # 读取一行


with open("study/day06/test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()   # 读取所有行到列表中
    for line in lines:
        print(line)   # 打印每一行