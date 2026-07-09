class details:

    def fun(self,name,no):
        self.name=name
        self.no=no
        print("NAME:",self.name)
        print("ROOL NO:",self.no)
obj=details()
obj.fun("yuvaaraj",23)

obj1=details()
obj1.fun("praveen",23)


class details:
    school_name="ABC SCHOOL"
    def __init__(self,name,no):
       self.name=name
       self.no=no
s1=details("yuvaraj",23)
print(s1.name,s1.no,details.school_name)
print(s1.school_name)
