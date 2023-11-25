# Import Turtle and Screen classes from the turtle module.
from turtle import Turtle, Screen
# Import the random module for generating random numbers.
import random
# Import a custom clear function to clear the console screen after the race.
from clear_function import clear

# Flag to indicate whether the race has started.
is_race_on = False
# Create a new screen object to display the race.
screen = Screen()
# Set the screen dimensions.
screen.setup(width=500, height=400)
# Prompt the user to place a bet on a turtle color.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# Define the colors of the turtles.
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# List to keep track of all turtle objects.
all_turtles = []

# Starting y-coordinate for the first turtle.
y = -100
# Create six turtles, each with a different color, and place them on the screen.
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # Create a new turtle with the shape of a turtle.
    new_turtle.color(colors[turtle_index])  # Set the turtle's color.
    new_turtle.pu()  # Pull up the pen to prevent drawing lines.
    new_turtle.goto(x=-230, y=y)  # Position the turtle at the start line.
    y += 30  # Increment the y-coordinate for the next turtle.
    all_turtles.append(new_turtle)  # Add the new turtle to the list of turtles.

# If the user places a bet, start the race.
if user_bet:
    is_race_on = True

# The race loop, which continues until one turtle crosses the finish line.
while is_race_on:
    # Iterate through each turtle and move it forward a random distance.
    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line (x-coordinate > 230).
        if turtle.xcor() > 230:
            # Stop the race as a turtle has crossed the finish line.
            is_race_on = False
            # Get the color of the winning turtle.
            winning_color = turtle.pencolor()
            # Check if the winning color matches the user's bet.
            if winning_color == user_bet:
                clear()  # Clear the screen.
                print(f"You've won! The {winning_color} turtle is the winner!")  # Print the win message.
            else:
                clear()  # Clear the screen.
                print(f"You've lost! The {winning_color} turtle is the winner!")  # Print the lose message.
        # Generate a random distance for the turtle to move.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)  # Move the turtle forward by the random distance.

# Wait for a mouse click on the screen to exit the program.
screen.exitonclick()
