# Inheritance  ---- resueablity code
"""
class parent:
    def function1(self):
        print("parent class")


class child(parent):
    def  function2(self):
        print("child class")

obj=child()
obj.function1()
obj.function2()
"""

class person:
    def details(self):
        name="yuvaraj"
        age=23
        gender="Male"
        print("Employee name:",name)
        print("Employee age:",age)
        print("Employee gender:",gender)
class update(person):
    def details_update(self):
        city="karur"
        print("Employee city:",city)

obj=update()
obj.details()
obj.details_update()
