# Dynamic Shopping Cart Program

## Overview

This Python program simulates a shopping cart system where users can add items, apply discounts, and view the cart summary. The program allows users to:
1. Add multiple items to the cart.
2. Apply discounts to each item.
3. View a detailed cart summary, including the total cost.

## Features
- **Add Items**: Users can add items by specifying their name, price, and optional details such as color, size, and weight.
- **Apply Discounts**: Users can apply multiple percentage discounts to each item (e.g., 10%, 20%).
- **Item Details**: Users can provide additional details (e.g., color, size) for each item.
- **Cart Summary**: Displays all items with their details, final price after discounts, and the total cost of all items.
- **Duplicate Item Handling**: The program ensures that the same item is not added multiple times to the cart.

## How to Run

### Requirements
- Python 3.x

### Steps to Run
1. Clone the repository or download the `main.py` file.
2. Open the terminal and navigate to the directory containing the `main.py` file.
3. Run the program with the following command:
   ```bash
   python main.py
   ```
4. Follow the on-screen prompts to add items to your cart.

### Example Usage
- When prompted for the item name, type the name of the item (e.g., "Laptop").
- Enter the price of the item (e.g., "1000").
- Optionally, input discounts (e.g., "10 5" for a 10% and 5% discount).
- Enter additional details like "color=red, weight=2kg".
- Type "done" when you are finished adding items to your cart.

### Sample Interaction:
```
Enter item name (or 'done' to finish): Laptop
Enter item price: 1000
Enter discounts (if any, separated by spaces): 10 5
Enter item details (e.g., color=red, size=large): color=black, weight=2kg

Enter item name (or 'done' to finish): Mouse
Enter item price: 50
Enter discounts (if any, separated by spaces): 
Enter item details (e.g., color=red, size=large): color=white

Enter item name (or 'done' to finish): done

--- Cart Summary ---
1. Laptop - $855.0 (color=black, weight=2kg)
2. Mouse - $50.0 (color=white)
Total Cost: $905.0
```

## Code Structure

- **add_to_cart(item_name, price, \*args, \**kwargs)**: Function that handles adding items to the cart and applying discounts.
- **Main program loop**: Handles user input, item addition, and displays the cart summary.
  

## Contact

For any questions or suggestions, please feel free to reach out at: [paulcodes001@gmail.com].