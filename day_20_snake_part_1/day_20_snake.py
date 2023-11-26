# Import Turtle class from turtle module.
from turtle import Turtle

# Constants for the starting positions of the snake segments and movement distance.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# Constants representing cardinal directions in degrees.
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Define a Snake class.
class Snake:
    # Constructor of the class.
    def __init__(self):
        self.segments = []  # List to store segments of the snake.
        self.create_snake()  # Call the create_snake method to create the snake.
        self.head = self.segments[0]  # Set the first segment as the head of the snake.

    # Method to create a snake.
    def create_snake(self):
        for position in STARTING_POSITIONS:  # Loop through the starting positions.
            new_segment = Turtle("square")  # Create a turtle object with a square shape.
            new_segment.color("white")  # Set the color of the segment.
            new_segment.penup()  # Lift the pen to avoid drawing lines.
            new_segment.goto(position)  # Move the segment to its starting position.
            self.segments.append(new_segment)  # Add the segment to the list of segments.

    # Method to move the snake forward.
    def move(self):
        # Move each segment to the position of the next segment.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the next segment.
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the next segment.
            self.segments[seg_num].goto(new_x, new_y)  # Set the new position of the segment.
        self.head.forward(MOVE_DISTANCE)  # Move the head forward.

    # Methods to change the direction of the snake.
    def up(self):
        if self.head.heading() != DOWN:  # Prevent the snake from reversing.
            self.head.setheading(UP)  # Set the head's direction to UP.

    def down(self):
        if self.head.heading() != UP:  # Prevent the snake from reversing.
            self.head.setheading(DOWN)  # Set the head's direction to DOWN.

    def left(self):
        if self.head.heading() != RIGHT:  # Prevent the snake from reversing.
            self.head.setheading(LEFT)  # Set the head's direction to LEFT.

    def right(self):
        if self.head.heading() != LEFT:  # Prevent the snake from reversing.
            self.head.setheading(RIGHT)  # Set the head's direction to RIGHT.
