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
                discount = int(percent) / 100
            else:
                print("Invalid promo code. No discount will be applied.")
        print("=" * 36)
        print("RECEIPT".center(36))
        print(f"Customer: {configs.customer_name}")
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
        print("=" * 36)
        print("Total: ${:.2f}".format(total_with_tax))
        print("=" * 36)
    else:
        print("Your cart is empty.")