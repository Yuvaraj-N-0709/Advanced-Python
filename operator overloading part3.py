class A:
    def __init__(self,value):
        self.value=value
    def __gt__(self,other):
        if(self.value > other.value):
            return True
        else:
            return False
obj1=A(20)
obj2=A(30)
if(obj1 > obj2):
    print("object1 is greater than object2")
else:
    print("object2 is greater then object1")


class A:
    def __init__(self,value):
        self.value=value
    def __lt__(self,other):
        if(self.value < other.value):
            return "object1 is greater than object2"
        else:
            return "object2 is greater then object1"
obj1=A(2)
obj2=A(3)
print(obj1 < obj2)
  
class A:
    def __init__(self,value):
        self.value=value
    def __eq__(self,other):
        if(self.value == other.value):
            print("both are equl")
        else:
            print("not equal")
obj1=A(9)
obj2=A(9)
obj1==obj2
