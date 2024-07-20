# Default Parameter passes Default values when User didn't pass any values, it passes by default.

def user(name, city="TVM"):     # here city is a Defalut Parameter it return when user didn't pass values to city argument.
    print(name, 'is from ', city)

user("Surya", "VTM")
user("Surya")


# Passing list as Argument

def tot(mark):
    return sum(mark)    # here sum() is a built-in function to total values.

i = tot([10,20,25,36,47])
print('Total : ',i)