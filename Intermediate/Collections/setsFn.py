# union() ==> combine one set | it require another varibale to store union

a = {1,2,3,4,5}
b = {'a','b','c','d','e'}
c = a.union(b)
print(c)
print("_____\n")

# update() ==> it combine one set to another like extend

a.update(b)
print(a)
print("_____\n")

# intersection() ==> it returns common value by comparing two Sets

a = {1,2,3,4,5}
b = {5,6,7,8}

c = a.intersection(b)
print(c)
print("_____\n")

# intersection_update() ==> it also same as intersection(), it won't requires and aditional varibale, it replaces the result itslef

a = {1,2,3,4,5}
b = {5,6,7,8}

a.intersection_update(b)
print(a)
print("_____\n")

# symmetric_difference() ==> it returns only unique values, it avoids common value by comparing two Sets

a = {1,2,3,4,5}
b = {5,6,7,8,1}

c = a.symmetric_difference(b)
print(c)
print("_____\n")

# symmetric_diffrence_update() ==> it also same as symmetric_difference(), it won't requires and aditional varibale, it replaces the result itslef

a = {1,2,3,4,5}
b = {5,6,7,8,1}

a.symmetric_difference_update(b)
print(a)
print("_____\n")

# isdisjoint() ==> it checks Sets values for joint i.e. if same values having in the Sets it means it can Joint so it return True else return False

a = {1,2,3,4,5}
b = {5,6,7,8,1}

c = a.isdisjoint(b)     # here a and b sets having 5 and 1 so it return Flase, it means it can able to joint
print(c)
print("_____\n")

# issubset()  ==> it returns True if same value exists on both sets. It check 'a' to 'b' set.

a = {3,4,5}
b = {1,2,3,4,5}

c = a.issubset(b)     # here 'a' having same elements that exists in 'b' so it returns True.
print(c)
print("_____\n")

# issuperset() ==> it returns True if same value exists on both sets. It check 'b' to 'a' set.

a = {1,2,3,4,5}
b = {3,4,5}

c = a.issuperset(b)     # here it check whether 'b' is derived from 'a' or not, if it's yes then return True.
print(c)