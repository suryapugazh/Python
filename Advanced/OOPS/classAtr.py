# Class Attributes is Data or Variables inside the Class.
# We can Access Attributes by Two Methods.
# 1] getattr(ClassName,'Attribute', 'Optinal').
# 2] accessing by '.' Notation method.

class Stud:
    name = 'Surya'
    age = 20

# getattr() method

print(getattr(Stud, "name"))
print(getattr(Stud, "age"))
# Here, we use 3rd Argument for Exception or Default.
# like if the accessing Attribute isn't available in given Class means the 3rd Argument acts as Exception.
print(getattr(Stud, "dob", "Attribute isn't available"))
print('__________\n')

# '.' Notation

print(Stud.name)
print(Stud.age)

# setattr() ==> set or change Value of the Attribute in the Class

setattr(Stud, "age", 19)
print(Stud.age)

# Insert a New Attribute by using setattr().

setattr(Stud, 'Gender', 'Male')
print(Stud.Gender)

# Insert a New Attribute by using '.' Notation.

Stud.city = 'VTM'
print(Stud.city)

# Each Data, Attributes and Functions in a Class is stored like a Dictionary Format (__dict__)
# It's called mapingproxy Object.

print(Stud.__dict__)

# Delete Attribute using delattr()

delattr(Stud, 'city')
print(Stud.__dict__)

# Delete Arribute using 'del' keyword.

del Stud.age
print(Stud.__dict__)