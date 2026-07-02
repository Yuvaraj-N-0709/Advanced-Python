"""
class details:
    def setname(self,n):
        self.__name=n
    def getname(self):
        return self.__name
    def display(self):
        print("student name:",self.getname())
obj=details()
obj.setname("yuvaraj")
obj.display()

class details:
    def setname(self,n):
        self.__name=n
    def getname(self):
        return self.__name
    def display(self):
        print("student name:",self.__name())
obj=details()
obj.setname("yuvaraj")
obj.display()
"""

class details:
    def setname(self,n):
        self.__name=n
    def getname(self):
        return self.__name

    def setage(self,a):
        self.__age=a
    def getage(self):
        return self.__age
    def display(self):
        print("student name:",obj.getname())
        print("student age:",self.__age())
obj=details()
obj.setname("yuvaraj")
obj.setage(23)
obj.display()
