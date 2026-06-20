#recursion function(if the function run again and again is called recursion function)
"""sample example
def greeting():
    print("good morning..!")
greeting()
"""

"""Example
def greeting():
    print("good morning..!")
    greeting()
greeting()
"""

#check the limit
"""
i=0
def greeting():
    global i
    i=i+1
    print("good morning..!:::",i)
    greeting()
greeting()
"""

#set the recursion lmit

import sys
sys.setrecursionlimit(1500)
print(sys.getrecursionlimit())


i=0
def greeting():
    global i
    i=i+1
    print("good morning..!:::",i)
    greeting()
greeting()
