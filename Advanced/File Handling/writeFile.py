# write() | 'w' ==> Overwrite

file = open("Advanced\File Handling\\bye.txt", "w")
file.write("Bang Bang Bang")         # It'll overwrite all the lines.
file.close()                         # close() method save the changes that we made on the file.

file = open("Advanced\File Handling\\bye.txt", "r")

for line in file:
    print(line)