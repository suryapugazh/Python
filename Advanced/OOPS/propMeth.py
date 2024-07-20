# Property method or property function also same as Property Getter and Setter
# We just assign Getter and Setter to property function like
# total = property(Getter, Setter) ==> here we assign it to 'total',
# because we need to Set or Get value to that 'Total' variable.

class Stud:
    def __init__(self, total):
        self._total = total   # this variable is to be assigned to 'total = property(Getter, Settter)' at the bottom of the class.
        
    @property     # here also we can use @property for no-paranthesis '()'.
    def avg(self):
        return self._total / 5.0
    
    #@property          # we just create getter as a function, by can't use @property for no-paranthesis '()',
    def getter(self):   # because the getter function has the ability to use no-paranthesis '()'. But we don't need this for 'total' because toal is varibale we can call by '.' method,
        return self._total # but we need @property for 'avg' because it is function, i.e. function only call with paranthesis(), by using @property we don't need paranthesis, which is no-paranthesis '()'.
    
    # @total.setter ==> setter function, instead we create Setter as a function
    def setter(self,tot):
        # for exmp. data validation can also do in setter 
        if tot<0 or tot>500:
            print("Invalid total and Total can't change, so previous value to be assigned!!!")
        else:
            self._total = tot

    total = property(getter, setter)

obj = Stud(450)
print("Total : ", obj.total)
print("Average : ", obj.avg)
obj.total = 250  # we can't set value directly, so we use seperate function for setting a value to __ or _ variable.
print("Total : ", obj.total)
print("Average : ", obj.avg)
obj.total = 501 # here 501>500 so it'll return previous values
print("Total : ", obj.total)
print("Average : ", obj.avg)
