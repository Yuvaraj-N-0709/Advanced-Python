#data abstraction
"""
from abc import ABC,abstractmethod

class a(ABC):
    @abstractmethod
    def method1(self):
        pass
    @abstractmethod
    def method2(self):
        pass
class b(a):
    def method1(self):
        print("i am method1")
obj=b()
obj.method1()
"""
"""
from abc import ABC,abstractmethod

class a(ABC):
    @abstractmethod
    def method1(self):
        pass
    @abstractmethod
    def method2(self):
        pass
class b(a):
    def method1(self):
        print("i am method1")
    def method2(self):
        print("i am method2")  
obj=b()
obj.method1()
"""
from abc import ABC,abstractmethod
class sides(ABC):
    @abstractmethod
    def number(self):
        pass
class triangle(sides):
    def number(self):
        orint("i have 3 sides")
class square(sides):
    def number(self):
        print("i have 4 sides")
class pentagon(sides):
    def number(self):
        print(" i have 5 sides")

t=triangle()
t.number()
s=square()
s.number()
p=pentagon()
p.number()
