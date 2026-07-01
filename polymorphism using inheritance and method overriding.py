"""
class a:
    def details(self):
        print("i am from class a")
class b(a):
    def details(self):
        super().details()
        print("i am from class b")
class c(b):
    def details(self):
        super().details()
        print("i am from class c")
obj=c()
obj.details()
"""
class yuva:
    def speak(self):
        return "i am yuva"
class praveen(yuva):
    def speak(self):
        return "i am praveen"
class kalish(praveen):
    def speak(self):
        return "i am kalish"
obj1=yuva()
obj2=praveen()
obj3=kalish()
#obj ={yuva(),preveen(),kalish()}
for i in (obj1,obj2,obj3):
    print(i.speak())
    
