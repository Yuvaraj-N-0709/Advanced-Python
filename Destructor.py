#destructor destory the object
#deallocate memory
#cleanupresource

class test:
    def __init__(self):
        print("object created")
    def __del__(self):
        print("object deleted")
obj=test()
del obj


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("my name is:",self.name)
        print("my age is:",self.age)
    def __del__(self):
        print("The destructor is called")
obj=person("yuvaraj",23)
del obj
