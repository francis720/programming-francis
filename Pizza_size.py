def get_pizza_price(size):
    size = size.lower()
    if size == "small":
        return 7.00
    elif size == "medium":
        return 9.50
    elif size == "large":
        return 11.00
    else:
        return None

# Ask the user for the pizza size
size = input("Please enter the size of pizza you want (Small/Medium/Large): ")

# Get the pizza price based on the selected size
price = get_pizza_price(size)

if price is not None:
    print(f"The total price for your {size} pizza is ${price:.2f}")
else:
    print("Invalid size entered. Please choose from Small, Medium, or Large.")