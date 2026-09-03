# BMI = 体重/身高**2
weight = float(input("请输入体重(kg): "))
height = float(input("请输入身高(m): "))
bmi = weight / height ** 2
print(f"您的BMI值为: {bmi:.2f}")