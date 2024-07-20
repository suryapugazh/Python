# Static Method is a Decorator '@staticmethod' to set Function as common for all
# By using static method we don't want to put 'self' keyword as parameter, usually it's compulsory because 'self' only can create object.

class Stud:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def primt(self):
        print("Name : ", self.name, "Age : ", self.age)

    @staticmethod                          # by putting '@staticmethod' we can use this function as common with without 'self'. i.e def welcome():
    def welcome():                         # default we should put 'self' as argument for creating Instances.  i.e. def welcome(self):
        print("Welcome to Schollege")

s1 = Stud("Surya", 20)
s1.primt()
s1.welcome()
print("\n__________\n")
s2 = Stud("Pugazh", 19)
s2.primt()
s2.welcome()