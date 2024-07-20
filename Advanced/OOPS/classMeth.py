# We can create a function called method inside the class.
# functions that inside the class is called methods.

class meth:
    name = "Surya"
    age = 20

    def primt():
        print("Name : ", meth.name)
        print("Age : ", meth.age)

meth.primt()
print(meth.__dict__)                # class dictionary
print(getattr(meth, 'primt', ))     # function dictionary with Hexa Decimal Number
getattr(meth, 'primt')()            # for print the values
print(meth.__dict__['primt'])       # it same as function dictionary but with __dict__ method
meth.__dict__['primt']()            # for print values