# 对象和类
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self):
        print("喵"*self.age)

cat_01 = Cat("aa", 3)
print(cat_01.name)
cat_01.speak()