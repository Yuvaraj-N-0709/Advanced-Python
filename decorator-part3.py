def greeting(name):
    def hello():
        return "hello,"+name
    print("hello ref:",hello)
    return hello
call = greeting("yuvaraj")
print(call())
print("call num:",call)


print("======")

def upperstring(ref):
    def process():
        data=ref()
        return data.upper()
    return process
def myfunction():
    return "happy morning"
output=upperstring(myfunction)
print(output())
 
