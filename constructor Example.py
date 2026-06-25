
class test:
    def __init__(self,name,**values):
        print("name:",name)
        print("age:",values['age'])
        print("city:",values['city'])
        print("ph:",values['ph'])
obj=test("yuvaraj",age=23,city="karur",ph=2222222222)


class triangle:
    def __init__(self,b,h):
        base=b
        height=h
        area =base * height *0.5
        print("area of traingle:",(area))
obj = triangle(7,10)
