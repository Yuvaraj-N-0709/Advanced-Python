#polymorphism with class methods
"""
class one:
    def name(self):
        print("my name is yuva")
    def age(self):
        print("i am 23 years old")
    def gender(self):
        print("male")
class two:
    def name(self):
        print("my name is praveen")
    def age(self):
        print("i am 23 years old")
    def gender(self):
        print("male")
obj1=one()
obj2=two()
for i in (obj1,obj2):
    i.name()
    i.age()
    i.gender()
"""
class one:
    def name(self):
        print("my name is yuva")
    def age(self):
        print("i am 23 years old")
    def gender(self):
        print("male")
class two:
    def name(self):
        print("my name is praveen")
    def age(self):
        print("i am 23 years old")
    def gender(self):
        print("male")
def fun_cal(obj):
    obj.name()
    obj.age()
    obj.gender()
obj1=one()
obj2=two()
fun_cal(obj1)
fun_cal(obj2)
