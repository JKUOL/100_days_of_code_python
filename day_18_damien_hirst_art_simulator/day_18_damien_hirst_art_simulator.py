# IImport modules
import turtle as t
import random

# Set the color mode to 255, which allows using RGB values.
t.colormode(255)

# Define a function to return a random RGB color.
def random_color():
    r = random.randint(0, 255)  # Random red component.
    g = random.randint(0, 255)  # Random green component.
    b = random.randint(0, 255)  # Random blue component.
    rgb = (r, g, b)  # Combine into a tuple representing an RGB color.
    return rgb  # Return the random color.

# Create a turtle object and set its speed to the fastest.
damien = t.Turtle()
damien.speed("fastest")
damien.hideturtle()  # Hide the turtle icon to only show the dots.

# Lift up the pen so no lines are drawn when the turtle moves.
damien.pu()
# Set the initial direction and move the turtle to starting position.
damien.setheading(225)
damien.forward(300)
damien.setheading(0)  # Set the direction back to the default (east).

# Define the size of the painting, the width of dots, and the space between them.
pic_length = 10
dot_width = 20
space = 50

# Create a loop to draw a grid of dots.
for element in range(pic_length):  # Loop over each row.
    for _ in range(pic_length):  # Loop over each column in the row.
        damien.color(random_color())  # Set the color to a random color.
        damien.dot(dot_width)  # Draw a dot with the specified size.
        damien.forward(space)  # Move forward to the next dot position.

    # After completing a row, reposition the turtle to start the next row.
    damien.setheading(90)  # Point north.
    damien.forward(space)  # Move to the next row.
    damien.setheading(180)  # Point west.
    damien.forward(space * pic_length)  # Move back to the start of the row.
    damien.setheading(0)  # Point east, ready for the next row.

# Create a screen object and wait for a click to exit.
screen = t.Screen()
screen.exitonclick()  # Close the window when clicked.
