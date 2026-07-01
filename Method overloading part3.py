!pip install multipledispatch

from multipledispatch import dispatch

class a:
    @dispatch(int,int)
    def add(a,b):
        print(a+b)
    
    @dispatch(float,float,float)
    def add(a,b,c):
        print(a+b+c)
    
    @dispatch(int,int,int)
    def add(a,b,c):
        print(a+b+c)

obj=a()
obj.add(90,10)
obj.add(3.5,3.5,3.0)
obj.add(80,15,5)
