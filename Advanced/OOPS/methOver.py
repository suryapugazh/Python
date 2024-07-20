# Function or Method Overriding.
# re-writing existing function in derived class.
# Change values to the function that already created on Base class in Derived class.

class Employee:
    def workHrs(self):     # Function in Base class.
        self.workHrs = 50
    
    def printHrs(self):
        print("Working hour of Employee : ", self.workHrs)
    
class Trainee(Employee):
    def workHrs(self):     # "Overriding" Function that Exist on Base class (Employee).
        self.workHrs = 70
    
    def upgradeTrainee(self):     # This function is for Hour decrement after Trainee enter into Company as an Employee.
        super().workHrs()
    
employee = Employee()

employee.workHrs()          # Base class that have "self.workHrs" function
employee.printHrs()

trainee = Trainee()
trainee.workHrs()            # Overriding "self.workHrs" for trainee work hours from derived class
trainee.printHrs()
trainee.upgradeTrainee()     # This call for Trainee upgradation as Employee
trainee.printHrs()
