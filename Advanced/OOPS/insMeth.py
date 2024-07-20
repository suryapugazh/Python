# Methods inside the objects (instances) are Instance Method.
# every method inside the class is invoked to object.
# self ==> is so called keyword used for assigning values for each object as seperate, it must be first argument.
# instead of self keyword we can use any varible to that place but it must be in First Argument.

class Stud:
    name = 'Surya'
    age = 20

    def primt(self, gender):
        print("Name : ",Stud.name)
        print("Age : ",Stud.age)
        print("Gender : ", gender)

o = Stud()
# o.primt()      ==> but we use '.' method nowdays.
# Stud.primt(o)  ==> Actually we write code like this, this is also Class Method,

o.primt("Male")             # '.' method using Object.
# or
Stud.primt(o,"Male")       # Actual Method or Class Method.