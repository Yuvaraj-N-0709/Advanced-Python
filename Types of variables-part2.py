"""
class details:
    school_name="ABC SCHOOL"
    
    def __init__(self,name,no):
       self.name=name
       self.no=no
    def show(self):
        print(self.name,self.no,details.school_name)

details.school_name ="xyz school"
s1=details("yuvaraj",23)
s1.show()
s2=details("praveen",23)
s2.show()
"""

class details:
    school_name="ABC SCHOOL"
    def __init__(self,name,no):
       self.name=name
       self.no=no
s1=details("yuvaraj",23)
s2=details("praveen",23)

print("object s1")
print(s1.name,s1.no,s1.school_name)
print(s2.name,s2.no,s2.school_name)
print("\n")
s1.school_name="xyz school"
print("object s2")
print(s1.name,s1.no,s1.school_name)
print(s2.name,s2.no,s2.school_name)
