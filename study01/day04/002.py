# BMI计算 calculate_BMI
def calculate_BMI(weight,hight):
    BMI = weight / (hight ** 2)
    return BMI

weight = float(input("体重(kg)："))
hight  = float(input("身高(m)："))
BMI = calculate_BMI(weight,hight)
if BMI < 18.5:
    BMI_status = "偏瘦"
elif BMI < 25: 
    BMI_status = "正常" 
elif BMI < 30:
    BMI_status = "偏胖"
else:
    BMI_status = "肥胖"
print("BMI为", f"{BMI:.2f}", "您的BMI分类为：", BMI_status)
