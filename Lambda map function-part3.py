#lambda map function

def addition(n):
    return n + n

number=[1,2,3,4,5]
result=[]

for num in number:
    result.append(addition(num))
print(result)

print("==========================")

def addition(n):
    return n + n
number=(1,2,3,4,5)
result=map(addition,number)
print(list(result))

print("===========================")

num1=[10,20,30]
num2=[40,50,60]
result=map(lambda x,y:x+y,num1,num2)
print(list(result))
print("===========================")

def even(num):
    if num%2==0:
       return "even"
    else:
        return "odd"
number=[1,2,3,4,5]
result=list(map(even,number))
print(result)
