"""
class a:
    def fun(self,*val):
        value=0
        for i in val:
            value=value+i 
        print("Added value:",value)
obj=a()
obj.fun(10,20,30,44,54,34,45)
obj.fun(20,10)
obj.fun(10)
"""

class a:
    def fun(self,a=None,b=None):
        if(a!=None and b!=None and a!=b):
            print("Rectangle area:",a*b)
        else:
            print("square root:",a*a)
obj=a()
obj.fun(20,20)
obj.fun(10)
