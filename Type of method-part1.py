#types of method
#instance method
#class method
#static method


#instance method
class demo:
    def method1(self):
        print("i am from method 1")
obj=demo()
obj.method1()

class demo:
    def method1(self,a,b):
        print("added value:",a+b)
obj=demo()
obj.method1(10,20)

class demo:
    def method1(self,a,b):
        print("added value:",a+b)
obj=demo()
obj.method1(10,20)
obj1=demo()
obj1.method1(100,20)

#class method

class demo:
    def method1(self,a,b):
        print("added value:",a+b)
    @classmethod
    def method2(cls):
        print("i am from class method")
obj=demo()
obj.method1(10,20)
ob.method2()
demo.method2()

class demo:
    var=" i am class variable"
    def method1(self,a,b):
        print("added value:",a+b)
    @classmethod
    def method2(cls):
        print("i am from class method")
        print(cls.var)
obj=demo()
obj.method1(10,20)
demo.method2()

class demo:
    var=" i am class variable"
    def method1(self,a,b):
        print("added value:",a+b)
    @classmethod
    def method2(cls):
        print("i am from class method")
        print(cls.var)
obj=demo()
obj.method1(10,20)
demo.method2()
demo.method2()#method2
demo.method2(obj,20,9)
