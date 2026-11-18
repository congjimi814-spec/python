# 父类 子类 员工原理
class Empolyee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"姓名:{self.name},工号:{self.id}")

class FulltimeEmpolyee(Empolyee):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary = salary

    def print_info(self):
        super().print_info()
        print(f"工资:{self.salary}")

class ParttimeEmpolyee(Empolyee):
    def __init__(self,name,id,daily_salary,worked_days):
        super().__init__(name,id)
        self.daily_salary = daily_salary
        self.worked_days = worked_days

    def print_info(self):
        super().print_info()
        print(f"日薪:{self.daily_salary},工作天数:{self.worked_days}")