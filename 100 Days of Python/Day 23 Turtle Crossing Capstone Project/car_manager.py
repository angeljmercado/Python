from turtle import Turtle
from scoreboard import Scoreboard
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.level = 5

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.setheading(180)
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(320, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.level)

    def level_up(self):
        self.level += MOVE_INCREMENT




