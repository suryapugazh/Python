# Multiple Inheritance     |     A --> B, B --> C.
# Accessing class that already derived from another one class.

class GrandFather:
    def ownHouse(self):
        print("Grandfather's House")
    
class Father(GrandFather):
    def ownPlot(self):
        print("Father's Plot")
    
class Son(Father):
    def ownBike(self):
        print("Son's Bike")
    
obj = Son()

obj.ownBike()     # This call from Son class.
obj.ownPlot()     # This call from Father class that derived from GrandFather class.
obj.ownHouse()    # This call from Base class which is GrandFather class.