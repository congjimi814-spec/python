# 函数
# 计算扇形的面积
def calculate_sector(angle, radius):
    area = (angle / 360) * 3.14 * radius ** 2
    return area 

angle_0 = int(input("请输入扇形的角度："))
radius_0 = int(input("请输入扇形的半径："))


print("扇形的面积为：", calculate_sector(angle_0, radius_0))

print(calculate_sector(90, 10))  # 计算角度为90，半径为10的扇形面积
print(calculate_sector(180, 5))  # 计算角度为180，半径为5的扇形面积
print(calculate_sector(270, 8))  # 计算角度为270，半径为8的扇形面积