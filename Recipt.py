import Configs 
# don't touch this ALEX
# Reference the configs.varibles in this file using configs.variable_name, so that it works.
# This makes things neater and easier to read but is mostly for the sake of coolness. 
#Alex's part

def reciptmaker():
    if Configs.cart:
        total = 0
        subtotal = 0
        item_total = 0
        discount = 0.0
        TAX_RATE = Configs.TAX_RATE
        count_category = {}

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
        print(f"Customer: {Configs.customer_name}")
        print(f"Customer Code: {Configs.customer_name[:3].upper()}-{len(Configs.cart)}")
        print("-" * 36)
        
        for item, quantity in Configs.cart:
            price, category = Configs.catalog[item]
            item_total = price * quantity
            subtotal += item_total
            print(f"{quantity} x {item} - ${price:.2f} ({category})")

            if category not in count_category:
                count_category[category] = 0
            count_category[category] += quantity

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
        
        for category, count in count_category.items():
            print(f"  {category}: {count}")
        
        print("=" * 36)
        print("Total: ${:.2f}".format(total_with_tax))
        print("=" * 36)
    else:
        print("Your cart is empty.")