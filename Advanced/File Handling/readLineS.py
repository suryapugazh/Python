# readline()
# readlines()

file = open("Advanced\File Handling\hello.txt", "r")
print(file.readline(7))     # slice first line with/without index start from 1 - n as argument.
print(file.readline())      # next line of the document
print(file.readlines())     # print all the remaining lines inside the document as a List format.