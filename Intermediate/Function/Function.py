def welcome():
    print("Hello")

welcome()

# Without Return, Without Argument

'''
def add():
    a = int(input("Enter a value of A: "))
    b = int(input("Enter a value of B: "))
    c = a + b
    print("Total : ", c)

add()
'''

# Without Return, With Argument

'''
def sub(a,b):
    c = a-b
    print("Result : ", c)

sub(50,25)
'''

# With Return Without Argument

'''
def mul():
    a = int(input("Enter a value of A: "))
    b = int(input("Enter a value of B: "))
    c = a * b
    return c     # the value of c is to be stored in mul() function.

n = mul()
print('Result : ', n)
'''

# With Return With Argument 

'''
def div(a,b):
    c = a / b
    return c

m = div(50,25)
print(m)
'''