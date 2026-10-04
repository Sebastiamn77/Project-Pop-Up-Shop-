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


def ordering():
    customer_name = input("Welcome! What's your name? ").strip().title()
    print(f"Welcome to the Green Team Ice Cream Shop, {customer_name}!")
    while True:
        print("Type the number of the option you want to choose:")
        print("1) View Menu")
        print("2) Add Item")
        print("3) Remove Item")
        print("4) View Cart")
        print("5) Checkout")
        choice = input("Choose an option: ").strip()
        #  Menu
        if choice == "1":
            print("What type of food would you like to see?")
            print("1) Shakes")
            print("2) Ice Cream")
            print("3) Pastries")
            menutype = input("Choose a menu type: ").strip().lower()
            if menutype == "shakes":
                print("Here are our shakes:")
                print("-" * 55)
                for item, (price, category) in catalog.items():
                    if category == "Shake":
                        print(f"{item:<35} {category:<10} ${price:>5.2f}")
            elif menutype == "ice cream":
                print("Here are our ice creams:")
                print("-" * 55)
                for item, (price, category) in catalog.items():
                    if category == "Scoop":
                        print(f"{item:<35} {category:<10} ${price:>5.2f}")
            elif menutype == "pastries":
                print("Here are our pastries:")
                print("-" * 55)
                for item, (price, category) in catalog.items():
                    if category == "Pastry":
                        print(f"{item:<35} {category:<10} ${price:>5.2f}")
            else:
                print("Invalid menu type. Please choose Shakes, Ice Cream, or Pastries.")

        # Add Item
        elif choice == "2":
            item_to_add = input(
                "Enter the name of the item you want to add: "
            ).strip().lower()
            if item_to_add in catalog:
                numberof_items = input(
                    "How many of this item would you like to add? "
                ).strip()
                if not numberof_items.isdigit() or int(numberof_items) == 0:
                    print("Quantity must be a whole number greater than 0.")
                else:
                    quantity = int(numberof_items)
                    item_found = False
                    for i, (item, old_quantity) in enumerate(cart):
                        if item == item_to_add:
                            cart[i] = (item_to_add, old_quantity + quantity)
                            item_found = True
                            break
                    if item_found:
                        print(
                            f"{quantity} more {item_to_add.title()}(s) "
                            "have been added to your cart."
                        )
                    else:
                        cart.append((item_to_add, quantity))
                        print(
                            f"{quantity} {item_to_add.title()}(s) "
                            "have been added to your cart."
                        )
        #remove item 
        elif choice == "3":
            item_to_remove = input(
                "Enter the name of the item you want to remove: ").strip().lower()
            found_item = None
            for item, quantity in cart:
                if item == item_to_remove:
                    found_item = (item, quantity)
                    break
            if found_item is not None:
                cart.remove(found_item)
                print(
                    f"{item_to_remove.title()} has been removed "
                    "from your cart."
                )
            else:
                print(
                    f"Sorry, '{item_to_remove.title()}' "
                    "isn't in your cart."
                )
        #double check cart
        elif choice == "4":
            if cart:
                 
                print("Your cart contains:")
                print("-" * 55)
                for item, quantity in cart:
                    price, category = catalog[item]
                    line_total = price * quantity
                print(f"{quantity} x {item.title():<30} ${line_total:>6.2f}")
            else:
                print("Your cart is empty.")
        #checkout
        elif choice == "5":
            if len(cart) == 0:
                print("Your cart is empty. You cannot check out.")
            else:
                reciptmaker()
                break

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
