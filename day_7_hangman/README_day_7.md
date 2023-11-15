# Hangman Game
This project contains a Python implementation of the classic game Hangman. The player attempts to guess a word by suggesting letters within a certain number of guesses.

## Features
Word List: A separate module (day_7_hangman_words) contains a list of words, one of which is randomly selected as the secret word for the game.

Visuals: ASCII art from day_7_hangman_art represents the hangman stages and the game logo.

Clear Screen: The screen is cleared after each guess to keep the interface clean, which is compatible with both Windows (cls) and Unix-based systems (clear).

Guessing: The player inputs letters as guesses and receives immediate feedback.

Lives System: The player starts with a set number of lives that decrease on incorrect guesses.

## Instructions

Clone the repository to your local machine.
Ensure that Python 3.x is installed.
Run the main game file in your terminal or command prompt.
Follow the on-screen prompts to guess letters.
Try to guess the word before your lives run out.

## Requirements

Python: Python 3.x

Operating System: This script is compatible with Windows, macOS, and Linux operating systems.

Command Line Interface: The game is run in the terminal or command prompt.


## Educational Value

This game is a great way to practice Python skills, including:

Modular Programming: Using separate modules for different parts of the game.

List Comprehensions: Manipulating lists to create game dynamics.

Looping: Using while loops for the game's main execution cycle.

Conditional Statements: Implementing game logic with if statements.