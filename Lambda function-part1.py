#lambda function

def name():
    print("hello world")
name()
print("=======================================")
def name(a):
    print("hello world",a)
name("yuvaraj")
print("=======================================")
message=lambda : print("hello world")
message()
print("=======================================")
message=lambda name : print("happy learning",name)
message("yuvaraj")
print("=======================================")
def add(a):
    return a+10
obj=add(5)
print(obj)
print("=======================================")
x=lambda a : a +10
print(x(5))
print("=======================================")
x=lambda a,b : a*b
print(x(5,6))
print("=======================================")
str1="happy morning"
upper=lambda string:string.upper()
print(upper(str1))
print("=======================================")
def cube(y):
    return y*y*y

print("normal function ,cube:",cube(5))
lambda_cube=lambda y: y*y*y
print("using lambda function ,cube:",lambda_cube(5))
