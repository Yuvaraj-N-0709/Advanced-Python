class test:
    def details(self,name,age):
        self.__name=name
        self.__age=age
    def show(self):
        print(obj.__name)
        print(obj.__age)
obj=test()
obj.details("yuva",23)
obj.show()


class school:
    def details(self):
        self.name="ABC school"
        print(self.name)
    def stu1(self):
        print("yuvaraj")
        print("10th")
    def stu2(self):
        print("praveen")
        print("10th")
obj=school()
obj.details()
obj.stu1()
obj.stu2()

class school:
    def details(self):
        self.name="ABC school"
        print(self.name)
    def __stu1(self):
        print("yuvaraj")
        print("10th")
    def stu2(self):
        self.__stu1()
        print("praveen")
        print("10th")
obj=school()
obj.details()
obj.stu2()

class school:
    def details(self):
        self.name="ABC school"
        print(self.name)
    def __stu1(self):
        print("yuvaraj")
        print("10th")
    def __stu2(self):
        print("praveen")
        print("10th")
obj=school()
obj.details()
obj._school__stu1()
obj._school__stu2()
