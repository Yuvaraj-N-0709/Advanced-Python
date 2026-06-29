#operator overloading
"""
a=10
b=20
print(a+b)

a=10
b=20
int.__add__(a,b)

a="happy"
b="morning"
str.__add__(a,b)

a="happy"
b=20
int.__add__(a,b)
"""

class student:
    def __init__(self,mark1,mark2):
        self.m1=mark1
        self.m2=mark2

    def __add__(self,temp):
        first_stu=self.m1+self.m2
        second_stu=temp.m1+temp.m2
        total=student(first_stu,second_stu)

s1=student(10,20)
s2=student(30,50)
total=s1+s2

print(total.m1)
print(total.m2)

        
