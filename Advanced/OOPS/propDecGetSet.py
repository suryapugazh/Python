'''
Access modifier in Python
# public data member
     var1 = 1
# protected data member
     _var2 = 2
# private data member
     __var3 = 3
'''
# To access values when varibales are in private(__) or protected(_),
# we use setter and getter methods to access __ or _ variables.

class Stud:
    def __init__(self, total):
        self._total = total          # here we use _total as protcted variable so we cann't access this variable,
        #self.avg = self.total/5.0     so we use seperate function for getting or setting private variables.
        
    @property     # here also we can use @property for no-paranthesis '()'.
    def avg(self):
        return self._total / 5.0
    
    @property     # getter function
    def total(self):
        return self._total
    
    @total.setter #setter function
    def total(self,tot):
        # for exmp. data validation can also do in setter 
        if tot<0 or tot>500:
            print("Invalid total and Total can't change, so previous value to be assigned!!!")
        else:
            self._total = tot
    
obj = Stud(450)
print("Total : ", obj.total)
print("Average : ", obj.avg)
obj.total = 250  # we can't set value directly, so we use seperate function for setting a value to __ or _ variable.
print("Total : ", obj.total)
print("Average : ", obj.avg)
obj.total = 501 # here 501>500 so it'll return previous values
print("Total : ", obj.total)
print("Average : ", obj.avg)