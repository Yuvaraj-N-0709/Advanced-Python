#demo2
"""
import demo1
print("demo2:",__name__)
"""
from demo1 import message
def greeting():
    print("good afternoon")
def message_new():
    message()
    print("how are you")
def main():
    greeting()
    message_new()
main()
print("second:",__name__)
