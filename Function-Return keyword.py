#print outside function
def add(a,b):
    c=a+b
    print("The Added value is:",c)
add(10,20)
  # print("The Added value is:",c)

#return keyword
def add(a,b):
    c=a+b
    return c
   # print("The Added value is:",result)
add(10,20)


def Gretting():
    print("Hai")
    return
    print("Good Afternon")
Gretting()


def fun(x):
    return x+5
fun(10)

#Expression-list

def great(a,b):
    print(a+b)
print(great(10,20))

def Gretting(x):
    print(x)
print(Gretting("Hello"))


def Gretting(x):
    print(x)
Gretting("Hello")


#add-sub

def add_sub(a,b):
    c=a+b
    c1=a-b
    return c,c1
add_sub(3,2)

def add_sub(a,b):
    c=a+b
    c1=a-b
    return c,c1
addval,subval=add_sub(3,2)
print("The added value:",addval)
print("The subtracted value :",subval)


