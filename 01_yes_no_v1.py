# functions


# main routine
while True:
    want_instructions = input("Do you want instructions? ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("Welcome to Franciscos Pizza Palace")
        print("Please choose from the variety of pizzas we offer. ")
        print("Then choose the size of the pizza. ")
        print("You can continue making orders or stop if you wish. ")
        print("You will be asked if you want it delivered or to pickup. ")
        print("Delivery will cost $5.00")

    elif want_instructions == "no" or want_instructions == "n":
        pass
    else:
        print("please answer yes / no")
