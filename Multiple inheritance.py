#multiple inheritance

class person:
    def person(self,name,age,gender):
        print("name:",name,"-----","age:",age,"-----","gender:",gender)

class company():
    def company_details(self,name,location):
        print("professional details:")
        print("cmpany name:",name,"-----","location:",location)

class other():
    def other_details(self,salary,designation):
        print("other details")
        print("salary:",salary,"-----","designation:",designation)

class all_details(person,company,other):
    print("printing the employee details:",end="\n\n")

obj=all_details()
obj.person("yuva",23,"male")
obj.company_details("google","ind")
obj.other_details("24LPA","python")
