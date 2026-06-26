"""
class a:
    def __init__(self):
        print("i am from a")
    def fun1():
        print(" i am fun 1")

class b(a):
    def __init__(self):
        super().__init__()
        print("i am from b")
    def fun2(self):
        print(" i am fun 2")

obj=b()
obj.fun2()

class a:
    def __init__(self):
        print("i am from a")
    def fun1():
        print(" i am fun 1")

class b:
    def __init__(self):
        print("i am from b")
    def fun2(self):
        print(" i am fun 2")

class c(a,b):
    def __init__(self):
        print("i am from c")

obj=c()


class a:
    def __init__(self):
        print("i am from a")
    def fun1():
        print(" i am fun 1")

class b:
    def __init__(self):
        print("i am from b")
    def fun2(self):
        print(" i am fun 2")

class c(a,b):
    pass

obj=c()
"""

class a:
    def __init__(self):
        print("i am from a")
    def fun1():
        print(" i am fun 1")

class b:
    def __init__(self):
        print("i am from b")
    def fun2(self):
        print(" i am fun 2")

class c(a,b):
    def __init__(self):
        super().__init__()
        print("i am from c")

obj=c()
