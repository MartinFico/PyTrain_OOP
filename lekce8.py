class Student:
    # age=20
    # name="Pavel"
    spec = "devOps"
    def __init__(self,name,age):
        self.name=name
        self.age =age

    def showMsg(self,):
         print(f"moje jmeno je {self.name} a muj vek je {self.age}")

    def sayHi(self,Pozdrav):
        print(f"{Pozdrav} , ja jsem {self.name}")

    def checkAlcohol(self):
        if self.age <18:
            return False
        else:
            return True

student=Student ("Petr", 50)
student.sayHi("ahoj")
student.sayHi("Dobrý den")
print(student.checkAlcohol())



# student.showMsg()



# student1=Student("Pavel",400)
#
# print(student1.name)
#
# student2=Student("Adam",600)
#
# print(student2.age)
# print(student2.spec)
# student2.name = "Petr"
# print(student2.name)
