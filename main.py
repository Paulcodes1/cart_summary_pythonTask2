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