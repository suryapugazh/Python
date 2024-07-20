i = 1            # Print 1 - 10 numbers
while i<=10:
    print(i)
    print("-----")
    i += 1
    print("|||||")

print("_____")

i = 1            # Odd numbers
while i<20:
    print(i)
    i += 2

print("_____")

i = 2            # Even numbers
while i<=20:
    print(i)
    i += 2

print("_____")

i = 1            # Continue Statement
while i<=20:
    if i%2 == 0:
        i += 1
        continue
    print(i)
    i += 1

print("_____")

i = 1            # Break Statement
while i<=10:
    if i==7:
        break
    print(i)
    i += 1

print("_____")

print(list(range(5)))            # Range() function

print("_____")

print(list(range(2,7)))

print("_____")

print(list(range(0,20,2)))

print("_____")

print(list(range(1,20,2)))
