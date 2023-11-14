# Rock, Paper, Scissors Game
This Python script is an interactive take on the classic game "Rock, Paper, Scissors" where the player competes against the computer.

## How It Works
The game progresses as follows:

### Starting the Game:

The player is greeted with a prompt to choose rock, paper, or scissors by entering 0, 1, or 2, respectively.

### Input Validation:

The script includes error handling to ensure the player inputs a valid number. If an invalid input is detected, the game ends with a loss.

### Gameplay Loop:

Once a valid choice is made, the player's choice and the corresponding ASCII art are displayed.
The computer's choice is generated randomly and displayed along with its ASCII art.

### Determining the Outcome:

The game compares the player's choice with the computer's and prints the outcome of the round.
Players can continue to play new rounds by inputting new choices or exit the game.

### End of the Game:

If the player enters an invalid choice at any point after the initial round, the game ends.

## Educational Value
This script is a helpful resource for learners, teaching several concepts:

### Error Handling:

Illustrates the use of try-except blocks to manage exceptions and ensure user input is within the expected range.

### Control Flow:

Shows how if-else statements can determine the game's logic and outcomes.

### While Loops:

Demonstrates the use of a while loop to keep the game running until the player decides to quit.

### Randomness:

Uses the random module to simulate the computer's choices, introducing randomness in programming.

### ASCII Art:

Enhances the visual appeal of the console output using ASCII art representations of the player's and computer's choices.

## Requirements
To run the Rock, Paper, Scissors game, ensure the following:

Python 3.x: Verify Python 3 is installed on your system. You can download it from the official Python website if needed.
Command Line Interface: You will need a terminal (macOS/Linux) or Command Prompt/PowerShell (Windows) to run the script.

## Instructions to Run the Game
Download the rock_paper_scissors.py script from the repository.
Open your terminal or command line interface.
Navigate to the directory where you have saved the script.
Execute the script by typing python rock_paper_scissors.py and pressing Enter.
Follow the on-screen prompts to play the game.