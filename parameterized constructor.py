#--parameterized constructor
"""
class student:
    def __init__(self,name,age):
        print("my name is:",name)
        print("my age is:",age)
stu=student("yuvaraj",23)


class student:
    def __init__(self,name,age):
        age=20
        print("my name is:",name)
        print("my age is:",age)
stu=student("yuvaraj",23)        

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print1(self):
        print("my name is:",self.name)
        print("my age is:",self.age)
stu=student("yuvaraj",23)
stu.print1()

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print1(self):
        print("my name is:",self.name)
        print("my age is:",self.age)
stu=student("yuvaraj",23)
stu=student("praveen",23)
stu.print1()
"""

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print1(self):
        print("my name is:",self.name)
        print("my age is:",self.age)
stu=student("yuvaraj",23)
stu.print1()
stu=student("praveen",23)
stu.print1()
