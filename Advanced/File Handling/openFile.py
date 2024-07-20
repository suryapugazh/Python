file = open("Advanced\File Handling\hello.txt", "r")
print(file.read())

"""

try:
    file = open("Advanced\File Handling\hello.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File Not Found")
else:
    file.close()

"""