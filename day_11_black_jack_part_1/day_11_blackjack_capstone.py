import os 
from clear_function import clear
import random

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

def cards_value(hand):
    total_value = sum(cards_dict[card] for card in hand)
    return total_value

def house_first_card_value(hand):
    for card in hand:
        value = cards_dict[card]
        return value


clear()
print(logo)
play = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ")

cards_dict = {
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5, 
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9, 
    "10": 10, 
    "Jack": 10, 
    "Queen": 10, 
    "King": 10, 
    "Ace": 11,
}

while play == 'y':
    player_cards = random.sample(sorted(cards_dict.keys()), 2)
    house_cards = random.sample(sorted(cards_dict.keys()), 2) 
    
    player_val = cards_value(player_cards)
    house_val = cards_value(house_cards)
    house_show_val = house_first_card_value(house_cards)

    print(f"Your cards: {', '.join(player_cards)}, current score: {player_val} ")
    print(f"The Houses first card: {house_cards[0]}, with a score of: {house_show_val}")
    cont = input("Type 'y' to get another cards, type 'n' to pass: ")

    while cont == 'y':
        player_cards.append(random.choice(list(cards_dict.keys())))

        player_val = cards_value(player_cards)

        print(f"Your cards: {', '.join(player_cards)}, current score: {player_val} ")
        if 'Ace' in player_cards and player_val > 21:
            cards_dict["Ace"] == 1
        if player_val > 21:
            clear()
            print("You lost")
            cont = 'n'
            break
        
        cont = input("Type 'y' to get another cards, type 'n' to pass: ")

    if player_val < 22:
        cards_dict["Ace"] == 11
        print(f"Your cards: {', '.join(player_cards)}, current score: {player_val} ")
        print(f"The Houses cards are: {', '.join(house_cards)}, with a score of: {house_val}")
        while house_val < 16:
            house_cards.append(random.choice(list(cards_dict.keys())))
            house_val = cards_value(house_cards)
            print(f"Your cards: {', '.join(player_cards)}, current score: {player_val} ")
            print(f"The Houses cards are: {', '.join(house_cards)}, with a score of: {house_val}")
            if 'Ace' in house_cards and house_val > 21:
                cards_dict["Ace"] == 1
            elif house_val > 21:
                print("The House lost")
                cont = 'n'
                break
    
    if house_val < 22 and house_val > player_val or house_val == player_val:
        print(f"The House won with a score of {house_val} against your score of {player_val}")
    elif player_val < 22:
        print(f"You won with a score of {player_val} against the house with score of {house_val}")

    play = input("Do you want to play another game of Blackjack? Type 'y' or 'no': ")
    clear()
    print(logo)
