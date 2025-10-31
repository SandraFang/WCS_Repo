class Product:

    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def show_info(self):
        print(f"Product: {self.name} ; Price: {self.price} ; Quantity: {self.quantity}")

products = []

while True:
    print ("Inventory System")
    selection = input("Please select: add, view, update, value, exit:")

    #add
    if selection == "add":
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        quantity = input("Enter product quantity: ")
        products.append(Product(name,price,quantity))

    #view
    elif selection == "view":
        if not products:
            print("no records yet.")
        else:
            for p in products:
                p.show_info()

    #update
    elif selection =="update":
        product_update = input("Please enter the name of product to be updated: ")
        found = False

        for p in products:
            if p.name == product_update:
                found = True
                new_price = input("Enter new price: ")
                new_quantity = input("Enter new quantity: ")
                p.price = new_price
                p.quantity = new_quantity
                print("Update success.")
                break
        if not found:
            print("Product not found")

    #value
    elif selection == "value":
        value = 0
        for p in products:
            value += float(p.quantity) * float(p.price)
        print(f"The total value of the inventory is {value}")

    #exit
    elif selection == "exit":
        print ("Goodbye")
        break
    else:
        print("invalid selection, please try again!")