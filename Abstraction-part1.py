"""
class a:
    def method1(self):
        print("i am from method1")

obj=a()
obj.method1()

from abc import ABC,abstractmethod

class a(ABC):
    @abstractmethod
    def method1(self):
        print("i am from method1")
obj=a()
obj.method1()


from abc import ABC,abstractmethod

class a(ABC):
    @abstractmethod
    def method1(self):
        pass
"""  
from abc import ABC,abstractmethod

class a(ABC):
    @abstractmethod
    def method1(self):
        pass
class b(a):
    def method1(self):
        print("i am from class b")
obj=b()
obj.method1()
