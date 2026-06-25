#hybrid inheritance

class dog:
    def fun1(self):
        print("hello i am dog")

class cat(dog):
    def fun2(self):
        print("hello i am caT")

class cow(dog):
    def fun3(self):
        print("hello i am cow")

class horse(cat,cow):
    def fun4(self):
        print("hello i am horse")

ani=horse()
ani.fun1()
ani.fun2()
ani.fun3()
ani.fun4()
