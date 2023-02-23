from turtle import Turtle, Screen, colormode
import tkinter
import random


kim = Turtle()
# kim.shape("turtle")
kim.color("red")
kim.pensize(2)
colormode(255)
kim.up()
kim.setpos(0, 0)
kim.down()


# # for number in range(3, 15):

#     counter = 0
#     while counter != number:
#         kim.forward(100)
#         kim.right(360 / number)
#         counter += 1


def random_color():
    """Assigns a Random color everything the loop starts over"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple = (r, g, b)
    return tuple


kim.speed("fastest")


starting = 0


for _ in range(0, 360, 7):
    kim.pencolor(random_color())
    kim.setheading(_)
    kim.circle(100, 360)
    # starting += _










screen = Screen()
screen.exitonclick()






