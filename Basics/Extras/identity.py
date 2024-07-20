# is       it check object of the variable 
# is not

a = [1,2]
b = [1,2]
c = a

print(id(a))
print(id(c))
print(id(b))
print(a is c)

print(a == b)    # it check values, so it's True.

print(a is not b) #it check object of the varibale

print(a!=b)       # it check values, so it's False