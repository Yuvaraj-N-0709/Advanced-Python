class demo:
    def __init__(self,fun):
        self.fun = fun
    def __call__(self,a,b):
        value=self.fun(a,b)
        return value+5
@demo
def multiple(a,b):
    return a*b
print(multiple(2,2))


class decorator:
    def __init__(self,function):
        self.function=function
    def __call__(self , *args,**kwargs):
        self.function(*args,**kwargs)

@decorator
def function(name,message="hello"):
    print("{},{}".format(message,name))
function("happy morning" ,"yuvaraj")
