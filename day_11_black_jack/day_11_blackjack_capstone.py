import os 
from ..clear_function import clear
import random

# ASCII art for the game logo
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Function to calculate the total value of a hand
def cards_value(hand):
    total_value = sum(cards_dict[card] for card in hand)
    return total_value

# Function to get the value of the house's first card
def house_first_card_value(hand):
    value = cards_dict[hand[0]]
    return value

# Clear the screen and display the game logo
clear()
print(logo)
# Prompt to start the game
play = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ")

# Dictionary mapping card names to their values
cards_dict = {
    "2": 2, 
    "3": 3, 
    # ... rest of the cards
    "Ace": 11,
}

# Main game loop
while play == 'y':
    # Deal two random cards for the player and the house
    player_cards = random.sample(sorted(cards_dict.keys()), 2)
    house_cards = random.sample(sorted(cards_dict.keys()), 2) 
    
    # Initial hand values
    player_val = cards_value(player_cards)
    house_val = cards_value(house_cards)
    house_show_val = house_first_card_value(house_cards)

    # Display initial cards and values
    print(f"Your cards: {', '.join(player_cards)}, current score: {player_val} ")
    print(f"The House's first card: {house_cards[0]}, with a score of: {house_show_val}")
    # Ask if the player wants another card
    cont = input("Type 'y' to get another card, type 'n' to pass: ")

    # Player's turn to take additional cards
    while cont == 'y':
        player_cards.append(random.choice(list(cards_dict.keys())))
        player_val = cards_value(player_cards)

        # Check for bust or adjust Ace value
        # ... (continued code for player's turn)

    # House's turn to take cards
    # ... (continued code for house's turn)

    # Determine the game outcome
    # ... (continued code for determining the winner)

    # Prompt for a new game
    play = input("Do you want to play another game of Blackjack? Type 'y' or 'no': ")
    clear()
    print(logo)