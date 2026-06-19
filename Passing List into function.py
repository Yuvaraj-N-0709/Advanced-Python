#passing List into function
def list(value):
    even=0
    odd=0
    for i in value:
        if i%2==0:
            even=even+1
        else:
           odd=odd+1
    return even , odd
value=[12,23,14,12,14,141,45,171,8,18,1,75,65,555]
even,odd=list(value)
print("Even number count:",even)
print("odd number counrt:",odd)
