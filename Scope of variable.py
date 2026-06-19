"""
 Global_variable="haii"
def local():
    local_variable="i am local variable"
    print(local_variable)
local()
print(Global_variable)
print(local_variable)
"""
#accessing within function
"""
var="happy to see you"
def greet():
   # var="god bless you"
    print("inside call:",var)
greet()
print("outside call:",var)
"""
#if need to change global variable value with in function
"""
var="happy to see you"
def greet():
    global var
    var="bye bye"
    print("inside call:",var)
greet()
print("outside call:",var)
"""
#global and local having same name
"""
var="happy to see you"
def greet():
    var="god bless you"
    print("inside call:",var)
    print(globals()['var'])
greet()
print("outside call:",var)
"""


var="happy to see you"
def greet():
    var="god bless you"
    print("inside call:",var)
    globals()['var']="bye take care..."
    print(globals()['var'])
greet()
print("outside call:",var)
