#type of method
#static method

class demo:
    @staticmethod
    def static_method():
        print("i am static method")
demo.static_method()

class myclass:
    def method(self):
        return "instance method called",self
    @classmethod
    def classmethod(cls):
        return "class method class",cls
    @staticmethod
    def staticmethod():
        return "static method called"
obj=myclass()
print(obj.method())
print(myclass.method(obj))
print(obj.classmethod())
print(obj.staticmethod())

    

class methodtype:
    name="happy"

    def instancemethod(self):
        self.lastname="learning"
        print(self.name,self.lastname)
    @classmethod
    def classmethod(cls):
        cls.name ="happyyyy"
        print(cls.name)
        print(m.lastname)
    @staticmethod
    def staticmethod():
        print("this is a static method")
        print(m.lastname)
m=methodtype()
m.instancemethod()

methodtype.classmethod()
methodtype.staticmethod()
