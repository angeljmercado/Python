# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
from turtle import Turtle, Screen, colormode
import turtle as k
colormode(255)
k.speed("fastest")
k.shape("classic")
k.up()
k.hideturtle()

x_axis = -420
y_axis = -370
k.setpos(x_axis, y_axis)


def color():
    """Chooses a random color from a list using rgb"""
    color_list = [(235, 229, 218), (221, 161, 80), (47, 102, 144), (118, 165, 192), (152, 65, 89), (215, 231, 220), (32, 133, 94), (189, 162, 32), (163, 80, 51), (197, 134, 155), (213, 88, 61), (199, 85, 114), (235, 216, 223), (125, 180, 156), (208, 224, 232), (232, 199, 111), (147, 30, 39), (58, 164, 134), (8, 105, 83), (43, 161, 184), (28, 62, 115), (120, 113, 160), (236, 162, 180), (131, 35, 31), (27, 56, 81), (153, 212, 200), (20, 64, 55), (235, 170, 159), (65, 44, 40), (148, 209, 217)]
    selected_color = random.choice(color_list)
    return selected_color


def paint_row():
    """Paint a row of Different Colors"""
    for _ in range(12):
        k.color(color())
        k.begin_fill()
        k.circle(20)
        k.end_fill()
        k.forward(75)


def next_row(y_axis):
    pass


for row in range(8):
    color()
    paint_row()
    y_axis += 100
    k.setpos(x_axis, y_axis)











screen = Screen()
screen.exitonclick()
