#encapsulation-part1
#access specifiers
#1)public
#2)private
#3)protected

class test:
     def details(self,name,age):
         self.name=name
         self.age=age

obj=test()
obj.details("yuva",23)
print("name is:",obj.name)
print("age is:",obj.age)

"""
class test:
     def details(self,name,age):
         self.name=name
         self.age=age
obj=test()
obj.details("yuva",23)
obj.name="praveen"
print("name is:",obj.name)
print("age is:",obj.age)
"""
