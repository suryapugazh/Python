a = (1, 3.5, True, "Surya")
print(a)
print(type(a))
print(a[2])
print(a[-1])
print(a[0:3])
print("_____\n")

# Tuple is immutable so if we need to add items to tuple, we first need to change the tuple into List using 'list() constructor' then add and the again convert it into tuple using 'tuple() constructor'

b = list(a)           # list() constructor
print(b)
print(type(b))
b.append("Python")
print(b)
a = tuple(b)          # tuple() constructor
print(a)
print(type(a))
print("_____\n")

# iterate the tuple

for i in a:
    print(i)
print("_____\n")

# check the item available in Tuple

if "Surya" in a:
    print("Found!")
else:
    print("Not Found!")
print("_____\n")

# len() ==> to find the no. of. elements in the Tuple

print(len(a))
print("_____\n")

c = (1)
print(type(c))     # if c has sigle value then type of C is to be considered as DataType of value inside the paranthesis()
print("_____\n")
c = (1,)
print(type(c))     # it shows tuple as type when put comma',' inside the tuple after each value
print("_____\n")

# Tuple is immutable so we can't remove any items, but we can delete a variable which is created using tuple

del a

# Concatenate two tuples

a = (8, 2, 8, 4, 5)
b = ("Sam", "Kumar", 6, 7, 8)
print(a)
print(b)
c = a + b
print(c)
print("_____\n")

# count() ==> count the repeated items in the Tuple

print(c.count(8))
print("_____\n")

# Nested Tuples

c = (a,b)
print(c)
print("_____\n")

# Accessing elements in Nested Tuples

print(c[0])
print(c[1])
print(c[0][3])
print(c[1][0])
print("_____\n")

# Repetiton in Tuple

d = ("Surya") * 5     # Without putting ','
print(d)
d = ("Surya",) * 5    # With ','
print(d)
print("_____\n")

# min() and max() ==> to find the maximum and minimum elements in the Tuple

e = (1, 8, 7, 56, 25)
print("Minimum Item : ",min(e))
print("Maximum Item : ",max(e))