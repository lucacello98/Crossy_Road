import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)  # Window size
screen.tracer(0)  # Turn off automatic animation

# Create instances of the main game components
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up key listener for player movement
screen.listen()
screen.onkey(player.move_up, "Up")  # Move player up when "Up" arrow is pressed

game_is_on = True  # Game loop control

# Main game loop
while game_is_on:
    time.sleep(0.1)  # Delay for game speed
    screen.update()  # Update screen manually

    car_manager.create_car()  # Randomly generate new cars
    car_manager.move_cars()   # Move all cars on screen

    # Detect collision with any car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:  # If player is too close to a car
            game_is_on = False         # End the game
            scoreboard.game_over()     # Display game over message

    # Check if player reached the top of the screen
    if player.ycor() >= 280:
        player.next_level()           # Reset player to starting position
        car_manager.increase_speed()  # Increase car movement speed
        scoreboard.increase_level()   # Update the level display

# Close the window when clicked
screen.exitonclick()
