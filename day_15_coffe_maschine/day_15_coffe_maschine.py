# Import the clear function 
from clear_function import clear

# A dictionary representing the menu with drink names, their ingredients, and cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Variable to keep track of money earned
profit = 0

# Dictionary that holds the information about the machine's current resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Function to check if the machine has sufficient resources to make the drink
def is_resource_sufficient(order_ingredients):
    """Returns True if order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Function to process coins inserted by the user
def process_coin():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# Function to check if the payment is successful
def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Function to make the coffee, deducting the ingredients from the resources
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️.")

# Flag to control the coffee machine operation
is_on = True

# Clear the terminal screen before starting the program
clear()

# Main loop that runs while the machine is on
while is_on:
    # Display the menu with costs
    print(f"Espresso: ${MENU['espresso']['cost']}, Latte: ${MENU['latte']['cost']}, Cappuccino: ${MENU['cappuccino']['cost']}")
    # Prompt the user to choose a drink
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # Check if the user wants to turn off the machine
    if choice == "off":
        is_on = False
    # Check if the user wants to print the report of resources and money
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    # If the user selects a drink
    else:
        drink = MENU[choice]
        # Check if resources are sufficient for the drink
        if is_resource_sufficient(drink['ingredients']):
            # Process the coins inserted by the user
            payment = process_coin()
            # Check if the transaction is successful
            if is_transaction_successful(payment, drink['cost']):
                # Make the coffee if the transaction is successful
                make_coffee(choice, drink['ingredients'])
