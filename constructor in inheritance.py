#constructor in inheritance
"""
class a:
    def __init__(self):
        print(" i am from init a")
    def fun1(self):
        print("i am from 1")

class b(a):
    def fun2(self):
        print("i am from 2")

obj=a()



class a:
    def __init__(self):
        print(" i am from init a")
    def fun1(self):
        print("i am from 1")

class b(a):
    def fun2(self):
        print("i am from 2")

obj=b()


class a:
    def __init__(self):
        print(" i am from init a")
    def fun1(self):
        print("i am from 1")

class b(a):
    def __init__(self):
        print(" i am from init b")
    def fun2(self):
        print("i am from 2")

obj=b()


class teacher:
    def __init__(self):
        print("teacher")
class student(teacher):
    def fun(self):
        print("student")

s=student()
s.fun()


class teacher:
    def __init__(self):
        self.sub="computer science"
        print("i am teacher")
        print("handling subject:",self.sub)
class student(teacher):
    def fun(self):
        print("i am student")

s=student()
s.fun()
"""

class teacher:
    def __init__(self):
        self.sub="computer science"
        print("i am teacher")
class student(teacher):
    def fun(self):
        print("i am student")
        print("favourite subject:",self.sub)


s=student()
s.fun()

