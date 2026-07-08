#decorator
"""
def divide(a,b):
    return a/b
print(divide(10,0))
"""
      
def divide_decorator(fun):
    def process(x,y):
        if y==0:
            return "pleace enter number other than zero"
        return fun(x,y)
    return process
@divide_decorator
def divide(a,b):
    return a/b
print(divide(10,5))
