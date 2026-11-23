# str 字符串常用方法
s = "ciallo"

# find() 查找子串,返回第一次出现的索引位置,找不到返回-1
index = s.find('l')
print(index)

# count() 统计出现次数
index = s.count('l')
print(index)

# upper() 字母转换为大写
print(s.upper())

# lower() 字母转换为小写
print(s.lower())

# split('') 将字符串按指定分隔符分割长列表
split_str = s.split("l")
print(split_str)

# strip() 去除两端指定或空白字符
strip_str = s.strip('c')
print(strip_str)

# replace('','') 将字符串中指定字串替换为新的字串
replace_str = s.replace("l","_")
print(replace_str)

# startswitch('') 检查字符串是否易指定字串开头,返回True/False
print(s.startswith("c"))
print(s.startswith("l"))