"""
    Shopping cart simulation
"""

# Function to add items to cart
def add_to_cart(item_name, price, *args, **kwargs):
    # Get final price
    final_price = price
    for discount in args:
        final_price -= final_price * (discount / 100)

    # Storing item details
    item_details = {
        "name": item_name,
        "final_price": round(final_price, 2),
        **kwargs
    }

    return item_details

"""
    MAIN PROGRAM LOOP
"""

# A dictionary storage for the items
cart = {}

while True:
    
    # Taking User inputs
    item_name = input("Enter item name (or 'done' to finish): ").strip()
    if item_name.lower() == 'done':
        break

    try:
        price = float(input("Enter item price: "))
    except ValueError:
        print("Invalid price. Please enter a numeric value.")
        continue

    discounts = input("Enter discounts (if any, separated by spaces): ").split()
    discounts = [float(d) for d in discounts if d.isdigit()] # Convert to numbers

    details_input = input("Enter item details (e.g., color=red, size=large): ").strip()
    details = {}
    if details_input:
        for detail in details_input.split(","):
            key, value = detail.split("=")
            details[key.strip()] = value.strip()


    if item_name in cart:
        print(f"{item_name} is already in the cart.")
    else:
        cart[item_name] = add_to_cart(item_name, price, *discounts, **details)
        print(f"Item added: {item_name} - Final Price: ${cart[item_name]['final_price']}")

#Display Cart Summary
print("\n--- Cart Summary ---")
total_cost = 0

counter = 1

for item_name, details in cart.items():
    detail_str = ", ".join(f"{key}={value}" for key, value in details.items() if key not in ["name", "final_price"])
    print(f"{counter}. {item_name} - ${details['final_price']} ({detail_str})")

    # Calculate and display total cost
    total_cost += details['final_price']

    # Increment counter for the next item
    counter += 1

# Print the total cost
print(f"Total Cost: ${round(total_cost, 2)}")