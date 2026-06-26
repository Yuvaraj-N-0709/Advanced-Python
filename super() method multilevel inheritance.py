"""
class a:
    def function1(self):
        print("class a")

class b(a):
    def function2(self):
        print("class b")
        super().function1()

class c(b):
    def function3(self):
        print("class c")
        super().function2()

c=c()
c.function3()

class a:
    def function(self):
        print("class a")

class b(a):
    def function(self):
        print("class b")
        super().function()

class c(b):
    def function(self):
        print("class c")
        super().function()

c=c()
c.function()
"""
class a:
    def __init__(self):
        print("constructo- class a")
        
    def function(self):
        print("class a")

class b(a):
    def __init__(self):
        print("constructo- class b")
        super().__init__()
        
    def function(self):
        print("class b")
        super().function()

class c(b):
     def __init__(self):
        print("constructo- class c")
        super().__init__()
        
     def function(self):
        print("class c")
        super().function()

c=c()
c.function()
