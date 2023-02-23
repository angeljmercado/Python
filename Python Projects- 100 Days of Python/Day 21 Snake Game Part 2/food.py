from turtle import Turtle
from snake import Snake
import random


class Food(Turtle, Snake):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color(self.colorize())
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(self.colorize())
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)
        
