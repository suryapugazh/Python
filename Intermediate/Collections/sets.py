# Sets is unodered, unidexed, unchangable and no duplicates

names = {"Surya", "Vignesh", "Muthamizh", "Gowtham"}
print(names)
print(type(names))
print("_____\n")

# Accessing elements in Sets

for name in names:
    print(name)
print("_____\n")

# add() ==> to add new elements to existing Set

names.add("Shagul")
print(names)
print("_____\n")

# update() ==> combining multiple sets into single

names1 = {"Saran", "Rajasekar", "Mohan"}
names.update(names1)
print(names)
print("_____\n")

# remove() ==> to remove any elements inside the Set. It shows us the Exception message when removing Data is not found in the Set

names.remove("Saran")
print(names)
print("_____\n")

# dicard() ==> it also remove element inside the Set, but if the removing item is not found, it won't shows us the Excpetion message

names.discard("Mohan")
print(names)
print("_____\n")

# pop() ==> it removes the last item in the Sets. Set is unordered so we can't recognize which element gonna pop.

names.pop()
print(names)
print("_____\n")

# clear() ==> it remove all entities in the set and it becomes an empty Set

names.clear()
print(names)
print("_____\n")

# del() ==> delete the entire set include variable

del(names)
# Set automatically remove duplicate elements

names = {"Surya", "Vignesh", "Muthamizh", "Gowtham", "Gowtham", "Vignesh", "ViGnEsH"}
print(names)