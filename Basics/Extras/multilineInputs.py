list = []
while True:
    inputs = input("Enter some words: ")
    if inputs:
        list.append(inputs)
    else:
        break


print(list)

output = '\n'.join(list)
print(output)