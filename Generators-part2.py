def sample():
    for i in range(10):
        if(i%2==0):
            yield i

for i in sample():
    print(i)
print("=============================")

def ten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n = n+1
obj=ten()

for i in obj:
    print(i)
print("=============================")

def fibo(max):
    a,b=0,1
    while True:
        c=a+b
        if c<max:
            print("before")
            yield c
            print("after")
            a=b
            b=c
        else:
            break
obj=fibo(10)
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())

