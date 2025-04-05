from turtle import Turtle

# Constants for starting position and how far the player moves each step
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.penup()  # Prevent the turtle from drawing lines
        self.shape("turtle")  # Use the turtle shape
        self.color("black")  # Set the turtle color
        self.goto(STARTING_POSITION)  # Start at the bottom center of the screen
        self.setheading(90)  # Point the turtle upward

    def move_up(self):
        # Move the player turtle upward by a set distance
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def next_level(self):
        # Reset the player to the starting position when a level is completed
        self.goto(STARTING_POSITION)
