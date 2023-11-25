from turtle import Screen
from day_20_snake import Snake
import time

# Create a new screen object for the game window.
screen = Screen()
# Set the dimensions of the game window.
screen.setup(width=600, height=600)
# Set the background color of the game window.
screen.bgcolor("black")
# Set the title of the game window.
screen.title("My Snake Game")
# Turn off animation to update the screen manually.
screen.tracer(0)

# Create a new Snake object.
snake = Snake()

# Start listening to keyboard input.
screen.listen()
# Bind the up arrow key to the snake's up method.
screen.onkey(snake.up, "Up")
# Bind the down arrow key to the snake's down method.
screen.onkey(snake.down, "Down")
# Bind the left arrow key to the snake's left method.
screen.onkey(snake.left, "Left")
# Bind the right arrow key to the snake's right method.
screen.onkey(snake.right, "Right")

# Flag to control the game loop.
game_is_on = True
# Game loop to keep the game running.
while game_is_on:
    # Update the screen with the current state of the game window.
    screen.update()
    # Pause the loop for a short period (0.1 seconds) to control the speed of the snake.
    time.sleep(0.1)

    # Call the move method of the Snake object to move the snake forward.
    snake.move()

# Set the screen to close when it is clicked.
screen.exitonclick()