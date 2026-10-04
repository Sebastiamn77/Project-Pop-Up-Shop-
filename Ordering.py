import configs
import Recipt
# Sebastians part 
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
                for item, (price, category) in configs.catalog.items():
                    if category == "Shake":
                        print(f"{item:<35} {category:<10} ${price:>5.2f}")
            elif menutype == "ice cream":
                print("Here are our ice creams:")
                print("-" * 55)
                for item, (price, category) in configs.catalog.items():
                    if category == "Scoop":
                        print(f"{item:<35} {category:<10} ${price:>5.2f}")
            elif menutype == "pastries":
                print("Here are our pastries:")
                print("-" * 55)
                for item, (price, category) in configs.catalog.items():
                    if category == "Pastry":
                        print(f"{item:<35} {category:<10} ${price:>5.2f}")
            else:
                print("Invalid menu type. Please choose Shakes, Ice Cream, or Pastries.")

        # Add Item
        elif choice == "2":
            item_to_add = input(
                "Enter the name of the item you want to add: ").strip().title()
            if item_to_add in configs.catalog:
                numberof_items = input(
                    "How many of this item would you like to add? "
                ).strip()
                if not numberof_items.isdigit() or int(numberof_items) == 0:
                    print("Quantity must be a whole number greater than 0.")
                else:
                    quantity = int(numberof_items)
                    item_found = False
                    for i, (item, old_quantity) in enumerate(configs.cart):
                        if item == item_to_add:
                            configs.cart[i] = (item_to_add, old_quantity + quantity)
                            item_found = True
                            break
                    if item_found:
                        print(
                            f"{quantity} more {item_to_add.title()}(s) "
                            "have been added to your cart."
                        )
                    else:
                        configs.cart.append((item_to_add, quantity))
                        print(
                            f"{quantity} {item_to_add.title()}(s) " "have been added to your cart.")
            else:
                print(
                    f"Sorry, '{item_to_add.title()}' is not on the menu. "
                    "Please check the menu and try again."
                )
        #remove item 
        elif choice == "3":
            item_to_remove = input(
                "Enter the name of the item you want to remove: ").strip().title()
            found_item = None
            for item, quantity in configs.cart:
                if item == item_to_remove:
                    found_item = (item, quantity)
                    break
            if found_item is not None:
                configs.cart.remove(found_item)
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
            if configs.cart:
                 
                print("Your cart contains:")
                print("-" * 55)
                for item, quantity in configs.cart:
                    price, category = configs.catalog[item]
                    line_total = price * quantity
                print(f"{quantity} x {item.title():<30} ${line_total:>6.2f}")
            else:
                print("Your cart is empty.")
        #checkout
        elif choice == "5":
            if len(configs.cart) == 0:
                print("Your cart is empty. You cannot check out.")
            else:
                Recipt.reciptmaker()
                break
        else:
            print("Invalid choice. Please choose a valid option.")

