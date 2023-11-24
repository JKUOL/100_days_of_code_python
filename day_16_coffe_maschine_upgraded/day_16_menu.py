# Class definition for MenuItem
class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        # Set up the menu item's name, ingredients, and cost
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

# Class definition for the Menu
class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        # Define the available drinks in the menu
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        # Concatenate the names of each menu item into a single string
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options.strip('/')

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None."""
        # Search for the drink in the menu by its name
        for item in self.menu:
            if item.name == order_name:
                return item
        # If the drink is not found, print a message
        print("Sorry that item is not available.")