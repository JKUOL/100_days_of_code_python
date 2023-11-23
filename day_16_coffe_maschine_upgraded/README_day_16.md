# Object-Oriented Coffee Machine Program README

## Introduction
This Python program emulates a coffee machine using an object-oriented programming approach. It features classes for menu items, coffee-making, and financial transactions, which interact to provide a simulated coffee vending experience. Users can choose from a selection of coffee drinks, which the program can prepare and sell based on available resources and customer payments.

## Features
- **Class `CoffeeMaker`**: Represents the machine that makes the coffee, tracking and managing resources like water, milk, and coffee.
- **Class `MenuItem`**: Defines the blueprint for each drink available in the menu, including its ingredients and cost.
- **Class `Menu`**: Contains a collection of `MenuItem` objects and methods to get menu items and find a specific drink.
- **Class `MoneyMachine`**: Handles the financial aspects, processing coins and managing profit and payments.
- **User Interaction**: Through command line prompts, users can order drinks, check machine reports, or turn off the program.

## Requirements
- **Python 3.x**: This program is written in Python and requires Python 3.x to run.

## Installation
1. Clone or download the repository containing the source code.
2. Ensure all class files (`day_16_menu.py`, `day_16_coffee_maker.py`, `day_16_money_machine.py`) are in the same directory.

## Usage
1. Execute the main script in your preferred Python environment.
2. Interact with the program via the command line interface, choosing a drink from the menu.
3. Use the 'report' command to get a status update on resources and finances.
4. To exit the program, type the 'off' command.

## Educational Value
- **Object-Oriented Programming (OOP)**: Demonstrates the use of OOP for structuring a program into modular and reusable pieces of code.
- **Encapsulation and Abstraction**: Each class encapsulates specific functionality and abstracts its implementation from the user.
- **Resource Management**: Highlights how to manage and track resources within a class.
- **Financial Transactions**: Teaches handling of basic financial transactions within a software application.
- **Modular Development**: Encourages the development of modular code for easier maintenance and scalability.

