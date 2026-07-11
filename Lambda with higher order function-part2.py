x=lambda a,b,c : a + b+ c
print(x(5,6,2))
print("=======================================")

add=lambda x,y=20,z=10: x+y+z
print(add(5))
print("=======================================")

add=lambda x,y=20,z=10: x+y+z
print(add(5,2))
print("=======================================")
add=lambda *args :sum(args)
print(add(10,20,30,40,50,60,70,80,90,100))
print("=======================================")
(lambda a,b :a*b)(10,20)
print("=======================================")

l1=[4,2,13,21,5]

l2=[]
for i in l1:
    temp=lambda i:i**2
    l2.append(temp(i))
print(l2)
