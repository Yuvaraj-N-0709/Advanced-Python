class rectangle:
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
        print ("rectangle:",self.length * self.breadth)
        
class cube:
    def __init__(self, length, breadth, height):
        self.length=length
        self.breadth=breadth
        self.height=height
        print ("cube:",self.length * self.breadth *self.height)
r=rectangle(2,3)
c=cube(2,3,4)
