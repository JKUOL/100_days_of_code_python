import os
from clear_function import clear

# Initial display value for the ASCII art calculator
display = 0

# ASCII Art for the calculator logo, including the display
logo = f""" ... """

# Clear the screen and print the calculator logo
clear()
print(logo)

# Functions for each arithmetic operation
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

# Dictionary mapping operation symbols to corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

# Main function for the calculator operation
def calculator():
    clear()
    print(logo)
    num1 = float(input("What's the first number?: "))
    
    # Print out all available operations
    for operation in operations:
        print(operation)
    
    # Flag to determine if the calculation should continue
    should_continue = True

    # Main calculation loop
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        clear()
        
        # Update the calculator display with the answer
        logo2 = f""" ... {answer} ... """
        print(logo2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        # User choice to continue with current calculation, start a new one, or exit
        cont = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or any other key to exit: ")
        clear()
        print(logo2)
        
        if cont == 'y':
            num1 = answer
        elif cont == 'n':
            should_continue = False
            calculator()
        else:
            break

# Start the calculator
calculator()
