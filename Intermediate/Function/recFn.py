def facto(x):
    if x == 1:
        return 1
    else:
        return x * facto( x - 1)
print("Factorial : ", facto(5))