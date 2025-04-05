from turtle import Turtle
import random

# Constants for car colors and movement speed
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5  # Initial speed of cars
MOVE_INCREMENT = 5  # Speed increase per level

class CarManager:
    def __init__(self):
        self.all_cars = []           # List to store all car objects
        self.speed = STARTING_MOVE_DISTANCE  # Initial speed of cars

    def create_car(self):
        # Only create a new car occasionally (approx 1 in 6 loops)
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")  # Use a stretched square shape as the car
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Makes it car-like: 20px high, 40px wide
            new_car.penup()  # Prevent drawing lines
            new_car.color(random.choice(COLORS))  # Random car color
            random_y = random.randint(-250, 250)  # Random vertical position
            new_car.goto(300, random_y)  # Start at the right edge of the screen
            self.all_cars.append(new_car)  # Add car to the list

    def move_cars(self):
        # Move each car to the left by the current speed
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        # Increase speed for the next level
        self.speed += MOVE_INCREMENT

