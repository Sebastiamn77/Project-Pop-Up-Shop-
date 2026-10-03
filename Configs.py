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

def main():
    print("Welcome to the Green Team Ice Cream Shop!")
    see_menu = input("Would you like to see our menu? (yes/no): ")
    if see_menu.lower() == "yes":
        print("Here is our menu:")
        for item, (price, category) in catalog.items():
            print(f"{item} - ${price:.2f} ({category})")
    imdonenameingthings= input("Type 1 to add an item to your cart, type 2 to view your cart, type 3 to checkout, type 4 to see the menu again, or type 5 to see the menu descriptions: ")
    if imdonenameingthings == "1":
        item_to_add = input("Enter the name of the item you want to add: ")
        if item_to_add in catalog:
            cart.append(item_to_add)
            print(f"{item_to_add} has been added to your cart.")
        else:
            print("Sorry, that item is not on the menu.")
    elif imdonenameingthings == "2":
        if cart:
            print("Your cart contains:")
            for item in cart:
                price, category = catalog[item]
                print(f"{item} - ${price:.2f} ({category})")
        else:
            print("Your cart is empty.")
    elif imdonenameingthings == "3":
        if cart:
            total = sum(catalog[item][0] for item in cart)
            print("Your total is: ${:.2f}".format(total))
            print("Thank you for your order!")
            cart.clear()
        else:
            print("Your cart is empty.")
    elif imdonenameingthings == "4":
        print("Here is our menu:")
        for item, (price, category) in catalog.items():
            print(f"{item} - ${price:.2f} ({category})")
    elif imdonenameingthings == "5":
        print("Here are the descriptions for each item:")
        for item, description in IndeptMenu.items():
            print(f"{item}: {description}")

main() 