#Hirearchial inheritance


class parent:
    def name(self):
        print("mothe name : annalakshmi")
        print("father name: narayanaamy")

class child(parent):
    def child_name(self):
        print("child 1 name :yuva")

class child2(parent):
    def child_name2(self):
        print("child 2 name is : nambu")

obj1=child()
obj2=child2()

obj1.name()
obj1.child_name()

obj2.name()
obj2.child_name2()
