# Define a variable to store the input
name = input("Please enter your name: ")
# Print the input
print("Hello, " + name + "! Welcome to Francisco's Pizza Palace.")

while True:
    want_instructions = input("Do you want instructions? ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("Please choose from the variety of pizzas we offer. ")
        print("Then choose the size of the pizza. ")
        print("You can continue making orders or stop if you wish. ")
        print("You will be asked if you want it delivered or to pickup. ")
        print("Delivery will cost $5.00")

    elif want_instructions == "no" or want_instructions == "n":
        break
    else:
        print("please answer yes / no")
