#kwargs

def person(name,age,city,ph):
    print("name:",name)
    print("age:",age)
    print("city:",city)
    print("ph:",ph)
person("yuvaraj",23,"karur",2222222222)


def person(name,*values):
    print("name:",name)
    print(values)
person("yuvaraj",23,"karur",2222222222)


def person(name,**values):
    print("name:",name)
    print(values)
person("yuvaraj",age=23,city="karur",ph=2222222222)


def person(name,**values):
    print("name:",name)
    for i ,j in values.items():
        print(i,j)
person("yuvaraj",age=23,city="karur",ph=2222222222)


def person(name,**values):
    print("name:",name)
    print(values.items())
    for i ,j in values.items():
        print(i,j)
person("yuvaraj",age=23,city="karur",ph=2222222222)



def person(name,**values):
    print("name:",name)
    print("age:",values['age'])
    print("city:",values['city'])
    print("ph:",values['ph'])
person("yuvaraj",age=23,city="karur",ph=2222222222)


