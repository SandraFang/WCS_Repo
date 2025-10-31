class Book:

    def __init__ (self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def checkout(self):
        if self.available:
            self.available = False
    
    def return_book(self):
        if self.available == False:
            self.available = True

    def show_info(self):
        if self.available: status = "available"
        else: status = "checked out"     
        print(f"Title: {self.title} ; Author: {self.author} ; Status: {status}")

books = []

while True:
    print ("Library Catalogue System")
    selection = input("Please select: add, view, check out, return, exit:")

    #add
    if selection == "add":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        books.append(Book(title,author))

    #view
    elif selection == "view":
        if not books:
            print("no records yet")
        else:
            for b in books:
                b.show_info()

    #checkout
    elif selection =="check out":
        book_checkout = input("Please enter title of book to checkout: ")
        book_found = False

        for b in books:
            if b.title == book_checkout:
                book_found = True
                if b.available == True:
                    b.available = False
                    print(f"{b.title} Checked out successfully")
                else:
                    print(f"{b.title} is already checked out")
                break
        if not book_found:
            print("Book not found")

    #return
    elif selection == "return":
        book_return = input("Please enter title of book to return: ")
        book_found = False

        for b in books:
            if b.title == book_return:
                book_found = True
                if b.available == False:
                    b.available = True
                    print(f"{b.title} returned successfully")
                else:
                    print(f"{b.title} is already returned")
                break
        if not book_found:
            print("Book not found")
    #exit
    elif selection == "exit":
        print ("Goodbye")
        break
    else:
        print("invalid selection, please try again!")