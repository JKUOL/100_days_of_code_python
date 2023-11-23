# Class definition for MoneyMachine
class MoneyMachine:

    CURRENCY = "$"
    # Define the value of each type of coin
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        # Initialize the machine's profit and money received
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        # Print out the current profit
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        # Prompt the user to insert coins
        print("Please insert coins.")
        # Calculate the total money inserted based on the coins
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        # If enough money is received, calculate change, update profit, and return True
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            # If not enough money is received
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False