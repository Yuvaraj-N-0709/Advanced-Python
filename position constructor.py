#position comstructor

#default
class student:
    def __init__(self,name,age=30):
        self.name=name
        self.age=age
    def print1(self):
        print("my name is:",self.name)
        print("my age is:",self.age)
stu=student("yuvaraj",23)
stu.print1()


class student:
    def __init__(self,name="yuva",age=30):
        self.name=name
        self.age=age
    def print1(self):
        print("my name is:",self.name)
        print("my age is:",self.age)
stu=student()
stu.print1()


class test:
    z=0
    def __init__(self,x,*y):
        z=x
        for i in y:
            z=z+i
        print("sum:",z)
obj=test(10,20,30,40)
