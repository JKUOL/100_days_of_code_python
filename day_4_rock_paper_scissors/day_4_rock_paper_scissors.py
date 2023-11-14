import random

# Prompt the player to make a choice between rock, paper, or scissors
player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# Try to convert the player's input to an integer, handle any conversion errors
try:
    player = int(player)
except ValueError:
    # If conversion fails, inform the player and exit the game
    print("Wrong input you lose")
    exit()

# Check if the player's choice is one of the valid options
if player != 0 and player != 1 and player != 2:
    print("Wrong input you lose!")
    quit()

# ASCII art representations for rock, paper, and scissors
rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
 '''
paper = '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'       

 '''
scissors = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
 '''

# List to store the ASCII art for each choice
images = [rock, paper, scissors]
# List to store the names of the gestures
gestures = ["Rock", "Paper", "Scissors"]

# Main game loop that continues as long as the player makes a valid choice
while player == 0 or player == 1 or player == 2:
    # Display the player's choice using the corresponding index in the lists
    print(f"You choose: {gestures[player]}")
    print(images[player])

    # Randomly generate the computer's choice
    computer = random.randint(0,2)
    # Display the computer's choice using the corresponding index in the lists
    print(f"Computer choose: {gestures[computer]}")
    print(images[computer])

    # Determine the game's outcome based on the player's and computer's choices
    if computer == player:
        print("draw")
    elif (computer == 0 and player == 1) or (computer == 1 and player == 2) or (computer == 2 and player == 0):
        print("You saved humankind!")
    else:
        print("The machines took over the world")

    # Ask the player if they want to play another round
    player = input("If you want to play again Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

    # Try to convert the player's input to an integer for the next round
    try:
        player = int(player)
    except ValueError:
        # If conversion fails, thank the player and exit the game
        print("Bye loser")
        exit()

# If the player enters an invalid option outside the main game loop, end the game
else:
    print("Bye loser!")

