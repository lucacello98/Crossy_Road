from turtle import Turtle

# Constants for font and alignment settings
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.level = 1  # Starting level
        self.penup()  # Prevent the turtle from drawing lines
        self.hideturtle()  # Hide the turtle icon, we only want to display the text
        self.goto(0, 260)  # Position the scoreboard at the top of the screen
        self.update_score()  # Display the initial score (Level 1)

    def update_score(self):
        # Update the displayed score (level)
        self.clear()  # Clear previous score display
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)  # Display current level

    def increase_level(self):
        # Increase the level and update the score display
        self.level += 1
        self.update_score()  # Update the score after the level increase

    def game_over(self):
        # Display "GAME OVER" message at the center of the screen
        self.goto(0, 0)  # Position the text at the center of the screen
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  # Display game over message
