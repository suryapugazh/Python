# Multiple Inheritance     |     A --> (B,C)
# Accessing Multiple parent classess to one base class

class Mother:
    def cooking(self):
        print("Mom making Food")
    def chess(self):
        print("Learnig chess from Mother")
    
class Father:
    def ride(self):
        print("Dad riding a bike")
    def chess(self):
        print("Learning chess from Dad")

class Son(Mother, Father):
    def cool(self):
        print("Cool")
    
obj = Son()     
obj.cool()      # This call from Son
obj.cooking()   # This call from Mother class
obj.ride()      # This call from Father class
obj.chess()     # This call executes from First argument of the Son class, Here we pass "Mother" as First argument.