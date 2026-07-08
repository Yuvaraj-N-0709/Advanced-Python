#decorator
#closer
#python closure is a nested function that allows to access variable of the outer function
#even after the outer function is closed

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(5)
print(result)


def upperstring(ref):
    def process():
        data=ref()
        return data.upper()
    return process

@upperstring
def myfunction():
    return  "happy morning"
print(myfunction())
