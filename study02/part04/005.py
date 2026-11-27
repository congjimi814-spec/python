# def 函数参数
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def calc(x,y,oper):
    return oper(x,y)

print(calc(2,3,add))
print(calc(2,3,subtract))