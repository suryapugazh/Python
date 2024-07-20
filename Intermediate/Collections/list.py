a = [1,2,3,4,5]
print(a)
print(type(a))
a[0] = 20
print(a)
#List slicing [start:stop:step]
print(a[-1])
print(a[0:2])
print(a[1:])
print(a[:3])
print(a[0:4:2])

print('_____\n')
# Different type of values
b = [1,0.5, True, "Python"]
print(b)
print(type(b))
print(b[0], 'type is', type(b[0]))
print(b[1], 'type is', type(b[1]))
print(b[2], 'type is', type(b[2]))
print(b[3], 'type is', type(b[3]))

# Nested List
c = [10,20,30,['Gowth','Muth','Vig']]

print(type(c[3]))
print(c[3][1])