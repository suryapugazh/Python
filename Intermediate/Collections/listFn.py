# clear() ==> clear all values in list.

a = [1,2,3,4,5]
print(a)
a.clear()
print(a)
print("_____\n")

#copy() ==> it copy the wholle list and assing it to another variable

b = [10,20,30,40,50]
print("Value of B: ",b)
c = b.copy()
print("Value of C: ",c)
print("_____\n")

# count()  ==> count the repeated values in the lsit

d = [1,2,8,4,1,2,3,5,2,1,4,5,5]
print(d)
print("_____\n")
print("Repeatation of number 5 is : ",d.count(5))
print("_____\n")

# index() ==> find the index of particular values in the list, index(5,10) i.e. 10 is next occurrence of value '5'

e = d.copy()
print(e)
print("_____\n")
print("Index of number 5 is : ",e.index(5)) 
print("_____\n")

# len() ==> to find the Length of the list

f = e.copy()
print("Length of the List is : ",len(f))
print("_____\n")

# max() and min() ==> find the maximum and minimum values in the List

g = [25, 40, 56, 25, 45]
print("Maximum element in the List: ", max(g))
print("Minimum element in the List: ", min(g))
print("_____\n")

# pop() ==> it returns the last item in the List if NO Parameter, if we give parameter of Index it will remove the Item. Simply, remove items using Index value.

h = g.copy()
print("Actual List : ",h)
print("_____\n")
print("Return Last Item using pop() : ",h.pop())     # It returns the last item in the list
print("_____\n")
h.pop(0)     # It remove the particular item with index, and return the remaining items in the list
print("After Removing First Index using pop(0): ",h)
print("_____\n")

# remove() ==> remove items using Values.

i = h.copy()
print(i)
i.remove(56)
print(i)
print("_____\n")

# append() ==> add items to existing List

j = [15, 24, 78, 15, 63]
print(j)
j.append(25)
print(j)
print("_____\n")

name = ["Vignesh"]
print(name)
name.append("Mutha",)
print(name)
name.append("Gowtham")
name.append("Surya")
print(name)
print("_____\n")

# extend() ==> add another to to exiting List

name1 = ["ravi", "rock", "sam"]
name2 = ["kumar", "ram", "vishal"]
print(name1)
print(name2)
name1.extend(name2)
print(name1)
print("_____\n")

# insert() ==> insert a new item with custom index

name3 = name1.copy()
print("Before : ",name3)
name3.insert(2,"Surya")
print("After : ",name3)
print("_____\n")

# list() ==> is a List constructor i.e. convert any values or any existing to List

print(list(range(5)))
print("_____\n")
print(list("Python"))
print("_____\n")

# sort() ==> sort the elements in the List

num = [14, 85, 105, 42, 96]
print("Before Sort() : ", num)
num.sort()                              # Ascending order
print("After Sort() : ", num)
num.sort(reverse=True)                  # reverse=True | Descending order (Reverse)
print("Reverse Sort() : ",num)
print("_____\n")

alp = ["Mango", "Apple", "Orange", "Guva", "Grape"]
print("Before sort() : ", alp)
alp.sort()                              # Ascending order
print("After sort() : ", alp)
alp.sort(reverse=True)                  # reverse=True | Descending order (Reverse)
print("Reverse Sort() : ",alp)
print("_____\n")

alp.sort(key=len)                       # key=len | sort based on length of the item in the List
print(alp)