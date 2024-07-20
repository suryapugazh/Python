import os

if os.path.exists("test.txt"):
    os.remove("test.txt")     # remove() for removing a file or document.
    #os.rmdir("New")      # rmdir() removes the Folder.
else:
    print("File not found!")