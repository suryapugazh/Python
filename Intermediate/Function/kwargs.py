# Keyword Argument can be passing values by using Keyword during Function Call

def msg(name, age):
    print(name, "age is ", age)

msg("Ram", 18)
msg(18,"Ram")  # python takes it as we given.
msg(age=18, name="Ram") # instead we can pass keyword to assign the values.