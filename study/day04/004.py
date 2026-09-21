# 学生类
class Student:
    def __init__(self,name,count):
        self.name = name
        self.count = count
        self.score_C = 0
        self.score_M = 0
        self.score_E = 0
        
    def Score(self,score_C,score_M,score_E):
        self.score_C = score_C
        self.score_M = score_M
        self.score_E = score_E

    def print_score(self):
        print("姓名：%s,学号：%s"%(self.name,self.count))
        print("语文成绩：%d,数学成绩：%d,英语成绩：%d"%(self.score_C,self.score_M,self.score_E))

stu_01 = Student("aa", "23323")
stu_01.Score(85,90,88)
stu_01.print_score()

print(stu_01.name)
print(stu_01.count)
print(stu_01.score_C)
print(stu_01.score_M)
print(stu_01.score_E)
