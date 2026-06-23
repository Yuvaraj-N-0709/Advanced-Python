"""
class person():
    def get_details(self):
        name="yuvaraj"
        age=23
        gender="male"
        print("my name:",name)
        print("age is:",age)
        print("gender is :",gender)
c=person()
c.get_details()

class person():
    def get_details(self):
        name="yuvaraj"
        age=23
        gender="male"
    def print_details(self):
        print("my name:",name)
        print("age is:",age)
        print("gender is :",gender)
c=person()
c.get_details()
c.print_details()

class person():
    def get_details(self):
        self.name="yuvaraj"
        self.age=23
        self.gender="male"
    def print_details(self):
        print("my name:",self.name)
        print("age is:",self.age)
        print("gender is :",self.gender)
c=person()
c.get_details()
c.print_details()
"""
class person():
    def get_details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print_details(self):
        print("my name:",self.name)
        print("age is:",self.age)
        print("gender is :",self.gender)
c=person()
c.get_details("yuvaraj",23,"male")
c.print_details()
d=person()
d.get_details("praveen",23,"male")
d.print_details()
