#multiple function with single decorator
def divide_decorator(fun):
    def process(*args):
        if 0 in args[1:]:
            return "pleace enter number other than zero"
        return fun(*args)
    return process
@divide_decorator
def divide(a,b):
    return a/b
print(divide(10,0))
@divide_decorator
def divide(a,b,c):
    return a/b/c
print(divide(10,5,0))
