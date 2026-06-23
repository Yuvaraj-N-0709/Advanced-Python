#self :: returns to instance of a class
#self :: used to access variable that belongs to the calss
"""
def add(a,b):
    c=a+b
    print(" the added value of ",a,"and",b,"is",c)
add(10,20)

class addition():
    def add(a,b):
        c=a+b
        print(" the added value of ",a,"and",b,"is",c)
a=addition()
a.add(10,20)

class addition():
    def add(self,a,b):
        c=a+b
        print(" the added value of ",a,"and",b,"is",c)
a=addition()
a.add(10,20)
"""

class addition():
    d=20
    def add(self,a,b):
        c=a+b+self.d
        print(" the added value of ",a,b,"and",self.d ,"is",c)
a=addition()
b=addition()
a.add(10,20)
b.add(20,3)
