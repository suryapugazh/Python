for i in range(6):
    for j in range(i):
        print("*", end="")
    print("")

print("_____\n")

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

print("_____\n")

# A - Z ==> 65 - 90
# a - z ==> 97 - 122

for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end="")
    print('')

print("_____\n")

for i in range(97,102,1):
    for j in range(97,102,1):
        print(chr(j),end="")
    print('')