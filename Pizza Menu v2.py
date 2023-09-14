import pandas

name = input("Please enter your name: ")

# Dictionaries to hold pizza details
all_pizzas = ["Hawaiian", "Pepperoni", "Vegetarian", "Simply Cheese", "Ice Cream Pizza"]
all_extras = ["Cheese", "Mushrooms", "Olives", "Pineapple", "Peppers"]
all_prices = [9.5, 8.5, 9.5, 8.0, 11.0]
extra_prices = [0.5, 1.0, 1.0, 0.75, 1.0]


pizza_dict = {
    "Pizzas": all_pizzas,
    "Prices": all_prices,
    "Extras": all_extras,
    "Extra Prices": extra_prices
}

pizza_menu_frame = pandas.DataFrame(pizza_dict)
pizza_menu_frame = pizza_menu_frame.set_index('Pizzas')

# Heading
heading = "Pizza Menu"

# Change frame to string so we can export
pizza_menu_string = pandas.DataFrame.to_string(pizza_menu_frame)

# List holding content to print / write to file
to_write = [heading, pizza_menu_string]

# Print output
for item in to_write:
    print(item)

def choose_pizza():
    while True:
        print("Available pizzas:")
        for index, pizza in enumerate(all_pizzas, start=1):
            print(f"{index}. {pizza}")

        pizza_choice = input("Please enter the number of the pizza you want (1-5): ")

        if pizza_choice.isdigit() and 1 <= int(pizza_choice) <= len(all_pizzas):
            return int(pizza_choice)
        else:
            print("Invalid pizza choice. Please enter a number between 1 and 5.")

def choose_sizes(pizza_choice):
    pizza_name = all_pizzas[pizza_choice - 1]
    while True:
        pizza_size = input(f"Please enter the size of your {pizza_name} pizza (Small/Medium/Large): ").lower()

        if pizza_size == "small" or pizza_size == "s":
            return "Small: $" + str(all_prices[pizza_choice - 1] * 0.8)
        elif pizza_size == "medium" or pizza_size == "m":
            return "Medium: $" + str(all_prices[pizza_choice - 1])
        elif pizza_size == "large" or pizza_size == "l":
            return "Large: $" + str(all_prices[pizza_choice - 1] * 1.2)
        else:
            print("Invalid size entered. Please choose from Small, Medium, or Large.")


def choose_extras():
    selected_extras = []
    while True:
        print("Available extras:")
        for index, extra in enumerate(all_extras, start=1):
            print(f"{index}. {extra} - ${extra_prices[index-1]:.2f}")

        extra_choice = input("Please enter the number of the extra you want (1-5) or 'xxx' to stop: ")

        if extra_choice == 'xxx':
            break

        if extra_choice.isdigit() and 1 <= int(extra_choice) <= len(all_extras):
            selected_extras.append(int(extra_choice))
        else:
            print("Invalid extra choice. Please enter a number between 1 and 5 or 'xxx' to stop.")

    return selected_extras

total_order_cost = 0


while True:

    while True:
        # Get the selected pizza
        selected_pizza = choose_pizza()
        pizza_name = all_pizzas[selected_pizza - 1]
        print(f"You've selected {pizza_name} pizza.")

        # Get the selected pizza size
        selected_size = choose_sizes(selected_pizza)
        print(f"The total price for your {selected_size.split(':')[0]} pizza is ${float(selected_size.split('$')[1]):.2f}")

        # Get the selected extras
        selected_extras = choose_extras()
        total_extra_cost = sum(extra_prices[extra - 1] for extra in selected_extras)
        selected_extra_names = [all_extras[extra - 1] for extra in selected_extras]
        selected_extra_prices = [extra_prices[extra - 1] for extra in selected_extras]
        print("Selected extras:")
        for i in range(len(selected_extra_names)):
            print(f"{selected_extra_names[i]} - ${selected_extra_prices[i]:.2f}")
        print(f"The total cost of extras is ${total_extra_cost:.2f}")

        # Calculate the total cost
        total_cost = float(selected_size.split('$')[1]) + total_extra_cost
        total_order_cost += total_cost
        print(f"The total cost for your order is ${total_cost:.2f}")

        another_order = input("Would you like to order another pizza? (yes/no): ").lower()
        if another_order != "yes" and another_order != "y":
            break

    # Print receipt
    print("\nReceipt:")
    print(f"Name: {name}")
    print(f"Pizza: {pizza_name}")
    print(f"Size: {selected_size.split(':')[0]}")
    if selected_extra_names:
        print("Selected extras:")
        for i in range(len(selected_extra_names)):
            print(f"{selected_extra_names[i]} - ${selected_extra_prices[i]:.2f}")
    print(f"Total order cost: ${total_order_cost:.2f}")

    # Ask for confirmation
    confirmation = input("Would you like to confirm your order? (yes/no): ").lower()
    if confirmation == "yes" or confirmation == "y":
        print("Thank you for ordering", name)

        break

    else:
        print("Your order has not been confirmed.")

        # Ask if they want to make another order
        another_order = input("Would you like to make another order? (yes/no): ").lower()
        if another_order == "yes" or another_order == "y":
            # Reset the order details
            total_order_cost = 0

            continue

        else:
            print("Thank you for considering our menu.")

            break
