import random

player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

try:
    player = int(player)
except ValueError:
    print("Wrong input you lose")
    exit()

if player != 0 and player != 1 and player != 2:
    print("Wrong input you lose!")
    quit()

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

images = [rock, paper, scissors]
gestures = ["Rock", "Paper", "Scissors"]

while player == 0 or player == 1 or player == 2:
    if player == 0:
        print(f"You choose: {gestures[player]}")
        print(images[player])

    if player == 1:
        print(f"You choose: {gestures[player]}")
        print(images[player])

    if player == 2:
        print(f"You choose: {gestures[player]}")
        print(images[player])

    computer = random.randint(0,2)

    if computer == 0:
        print(f"Computer choose: {gestures[computer]}")
        print(images[computer])
        
    if computer == 1:
        print(f"Computer choose: {gestures[computer]}")
        print(images[computer])
        
    if computer == 2:
        print(f"Computer choose: {gestures[computer]}")
        print(images[computer])

    if computer == player:
        print("draw")
    elif computer == 0 and player == 1:
        print("You saved humandkind!")
    elif computer == 0 and player == 2:
        print("The maschines took over the world")
    elif computer == 1 and player == 0:
        print("The maschines took over the world")
    elif computer == 1 and player == 2:
        print("You saved humankind!")
    elif computer == 2 and player == 0:
        print("You saved humankind!")
    elif computer == 2 and player == 1:
        print("The maschines took over the world")

    player = input("If you want to play again Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

    try:
        player = int(player)
    except ValueError:
        print("Bye loser")
        exit()

else:
    print("Bye loser!")
