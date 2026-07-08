#class decorator
class example:
    def __init__(self):
        print("i am from constructor")
    def __call__(self):
        print("i am from call method")

obj=example()
obj()

class demo:
    def __init__(self):
        print("i am from constructor")
    def __call__(self,a,b ):
        print("i am from call method")
        print(a*b)

obj=demo()
obj(10,20)


class example:
    def __init__(self):
        print("i am from constructor")
    def __call__(self):
        print("i am from call method")
    def display(self):
        print("hai")

obj=example()
obj.display()
obj()


class mydecorator:
    def __init__(self, function):
        self.function=function
    def __class__(self):
        self.function()

def function():
    print("happy morning")
obj=mydecorator(function)
obj()


class mydecorator:
    def __init__(self, function):
        self.function=function
    def __class__(self):
        self.function()
@mydecorator
def function():
    print("happy morning")
function()
