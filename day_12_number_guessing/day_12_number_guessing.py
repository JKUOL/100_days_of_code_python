# Importing necessary libraries
import random
import os
# Importing the clear function from a file named clear_function.py
from clear_function import clear

# Calling the clear function to clear the terminal screen
clear()

# Function to set the difficulty level of the game
def difficulty_func():
    # Asking the player to choose a difficulty level
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    # Setting the number of tries based on the chosen difficulty
    if difficulty == "easy":
        trys = 10
    else:
        trys = 5
    # Returning the number of tries
    return trys

# Main game function
def game():
    # Printing the welcome message and game instructions
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Initializing the variable to start the game loop
    new_try = 'y'
    # Starting the game loop
    while new_try == 'y' or new_try == 'yes':
        # Generating a random number between 1 and 100 inclusive
        number = random.randint(1, 101)
        # Setting the number of lives based on the difficulty function
        lives = difficulty_func()
        # Informing the player of the number of tries they have
        print(f"You get {lives} trys to guess the correct answer!\n")
        # Asking the player for their first guess
        player_number = int(input("Guess a number: "))
        # Starting the guessing loop
        while lives > 0:
            # If the player's guess is correct
            if number == player_number:
                print(f"You won! {number} is the correct guess!")
                break
            # If the guess is too low and the player has more than one life
            elif number > player_number and lives > 1:
                lives -= 1
                player_number = int(input(f"To low, you have {lives} try(s) left. \nGuess again: "))
            # If the guess is too high and the player has more than one life
            elif number < player_number and lives > 1:
                lives -= 1
                player_number = int(input(f"To high, you have {lives} try(s) left. \nGuess again: "))
            # If the player is on their last life and hasn't guessed correctly
            if lives == 1 and number != player_number:
                print(f"You lost, the correct number was {number}")
                break
        # Asking if the player wants to play again
        new_try = input("Type 'y' to play again, if you want to quit press any other key: ").lower()

    # Printing a farewell message when the player chooses to quit
    print("Have a nice day!")

# Starting the game by calling the game function
game()