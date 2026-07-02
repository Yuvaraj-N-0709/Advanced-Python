class demo:
    def __init__(self):
        self._age=0
    @property
    def age(self):
        print("getter method called")
        return self._age#>return
    @age.setter
    def age(self,a):
        if(a<18):
            print("you are below 18")
        print("setter method called")
        self._age=a#>set
obj=demo()
obj.age=23
print(obj.age)
