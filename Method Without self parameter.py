#With classes,variable and object
"""
class person():
    name=""
    age=0
    gender=""

person1=person()
person1.name="yuvaraj"
person1.age=23
person1.gender="male"

person2=person()
person2.name="praveen"
person2.age=23
person2.gender="male"

print("my name is:",person1.name)
print("age is :",person1.age)
print("gender is:",person1.gender)

print("my name is:",person2.name)
print("age is :",person2.age)
print("gender is:",person2.gender)


class person():
    name=""
    age=0
    gender=""
    def print_details(self):
        print("my name is:",c.name)
        print("age is :",c.age)
        print("gender is:",c.gender)
c=person()
c.name="yuvaraj"
c.age=23
c.gender="male"
c.print_details()
"""

class Room:
    length =0.0
    breadth =0.0
    def calculate_area(self):
        print("Aera of Room :",room1.length*room1.breadth)

room1=Room()

room1.length =42.5
room1.breadth=30.0

room1.calculate_area()


class Room:
  
    def calculate_area(self):
          length =0.0
          breadth =0.0
          print("Aera of Room :",self.length * self.breadth)

room1=Room()

room1.length =42.5
room1.breadth=30.0

room1.calculate_area()
