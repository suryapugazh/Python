# Accessing Data of Object(Instance)
# Store a class to a Variable and Access Data

class user:
    name = 'Surya'

obj = user()

print(user.__dict__)     # user (class) having name attribute so __dict__ function shows that.
print(obj.__dict__)      # obj (object) that contain user class but it doesn't contain actual data of class.

obj.name = "Pugazh"      # adding a value of 'name' variable which contains in 'user' class.
print(obj.__dict__)      # it shows the added data to the object.