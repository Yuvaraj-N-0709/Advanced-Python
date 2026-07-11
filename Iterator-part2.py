def looping(value):
    it=iter(value)
    while True:
        try:
            item=next(it)
        except StopIteration:
            break
        else:
            print(item)
looping([1,2,3])


print("==========")

class ten:

    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            value=self.num
            self.num+=1
            return value
        else:
            raise StopIteration
obj=ten()

for i in obj:
    print(i)
    
