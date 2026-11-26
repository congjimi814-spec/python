# def 函数 默认参数(缺省参数)
def reg_stu(name,age,gender = "男",city = "塔"):
    print(f"姓名:{name} 年龄:{age} 性别:{gender} 城市:{city} ")
    return {"name":name,"age":age,"gender":gender,"city":city}

reg_stu("AC",31)

reg_stu("CC",41,"女")

reg_stu("EA",31,city = "ciallo")   #前方有默认参数时后位的默认参数单独赋值只能使用关键词
