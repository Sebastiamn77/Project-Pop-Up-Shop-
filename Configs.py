catalog = {
    #ice cream 
    "Lemon Meringue Pie": (4.95, "Scope"),
    "Raspberry White Chocolate Truffle": (4.95, "Scope"),
    "Campfire S'mores": (4.95, "Scope"),
    "Red Velvet Cheesecake": (4.95, "Scope"),
    "Churro & Dulce de Leche": (4.95, "Scope"),
    "Powdered Jelly Donut": (4.95, "Scope"),
    
    #shakes 
    "Lemon Meringue Shake": (9.95, "Shake"),
    "Raspberry White Chocolate Shake": (9.95, "Shake"),
    "Campfire S'mores Shake": (9.95, "Shake"),
    "Red Velvet Cheesecake Shake": (9.95, "Shake"),
    "Churro & Dulce de Leche Shake": (9.95, "Shake"),
    " Jelly Donut Shake": (9.95, "Shake"),
   
    # pastries
    "Brownie": (2.95, "Pastry"),
    "Apple Pie": (4.95, "Pastry"),
    "Chocolate Chip Cookie": (1.95, "Pastry"),
    "Cinnamon Roll": (2.95, "Pastry"),
    "Crounton": (2.95, "Pastry"),
    "Churro bites": (3.95, "Pastry"),

}
#includeing the menu descriptions for each item in the catalog
IndeptMenu = {
    "Lemon Meringue Pie": "A tangy lemon ice cream with a sweet meringue swirl.",
    "Raspberry White Chocolate Truffle": "A creamy raspberry ice cream with white chocolate truffle pieces.",
    "Campfire S'mores": "A chocolate and marshmallow ice cream with graham cracker pieces.",
    "Red Velvet Cheesecake": "A rich red velvet ice cream with cheesecake pieces.",
    "Churro & Dulce de Leche": "A cinnamon churro ice cream with dulce de leche swirls.",
    "Powdered Jelly Donut": "A sweet powdered sugar ice cream with jelly-filled donut pieces.",
    "Lemon Meringue Shake": "A tangy lemon milkshake with a sweet meringue swirl.",
    "Raspberry White Chocolate Shake": "A creamy raspberry milkshake with white chocolate truffle pieces.",
    "Campfire S'mores Shake": "A chocolate and marshmallow milkshake with graham cracker pieces.",
    "Red Velvet Cheesecake Shake": "A rich red velvet milkshake with cheesecake pieces.",
    "Churro & Dulce de Leche Shake": "A cinnamon churro milkshake with dulce de leche swirls.",
    "Jelly Donut Shake": "A sweet powdered sugar milkshake with jelly-filled donut pieces.",
    "Brownie": "A rich chocolate brownie with a fudgy center.",
    "Apple Pie": "A classic apple pie with a flaky crust and sweet apple filling.",
    "Chocolate Chip Cookie": "A soft and chewy chocolate chip cookie with a golden brown exterior.",
    "Cinnamon Roll": "A sweet cinnamon roll with a soft and fluffy interior, topped with a sweet glaze.",
    "Crounton": "A crunchy and buttery pastry with a sweet glaze.",
    "Churro bites": "A bite-sized version of the classic churro, coated in cinnamon sugar and served with a sweet dipping sauce.",  

}
cart = []
global firstimeordering
firstimeordering = True
def ordering():
    global firstimeordering
    if firstimeordering == True:
        print("Welcome to the Green Team Ice Cream Shop!")
        firstimeordering = False
        see_menu = input("Would you like to see our menu? (yes/no): ")
        if see_menu.lower() == "yes":
            menutype=input("Type Shakes, Ice Cream, or Pastries: ")
            if menutype.lower() == "shakes":
                print("Here are our shakes:")
                for item, (price, category) in catalog.items():
                    if category == "Shake":
                        print(f"{item} - ${price:.2f} ({category})")
            elif menutype.lower() == "ice cream":
                print("Here are our ice creams:")
                for item, (price, category) in catalog.items():
                    if category == "Scope":
                        print(f"{item} - ${price:.2f} ({category})")
            elif menutype.lower() == "pastries":
                print("Here are our pastries:")
                for item, (price, category) in catalog.items():
                    if category == "Pastry":
                        print(f"{item} - ${price:.2f} ({category})")
            else:
                print("Invalid menu type. Please choose from Shakes, Ice Cream, or Pastries.")
   
    imdonenameingthings= input("Type 1 to add an item to your cart, type 2 to view your cart, type 3 to checkout, type 4 to see the menu again, or type 5 to see the menu descriptions: ")
    if imdonenameingthings == "1":
        item_to_add = input("Enter the name of the item you want to add: ")
        numberof_items = input("How many of this item would you like to add? ")
        if item_to_add in catalog:
            for _ in range(int(numberof_items)):
                cart.append(item_to_add)
            print(f"{numberof_items} {item_to_add}(s) have been added to your cart.")
            ordering()
            
        else:
            print("Sorry, that item is not on the menu.")
            ordering()

    elif imdonenameingthings == "2":
        if cart:
            print("Your cart contains:")
            for item in cart:
                price, category = catalog[item]
                print(f"{item} - ${price:.2f} ({category})")
                ordering()
        else:
            print("Your cart is empty.")
            ordering()
    elif imdonenameingthings == "3":
        if cart:
            reciptmaker()
        else:
            print("Your cart is empty.")
            ordering()
    elif imdonenameingthings == "4":
        menutype=input("Type Shakes, Ice Cream, or Pastries: ")
        if menutype.lower() == "shakes":
            print("Here are our shakes:")
            for item, (price, category) in catalog.items():
                if category == "Shake":
                    print(f"{item} - ${price:.2f} ({category})")
                    ordering()
        elif menutype.lower() == "ice cream":
            print("Here are our ice creams:")
            for item, (price, category) in catalog.items():
                if category == "Scope":
                    print(f"{item} - ${price:.2f} ({category})")
                    ordering()
        elif menutype.lower() == "pastries":
            print("Here are our pastries:")
            for item, (price, category) in catalog.items():
                if category == "Pastry":
                    print(f"{item} - ${price:.2f} ({category})")
                    ordering()
        else:
            print("Invalid menu type. Please choose from Shakes, Ice Cream, or Pastries.")
    elif imdonenameingthings == "5":
        item_description = input("What item do you want to see the description for? ")
        if item_description in IndeptMenu:
            print(f"{item_description}: {IndeptMenu[item_description]}")
            ordering()
        else:
            print("Item not found. Please check the spelling and try again.")
            ordering()


def reciptmaker():
    if cart:
        print("Your receipt:")
        total = 0
        for item in cart:
            price, category = catalog[item]
            total += price
            print(f"{item} - ${price:.2f} ({category})")
        print("Total: ${:.2f}".format(total))
    else:
        print("Your cart is empty.")

ordering() 
