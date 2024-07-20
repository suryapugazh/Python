# append() | 'a' ==> add to next line

file = open("Advanced\File Handling\\bye.txt", "a")
file.write("Song from Anjan")
file.write("\nActor Surya")
file.close()

file = open("Advanced\File Handling\\bye.txt", "r")
print(file.read())