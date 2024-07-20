# Class ==> is a Template consists of Data and Variables.
# Object ==> is a Instance of Template i.e. Copy of Class.

class new():
    pass

print(type(new))

old = new()

# isinstance(ObjectName, ClassName) ==> it check whether given Object is created by given Class.
# If the object creared by Given class then it'll return True.

print(isinstance(old,new))

a = 10      # Here, a is the Object of Integer Class.
print(isinstance(a,int))     # It check whether that's True or Not.

print(type(old))