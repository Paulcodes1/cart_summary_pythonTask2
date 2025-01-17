# Program that simulates a shopping cart

item_name = input("Enter item name(or 'done' to finish): ")
price = input("Enter item price: ")
discounts = input("Enter discounts(if any, separated by spaces): ").split(" ")
item_details = input("Enter item details(e.g, color=red size=large): ")

def add_to_cart(item_name, price, *discounts, **item_details) -> str :
    #print("---Cart Summary---")
    
    return (item_name, price, discounts, item_details)

cart = add_to_cart(item_name, price, discounts, item_details)
print(cart)