#multiple decorator
"""
def decor1(ref):
    def process1():
        data=ref()
        return data.upper()
    return process1

def decor2(ref):
    def process2():
        data=ref()
        return data.split()
    return process2

def myfunction():
    return "happy morning"

myfun=decor2(decor1(myfunction))
print(myfun())
  """
def decor1(ref):
    def process1():
        data=ref()
        return data.upper()
    return process1

def decor2(ref):
    def process2():
        data=ref()
        return data.split()
    return process2

@decor2
@decor1
def myfunction():
    return "happy morning"

print(myfunction())
