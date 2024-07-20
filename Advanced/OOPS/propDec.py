# Property Decorator
# Change values after craeted an Instance or 
# Update the value of the variable while Runtime.

# it is used when we want to change any changes,
# instead we ue Property Decorator "@".

class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # self.msg = self.name + " is " + str(self.age) + "years old."

        # by usign above self.msg we cannot change value after assigned
        # so we create another function to return the value

    @property
    def msg(self):
        return self.name + " is " + str(self.age) + " years old."


o = user("Surya", 20)
print(o.name)
print(o.age)
print(o.msg)
o.age = 19
print(o.name)
print(o.age)
print(o.msg)  # <== instead ==> print(o.msg()) by using @property
# here we change value of age, without Property Decorator we put brackets like msg()
# by using '@property' we use only 'msg' without brackets,
# For example, a project has many function call with brackets, for calling function without '()' we use '@property',
# because we can't changes each function call, it takes so much time.