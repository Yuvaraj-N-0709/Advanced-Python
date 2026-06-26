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
    def show(self):
        print("printing the employee details:",end="\n\n")
        super().person("yuvaraj",23,"male")
        super().company_details("google","ind")
        super().other_details("24lpa","data scientist")
        
obj=all_details()
obj.show()
