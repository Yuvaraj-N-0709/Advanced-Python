#lambda filter function


def even(num):
    if num%2==0:
        return True
    else:
        return False
number=[1,2,3,4,5]
filtered=filter(even,number)
print(list(filtered))
print("===============================")
ages=[12,45,18,22,7]
def myfun(x):
    if x >=18:
        return True
    else:
        return False
adults=filter(myfun,ages)
for x in adults:
      print(x)
print("===================================")

seq=[0,1,2,3,4,5,6,7,8,9]
result=filter(lambda x:x%2 !=0,seq)
print(list(result))

result=filter(lambda x: x%2==0,seq)
print(list(result))

print("==================================")
result=filter(lambda x:x%2 !=0,range(1,11))
print(list(result))

result=filter(lambda x: x%2==0,range(1,11))
print(list(result))
