#default Argument
"""
def person(name,age=18):
    print("name:",name)
    print("age:",age)
person("yuvaraj N")


def person(name,age=18):
    print("name:",name)
    print("age:",age)
person("yuvaraj N",23)




def person(name,age=18):
    print("name:",name)
    print("age:",age+2)
person("yuvaraj N",23)


#def person(name="Yuvaraj",age):
 #   print("name:",name)
 #   print("age:",age)
#person(23)


def person(age,name="Yuvaraj"):
    print("name:",name)
    print("age:",age)
person(23)


def person(name="Yuvaraj"):
    print("name:",name)
person()
"""

#variable length Argument
"""
def add(a,b):
    c=a+b
    print("sum:",c)
add(10,30)


def add(a,b):
    c=a+b
    print("sum:",c)
add(10,30,20,50,10)


def add(a,*b):
    c=a+b
    print("sum:",c)
add(10,30,10,50)

def add(a,*b):
    print(a)
    print(b)
    c=a+b
    print("sum:",c)
add(10,30,10,50)
"""

def add(a,*b):
    c=a
    for i in b:
        c=c+i
    print("sum:",c)
add(50,20,30)


def add(*b):
    c=0
    for i in b:
        c=c+i
    print("sum:",c)
add(50,20,30)

