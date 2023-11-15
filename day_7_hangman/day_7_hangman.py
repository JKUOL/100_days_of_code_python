import random
import day_7_hangman_words
from day_7_hangman_art import stages, logo
import os

def clear():
    # Function to clear the console screen based on the operating system
    if os.name == 'nt':  # If the system is Windows
        _ = os.system('cls')
    else:  # If the system is Unix-based (macOS or Linux)
        _ = os.system('clear')

# Clear the screen before starting the game
clear()

# Choose a random word from the word list module
word = random.choice(day_7_hangman_words.word_list)
# Get the length of the word
word_len = len(word)
# Print the game logo
print(logo)

# Create a display list with underscores for each letter in the word
display = ["_" for _ in word]

# Set the initial number of lives
lives = 6

# Main game loop, runs while there are still underscores and the player has lives left
while "_" in display and lives > 0:
    # Prompt the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in display:
        print(f"You already guessed {guess}")
    
    # Check if the guessed letter is in the word
    for position in range(word_len):
        letter = word[position]
        if letter == guess:
            display[position] = letter

    # If the guessed letter is not in the word, reduce a life and clear the screen
    if guess not in word:
        clear()
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        # Display the corresponding hangman stage
        print(stages[lives])

    # If no lives are left, the game is over
    if lives == 0:
        print("GAME OVER")

    # If there are no more underscores, the player has won
    if "_" not in display:
        print("You won!!!")

    # Print the current state of the display
    print(" ".join(display))
