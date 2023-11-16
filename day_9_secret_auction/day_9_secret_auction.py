# First price sealed auction, bids get summited secretly (noones knows the bid of other players) hihgest bid wins and pays the price of the highest bid
import os
from clear_function import clear
from day_9_art import logo

# Clear the screen and print the auction logo
clear()
print(logo)

# Function to add a new bidder to the auction dictionary
def add_bider(new_name, new_bid):
    auction[new_name] = new_bid

print("Welcome to our secret auction")

# Initialize the loop control variable and auction dictionary
more_players = "y"
auction = {}

# Main loop to accept bids
while more_players in ["y", "yes"]:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    add_bider(name, bid)
    more_players = input("Are there any other bidders? Type 'yes' or press any other key to quit\n")
    clear()
    # Print the current highest bid
    print(max(auction.values()))

# Calculate the highest bid and the winner
highest_bid = max(auction.values())
winner = max(auction, key=lambda x: auction[x])

# Announce the winner and their bid
print(f"The winner of the auction is {winner} with a bid of {highest_bid}€")






