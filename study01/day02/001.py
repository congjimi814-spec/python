# BMI = 体重/身高**2
weight = float(input("请输入体重(kg): "))
height = float(input("请输入身高(m): "))
bmi = weight / height ** 2
print(f"您的BMI值为: {bmi:.2f}")

if bmi < 18.5:
    print("体重过轻")
elif bmi < 24:
    print("体重正常")
elif bmi < 30:
    print("体重过重")
else:
    print("肥胖")