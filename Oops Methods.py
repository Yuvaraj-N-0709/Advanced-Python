#oops
"""
class text():
    def msg():
        print("hello")
a.text()
msg()

class text():
    def msg():
        print("hello")
a=text()
a.msg()

class text():
    def msg(self):#self ku pathula namba enna name venumunalum use pannalam
        print("hello")
a=text()
a.msg()

class text():
    def msg(self):
        print("hello")
a=text()
b=text()
a.msg()
b.msg()

class text():
    def msg(self):
        print("hello")
a=text()
text.msg(a)
"""
class text():
    def msg(self):
        print("hello")
a=text()
b=text()
text.msg(a)
text.msg(b)

