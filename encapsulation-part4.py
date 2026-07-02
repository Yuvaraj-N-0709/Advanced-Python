class details:
    _name="yuva"
    _roll=23
    def display(self):
        print(self._name)
        print(self._roll)
obj=details()
obj.display()


class base:
    def __init__(self):
        self._name="yuva"
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._name)
        self._name="yuvaraj"
        print(self._name)
obj1=derived()
obj2=base()
print(obj1._name)
print(obj._name)
