#Encapsulation -part2

class test:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(obj.name)
        print(obj.age)
obj=test()
obj.details("yuva",23)

class test:
    def details(self,name,age):
        self.name=name
        self.age=age
obj=test()
obj.details("yuva",23)
print(obj.name)
print(obj.age)


class test:
    def details(self,name,age):
        self.name=name
        self.age=age
    def Age(self):
        print(self.age)
obj=test()
obj.details("yuva",23)#access public member
print(obj.name)
obj.Age()

class test:
    def details(self,name,age):
        self.__name=name
        self.__age=age
        print(obj.__name)
        print(obj.__age)
obj=test()
obj.details("yuva",23)


class test:
    def details(self,name,age):
        self.__name=name
        self.__age=age
obj=test()
obj.details("yuva",23)
print(obj.__name)
print(obj.__age)

class test:
    def details(self,name,age):
        self.__name=name
        self.__age=age
    print(obj.__name)
    print(obj.__age)
obj=test()
obj.details("yuva",23)
