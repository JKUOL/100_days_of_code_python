# Import the 'random' module to generate random selections
import random
# Import the 'os' module to interact with the operating system
import os
# Import the 'clear' function from the 'clear_function' module to clear the console
from clear_function import clear
# Import 'logo' and 'vs' variables from the 'day_14_art' module which contain string art
from day_14_art import logo, vs
# Import the 'data' list from the 'day_14_data' module which contains Instagram account data
from day_14_data import data

# Clear the console screen
clear()

# Define a function to get a random account from the 'data' list
def get_random_account():
  return random.choice(data)

# Define a function to format the data of an account into a string
def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

# Define a function to check the user's guess against the actual follower counts
def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

# Define the main game function
def game():
  # Display the game logo
  print(logo)
  # Prompt the game's main question
  print("Who has more Instagram followers?")
  # Initialize the score to 0 at the start of the game
  score = 0
  # Set a flag to keep the game running until the player loses
  game_should_continue = True
  # Get the initial two random accounts to compare
  account_a = get_random_account()
  account_b = get_random_account()

  # Start the game loop
  while game_should_continue:
    # Assign the second account as the first to compare against a new second account
    account_a = account_b
    account_b = get_random_account()

    # Ensure that the new second account is not the same as the first
    while account_a == account_b:
      account_b = get_random_account()

    # Print the data for the first account to compare
    print(f"Compare A: {format_data(account_a)}.")
    # Display the versus art
    print(vs)
    # Print the data for the second account to compare
    print(f"Against B: {format_data(account_b)}.")
    
    # Get the player's guess and convert it to lowercase
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # Retrieve the follower counts for comparison
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # Check if the player's guess is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the console after each guess
    clear()
    # Display the logo again
    print(logo)
    # If the player is correct, increment the score and display it
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    # If the player is wrong, end the game and show the final score
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

# Set a flag to repeat the game based on player's choice
repeat_game = True
# Start the loop for repeating the game
while repeat_game:
    # Clear the console before starting a new game
    clear()
    # Call the game function to start a new game
    game()
    # Ask the player if they want to play again
    if input("Press 'y' to play again: ") != 'y':
      # If the player does not press 'y', change the flag to False to end the loop
      repeat_game = False
