# Arbitrary Argument can be Passing n number of arguments to Function during Function Call
# denoted by '*' before the argument in function

def stud(*names):
    #print(names)
    for i in names:
        print(i)

stud("Surya", "Gowtham", "Muthamizh", "Vignesh")