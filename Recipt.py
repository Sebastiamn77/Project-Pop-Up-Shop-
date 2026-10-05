import configs 
# don't touch this ALEX
# Reference the configs.varibles in this file using configs.variable_name, so that it works.
# This makes things neater and easier to read but is mostly for the sake of coolness. 
#Alex's part

def reciptmaker():
    if configs.cart:
        total = 0
        subtotal = 0
        item_total = 0
        discount = 0.0
        TAX_RATE = configs.TAX_RATE

        promo = input("Promo code (Enter to skip): ").strip().lower()
        if promo.startswith("save"):
            percent = promo[4:]
            if percent.isdigit():
                discount = min(0.5, int(percent) / 100)  # Cap discount at 50%
            else:
                print("Invalid promo code. No discount will be applied.")
        else:
            print("Invalid promo code. No discount will be applied.")
        print("=" * 36)
        print("RECEIPT".center(36))
        print(f"Customer: {configs.customer_name}")
        print(f"Customer Code: {configs.customer_name[:3].upper()}-{len(configs.cart)}")
        print("-" * 36)
        
        for item, quantity in configs.cart:
            price, category = configs.catalog[item]
            item_total += price * quantity
            subtotal += item_total
            print(f"{quantity} x {item} - ${price:.2f} ({category})")
        print("Subtotal: ${:.2f}".format(subtotal))
        if discount > 0:
            discount_amount = subtotal * discount
            total = subtotal - discount_amount
            print("Discount: -${:.2f}".format(discount_amount))
        else:
            total = subtotal
        tax = total * TAX_RATE
        total_with_tax = total + tax
        print("Tax (7%): ${:.2f}".format(tax))
        print("-" * 36)
        print("Items by Category:")
        # for category in ["Scoop", "Shake", "Pastry"]:
        #     print(f"  {category}:")
        #     number_of_items = 0
        #     for item, quantity in configs.cart:
        #         _, item_category = configs.catalog[item]
        #         number_of_items += quantity
        #         if number_of_items > 0 and item_category == category:
        #             print(f"    {number_of_items}")
        print("=" * 36)
        print("Total: ${:.2f}".format(total_with_tax))
        print("=" * 36)
    else:
        print("Your cart is empty.")