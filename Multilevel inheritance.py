#multilevel inheritance

class one:
    def function1(self):
        print("class 1")

class two(one):
    def function2(self):
        print("class 2")

class three(two):
    def function3(self):
        print("class 3")

test=three()
test.function1()
test.function2()
test.function3()


