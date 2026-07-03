#decorator
#@property decorator
#nested function
#return function from another function
#function as reference

"""
def outer():
    msgl="happy"
    def inner():
        msg2="learning"
        msg=msg1+msg2
        return msg
    return inner
obj=outer()
print(obj())

def simple():
    print("hello")
print(simple)
"""
def outer(x):
    def inner(y):
        return x + y
    return inner
add=outer(5)
print(add)
result=add(6)
print(result)

