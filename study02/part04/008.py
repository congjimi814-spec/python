# 类型注解 (确定变量类型)
# case:
def clc_round(r = 10) -> tuple[float,float]:  #赋默认值 推断传入值的类型 -> 指向返回值类型
    return round(3.14*r*r,1),round(2*3.14*r,1)

al = clc_round(10)
print(al)
