# 文件的编写
# with open('study/day06/test0.txt', 'w', encoding='utf-8') as f:
#     f.write('Hello, World!\n')

# 同时读写
# with open('study/day06/test0.txt', 'r+', encoding='utf-8') as f:
#     content = f.read()
#     print(content)
#     f.write('This is a new line.\n')

# 追加模式
with open('study/day06/test0.txt', 'a', encoding='utf-8') as f:
    f.write('This line is appended.\n')