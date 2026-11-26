# def 函数传参
def reg_stu(name,age,gender,city):
    print(f"姓名:{name} 年龄:{age} 性别:{gender} 城市:{city} ")
    return {"name":name,"age":age,"gender":gender,"city":city}
# 1.位置传参    一一对应
reg_stu("AA",18,"男","城")

# 2.关键字传参   "键 = 值"形式
reg_stu(name="BB",city="city_0",gender="无",age=60)

# 可以混用..(关键字参在位置参之后)
reg_stu("CD",20,city="city_6",gender="无")
