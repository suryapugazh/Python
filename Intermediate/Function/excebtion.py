# Try Exceptblock

'''
try:
    a = 10/0
except Exception as e:
    print(e)
'''

# Try Except Else block

'''
try:
    a = 10/20
except Exception as e:
    print(e)
else:
    print("Result : ", a)
'''

# Finally

'''
try:
    a = 10/20
except Exception as e:
    print(e)
else:
    print("Result : ", a)
finally:
    print("I don't care")
'''

# Types of Exceptions in Python

'''
print(dir(locals()['__builtins__']))
print("No. of Exceptions : ",len(dir(locals()['__builtins__'])))

'''
# Example of Five Exceptions

''' 
# NameError Exception

try:
    print(a)
except NameError:
    print("A is not defined")

# ZeroDivisionError Exception

try:
    print(10/0)
except ZeroDivisionError:
    print("Denominator can't be Zero")

# ValueError Exception

try:
    a = int("String")
except ValueError:
    print("Please Enter numbers only")

# IndexError Exception

try:
    list = [10,20,30,40,50]
    print(list[10])
except IndexError:
    print("Invalid Index")

# FileNotFoundError Exception

try:
    a = open("test.txt")
except FileNotFoundError:
    print("File not found")
else:
    print(a.read())

'''

# Handling Multiple Exception

try:
    a = 10/2
    print(a)
    b = [10,20,30,40,50]
    print(b[10])
except ZeroDivisionError:
    print("Denominator can't be Zero")
except IndexError:
    print("Invalid Index")