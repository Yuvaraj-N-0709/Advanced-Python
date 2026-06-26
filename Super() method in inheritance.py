"""
class test:
    def method1(self):
        print("hai i am from method 1")

class test2:
    def method2(self):
        test.method1(self)

t=test2()
t.method2()
"""
class test:
    def method1(self):
        print("hai i am from method 1")

class test2(test):
    def method2(self):
        super().method1()
        print("i am from method 2")

t=test2()
t.method2()
