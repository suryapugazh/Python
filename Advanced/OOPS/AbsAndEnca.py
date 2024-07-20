# Abstraction   ==> Hiding background information from User
# Encapsulation ==> Process of wraping code and data in single unit. eg. Class
# Example : Library Management

class Library:

    def __init__(self,books):
        self.books = books
    
    def list_of_books(self):
        print("*** Available Books ***")
        for book in self.books:
            print(book)
        
    def buy_book(self, buy_book):
        if buy_book in self.books:
            print("Get your book: ", buy_book)
            #baught = [].append(buy_book)
            #print("You baught : ", baught[0])
            self.books.remove(buy_book)
        else:
            print("Book isn't available!")
    
    def return_book(self, return_book):
        self.books.append(return_book)
        print("Book returned : ",return_book)

    
books = ["Python", "Java", "C", "C++", "R"]
obj = Library(books)

msg = '''
    1. List Books.
    2. Buy Book.
    3. Return Book.
'''
while True:

    print(msg)
    choice = int(input("Enter your choice : "))

    if choice == 1:
        obj.list_of_books()
    elif choice == 2:
        buy = input("Enter book that you want to buy: ")
        obj.buy_book(buy)
    elif choice == 3:
        retorn = input("Enter book that you want to return: ")
        obj.return_book(retorn)
    else:
        print("Thank you for Purchasing!")
        quit()