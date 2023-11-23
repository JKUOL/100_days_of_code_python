# Class definition for the CoffeeMaker
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        # Initial resources in the coffee maker
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        # Print out the current resource levels
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # Check if each required ingredient is available
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                # If any ingredient is insufficient, print a message and return False
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        # Deduct the required ingredients from the resources
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        # Print a confirmation message
        print(f"Here is your {order.name} ☕️. Enjoy!")
