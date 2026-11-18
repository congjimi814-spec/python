# 学生类2
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_grades(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade
        else:
            print("课程不存在")
            
    def print_grades(self):
        print(f"学生{self.name}学号{self.id}的成绩如下：")
        for course in self.grades:
            print(f"{course}成绩：{self.grades[course]}")

stu01 = Student("aa", "23323")
stu01.set_grades("语文", 85)
stu01.print_grades()