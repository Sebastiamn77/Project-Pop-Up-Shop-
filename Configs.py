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
    "Jelly Donut Shake": (9.95, "Shake"),
   
    # pastries
    "Brownie": (2.95, "Pastry"),
    "Apple Pie": (4.95, "Pastry"),
    "Chocolate Chip Cookie": (1.95, "Pastry"),
    "Cinnamon Roll": (2.95, "Pastry"),
    "Crounton": (2.95, "Pastry"),
    "Churro bites": (3.95, "Pastry"),

}
#including the menu descriptions for each item in the catalog
IndeptMenu = {
    "Lemon Meringue Pie": "A tangy lemon ice cream folded with fluffy marshmallow and vanilla wafer bits.",
    "Raspberry White Chocolate Truffle": "A creamy raspberry ice cream with white chocolate truffle pieces.",
    "Campfire S'mores": "A toasted marshmallow ice cream with graham cracker pieces and chocolate chunks.",
    "Red Velvet Cheesecake": "A rich red velvet ice cream with cheesecake chunks and a fudge ripple.",
    "Churro & Dulce de Leche": "A cinnamon sugar ice cream base packed with crispy churro bits and thick dulce de leche swirls.",
    "Powdered Jelly Donut": "A creamy vanilla bean ice cream rippled with a thick raspberry-strawberry jam and chunks of soft, sugar-dusted brioche dough.",
    "Lemon Meringue Shake": "A tangy lemon milkshake with fluffy marshmallow and vanilla wafer bits.",
    "Raspberry White Chocolate Shake": "A creamy raspberry milkshake with white chocolate truffle pieces.",
    "Campfire S'mores Shake": "A toasted marshmallow milkshake with graham cracker pieces and chocolate chunks.",
    "Red Velvet Cheesecake Shake": "A rich red velvet milkshake with cheesecake chunks and a fudge ripple.",
    "Churro & Dulce de Leche Shake": "A cinnamon sugar milkshake with crispy churro bits and thick dulce de leche swirls.",
    "Jelly Donut Shake": "A sweet powdered sugar milkshake rippled with a thick raspberry-strawberry jam and chunks of soft, sugar-dusted brioche dough.",
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
   
    imdonenameingthings = input("Type 1 to add an item to your cart, type 2 to view your cart, type 3 to checkout, type 4 to see the menu again, or type 5 to see the menu descriptions: ")
    if imdonenameingthings == "1":
        item_to_add = input("Enter the name of the item you want to add: ")
        numberof_items = input("How many of this item would you like to add? ")
        if item_to_add in catalog:
            for _ in range(int(numberof_items)):
                cart.append((item_to_add, int(numberof_items)))
            print(f"{numberof_items} {item_to_add}(s) have been added to your cart.")
            ordering()
            
        else:
            print("Sorry, that item is not on the menu.")
            ordering()

    elif imdonenameingthings == "2":
        if cart:
            print("Your cart contains:")
            for item, quantity in cart:
                price, category = catalog[item]
                print(f"{item} - ${price:.2f} ({category}) x {quantity}")
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
        total = 0
        subtotal = 0
        item_total = 0
        discount = 0.0
        tax_rate = 0.07
        
        promo = input("Promo code (Enter to skip): ").strip().lower()
        if promo.startswith("save"):
            percent = promo[4:]
            if percent.isdigit():
                discount = int(percent) / 100
            else:
                print("Invalid promo code. No discount will be applied.")
        print("=" * 36)
        print("RECEIPT".center(36))
        print("Customer something somethign")
        print("-" * 36)
        
        for item, quantity in cart:
            price, category = catalog[item]
            item_total += price * quantity
            subtotal += item_total
            print(f"{quantity} x {item} - ${price:.2f} ({category})")
        print("Total: ${:.2f}".format(subtotal))
        if discount > 0:
            discount_amount = subtotal * discount
            total = subtotal - discount_amount
            print("Discount: -${:.2f}".format(discount_amount))
        else:
            total = subtotal
        tax = total * tax_rate
        total_with_tax = total + tax
        print("Tax (7%): ${:.2f}".format(tax))
        print("=" * 36)
        print("Total with tax: ${:.2f}".format(total_with_tax))
        print("=" * 36)
    else:
        print("Your cart is empty.")

ordering() 
