# Single Inheritance     |     A --> B
# Process of derive a class from base class and it's functionalites.
# Single means one class derived from another one class not many.

class HP:                  # Base Class
    company = "HP"
    website = "www.hp.com"

    def contact(self):
        print("Ooraagaali Meatu Street, Vettavalam")
    
class HP_Pavilion(HP):     # Derived Class

    def __init__(self):
        self.name = "HP Pavilion 15"
        self.year = 2022

    def product(self):
        print("Name : ", self.name)
        print("Year : ", self.year)
        print("Company : ", self.company)     # Access from base calss
        print("Website : ", self.website)     # Access from base calss

hp1 = HP_Pavilion()
hp1.product()
print("\n__________\n")
hp1.contact()