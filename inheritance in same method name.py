#inheritance in same method name
"""
class a:
    def a_fun(self):
        print("hai")

class b(a):
    def a_fun(self):
        print("Hello")

obj=b()
obj.a_fun()
obj.a_fun()

class a:
    def a_fun(self):
        print("hai")

class b():
    def a_fun(self):
        print("Hello")

class c(a,b):
    def a_fun(self):
        print("from c")
        
obj=c()
obj.a_fun()
"""

class a:
    def a_fun(self):
        print("hai")

class b():
    def a_fun(self):
        print("Hello")

class c(a,b):
    pass
        
obj=c()
obj.a_fun()

