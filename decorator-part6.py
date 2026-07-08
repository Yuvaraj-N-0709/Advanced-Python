def outer(val):
    def decor1(ref):
        def process1():
            data=ref()
            return data.upper() +val
        return process1
    return decor1

@outer("  sakthi")
def myfunction():
    return "happy learning"
print(myfunction())
