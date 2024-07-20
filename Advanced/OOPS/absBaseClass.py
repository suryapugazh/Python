# Abstract Base Class | Abstract Method.
# In Abstract class, we should create only Function, shouldn't Define any data's or any other Functionalities.
# We should Define only Function Name, Should not put any Definition inside the Function.
# After that we should convert Functions or Method into an abstarct method by putting "@abstractmethod" above each method.
# After created Derived class by Inhereting Abstract Base Class we Should "Re-Define" "All" each functions that having in Abstract Base Class(ABS) to Derived class.
# Simply : Template for Class or Class as a Template i.e. Abstract Class (Base)

from abc import ABC, abstractmethod

class Bank(ABC):     # by inheriting Abstract Base Class(ABS) as an argument, it converted into Abstract class.
    
    @abstractmethod
    def loan(self):
        pass         # we shouldn't put any Definition

    @abstractmethod
    def credit(self):
        pass         # we shouldn't put any Definition

    @abstractmethod
    def debit(self):
        pass         # we shouldn't put any Definition

class IndianBank(Bank):
    
    def loan(self):          # method from Abstract Class (Compulsory)
        print("Loan amount 5% you should pay")

    def credit(self):        # method from Abstract Class (Compulsory)
        print("We provide Credit")

    def debit(self):         # method from Abstract Class (Compulsory)
        print("Also we provide Debit")

    def card(self):          # we can add additional method in Derived class (Additional)
        print("We provide Credit Card also")

obj = IndianBank()
obj.loan()
obj.credit()
obj.debit()
obj.card()