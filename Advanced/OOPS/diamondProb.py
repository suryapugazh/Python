# Solving Diamond Problem in Python
# A
# B --> A
# C --> A
# D --> (B,C)
# Solution: Displaying a "display" function if no other function is having then print Top Base class that class A.

class A:
    def display(self):
        print("Displaying class A")

class B(A):                # Single Inherit
    #def display(self):     # Function overriding
        #print("Displaying class B")
    pass

class C(A):                # Single Inherit
    #def display(self):     # Function overriding
        #print("Displaying class C")
    pass

class D(B,C):              # if we want to print "C" class then change argument to D(C,B)
    #def display(self):
        #print("Displaying class D")
    pass
    
obj = D()
obj.display()