# Class Method Decorator
# We can count no. of time constructor (__init__) called which is how manny object created, when each object created, each time __init__ called, so we can count easily no. of. time object is created.
# For Ex, A Admission Cell, if we create object for each admission, every time __init__ is called so we count the object,  

class Stu:

    count = 0     # commom for all objects

    def __init__(self, name, age):
        self.name = name
        self.age  = age
        Stu.count += 1

    def primt(self):
        print("Name: ", self.name)
        print("Age :", self.age)

    @classmethod
    def total(cls):
        return cls.count


o = Stu("Surya", 20)
o.primt()
print("Toal Students: ", o.total())     # call total() using Object

o = Stu("Pugazh", 19)
o.primt()
print("Toal Students: ", Stu.total())     # call total() using Class