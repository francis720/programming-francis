all_extras = ["Cheese", "Mushrooms", "Olives", "Pineapple", "Peppers"]
extra_prices = [0.5, 1.0, 1.0, 0.75, 1.0]

def choose_extras():

    selected_extras = []
    while True:
        print("Available extras:")
        for index, extra in enumerate(all_extras, start=1):
            print(f"{index}. {extra}")

        extra_choice = input("Please enter the number of the extra you want (1-5) or 'xxx' to stop: ")

        if extra_choice == 'xxx':
            break

        if extra_choice.isdigit() and 1 <= int(extra_choice) <= len(all_extras):
            selected_extras.append(int(extra_choice))
        else:
            print("Invalid extra choice. Please enter a number between 1 and 5 or 'xxx' to stop.")

    return selected_extras

# Get the selected extras
selected_extras = choose_extras()
total_extra_cost = sum(extra_prices[extra - 1] for extra in selected_extras)
print(f"Selected extras: {', '.join(all_extras[extra - 1] for extra in selected_extras)}")
print(f"The total cost of extras is ${total_extra_cost:.2f}")
