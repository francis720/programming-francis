import pandas

name = input("Please enter your name: ")

# dictionaries to hold ticket details
all_pizzas = ["Hawaiian", "Pepperoni", "Vegetarian", "Simply Cheese", "Ice Cream Pizza"]
all_extras = ["Cheese", "Mushrooms", "Olives", "Pineapple", "Peppers"]
all_prices = [9.5, 9.5, 9.5, 9.5, 9.5]
extra_prices = [.5, 1.00, 1.00, .75, 1.00]


pizza_dict = {
    "Pizzas": all_pizzas,
    "Prices": all_prices,
    "Extras": all_extras,
    "Extra Prices": extra_prices
}

pizza_menu_frame = pandas.DataFrame(pizza_dict)
pizza_menu_frame = pizza_menu_frame.set_index('Pizzas')

# heading
heading = "Pizza Menu"



# calculate pizza cost
#pizza_menu_frame[all_pizzas] = pizza_menu_frame[all_prices]

# calculate extras cost
#pizza_menu_frame[all_extras] = pizza_menu_frame[all_prices]

# Currency format
#add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
#for var_item in add_dollars:
 #   pizza_menu_frame[var_item]

# change frame to string so we can export
pizza_menu_string = pandas.DataFrame.to_string(pizza_menu_frame)


# list holding content to print / write to file
to_write = [heading, pizza_menu_string]

# print output
for item in to_write:
    print(item)

while True:
    want_pizza_size = input("Do you want the list of sizes? ").lower()

    if want_pizza_size == "yes" or want_pizza_size == "y":
        print("small: 7.0")
        print("Medium: 9.50")
        print("Large: 11.00")

    elif want_pizza_size == "no" or want_pizza_size == "n":
        break
    else:
        print("please answer yes / no")
        pass
pizza_size = input("Please enter the size of your pizza")

if pizza_size == "small" or pizza_size == "s":
        return "price = 7.0"
    elif response == "no" or response == "n":
        return "no"
    else:
        print("please enter yes or no")