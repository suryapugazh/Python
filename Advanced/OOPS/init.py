# __int__ method also called constructor.
# but in python we should say __init__ method.
# __int__ function always first execute when Obejct Called.
# after that remaining methods are execute.

class samp:
    def __init__(self, name):
        print("This always executes first")
        self.name = name

    def primt(self):
        print("Name : ", self.name)

obj1 = samp("Surya")
obj1.primt()
print(obj1.__dict__) # object is created after called while there is empty dictionary.

print("\n----------\n")

obj2 = samp("Pugazh")
obj2.primt()
print(obj2.__dict__) # object is created after called while there is empty dictionary.

print(samp.__dict__) # but here class dictionary has no method about NAME attribute, because there is 'self' keyword to create object (instance) attribute.