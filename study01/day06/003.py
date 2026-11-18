# 捕捉异常 try-except
try:
    weight = float(input("体重(kg):"))
    hight  = float(input("身高(m):"))
    BMI = weight / (hight ** 2)
except ValueError:
    print("输入为不合理数字")
except ZeroDivisionError:
    print("身高不能为0")
except :
    print("未知错误")
else :                          #没有错误时运行
    print("BMI值为:"+BMI)
finally:                        #必定运行
    print("程序结束运行")