#Iterator
#list=[1,2,3,4,5]
#print(list)
"""
list=["hai","hello","how are you","pyhton","happy learning"]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
"""
""" 
#for loop
list=["hai","hello","how are you","pyhton","happy learning"]
for i in list:
     print(i)
"""    
#looping without for loop
#list elements
"""
list=["hai","hello","how are you","pyhton","happy learning"]
i=0
while i<len(list):
    print(list[i])
    i=i+1
"""

list=[1,2,3,4,5,"python"]
iter(list)

list=[1,2,3,4,5]
ite=iter(list)
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))

list1=[1,2,3,4,5,"python"]
ite=iter(list1)
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())
print(ite.__next__())

