#recursion function program

#function with recursion
def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
factorial=fact(5)
print("The Factorialm is :",factorial)
