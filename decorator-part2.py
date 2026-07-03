def function1():
    print("function1")
def function2():
    print("function2")
function1()
function2()

print("======")

def function1():
    print("function1")
def function2(ref):
    ref()
    print("function2")
print(function1)
function2(function1)

def add(x,y):
    return x+y
def display(fun,x,y):
    return fun(x,y)
result = display(add,4,6)
print(result)
print(add)

print("=====")

def upper(text):
    return text.upper()

def lower(text):
    return text.lower()

def text(fun):
    msg=fun("happy learning")
    print(msg)
text(upper)
text(lower)
