#method overloading

class a:
    def fun(self,a=None,b=None,c=None):
        if (a!=None and b!=None and c!=None):
            print(a+b+c)
        elif(a!=None and b!=None):
            print(a+b)
        else:
            print(a)
obj=a()
obj.fun(10,20,30)
                 
