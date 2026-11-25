# dict 字典
# 键值对(key value)类型数据 通过键找到值 键无法重复(重复后值覆盖前值)
# key类型不可变 不能为 list set dict

# 定义
dict_1 = {}
dict_2 = dict()     #空字典

dict1 = {"AA":100,"BB":321,"AB":459}
print(dict1)
print(type(dict1))

# 访问
print(dict1["AB"])
dict1["AB"] = 200              #修改
print(dict1["AB"])

# 操作:
dict1 = {"AA":100,"BB":888,"AB":459}

# 添加或修改数据:字典名称[key] = value
dict1["OS"] = 200              #添加
print(dict1)
dict1["AB"] = 231              #修改
print(dict1["AB"])

# 删除:pop(key)方法 ; del + 字典名称[key]
value = dict1.pop("BB")
print(value)
print(dict1)

del dict1["AA"]
print(dict1)

# 查询:根据key ; get(ket); keys()所有的key ;values()所有的value ; items()所有键值对
print(dict1["AB"])
print(dict1.get("OS"))

print(dict1.keys())
print(dict1.values())
print(dict1.items())

# 遍历
for k in dict1.keys():
    print(k)

for k,v in dict1.items():
    print(f"{k} : {v}")