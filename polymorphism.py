#polymorphism

#(+)operator
num1=10
num2=20
print("tehe added value :",num1+num2)

num1="happy"
num2="morning"
print("the added value:",num1+num2)

#(*)operator
num1=10
num2=20
print("tehe added value :",num1*num2)

num1="happy"
num2=5
print("the added value:",num1*num2)

#function
print(len("happy morning"))

print(len(["happy morning","good","happy"]))

print(len({"name":"yuva","course":"python"}))

#classes

class employee1:
    def info(self):
        name="yuva"
        age=23
        print(name)
        print(age)

class employee2:
    def info(self):
        name="praveen"
        age=25
        print(name)
        print(age)
obj=employee1()
obj1=employee2()
obj.info()
obj1.info()
