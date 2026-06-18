#Add Two function
def add():
    a=10
    b=20
    c=a+b
    print("The sum is:",c)
add()

#add value
def add(a,b):
    c=a+b
    print("The Add two number :",c)
add(20,20)

#sub value
def sub(a,b):
    c=a-b
    print("The Sub two number :",c)
sub(40,20)

#add 2nd value
def add(a,b=50):
    c=a+b
    print("The ad two number :",c)
add(40)

#add two values..
def add(a,b=50):
    c=a+b
    print("The ad two number :",c)
add(40,20)
