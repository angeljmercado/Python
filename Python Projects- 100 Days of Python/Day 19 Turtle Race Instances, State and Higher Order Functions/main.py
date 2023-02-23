from turtle import Turtle, Screen
import random


red = Turtle(shape="turtle")
orange = Turtle(shape="turtle")
yellow = Turtle(shape="turtle")
green = Turtle(shape="turtle")
blue = Turtle(shape="turtle")
purple = Turtle(shape="turtle")
turtles = [red, orange, yellow, green, blue, purple]
# def move_forward():
#     kim.forward(30)
# def move_backwards():
#     kim.back(30)
# def counter_clockwise():
#     kim.left(10)
# def clockwise():
#     kim.right(10)
# def clear_drawing():
#     kim.clear()
#     kim.up()
#     kim.setpos(0, 0)
#     kim.down()


y = -70
order = 0

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
for turtle in turtles:
    turtle.up()
    turtle.color(colors[order])
    turtle.goto(-230, y)
    order += 1
    y += 30
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True
# screen.listen()
# screen.onkey(key="W".lower(), fun=move_forward)
# screen.onkey(move_backwards, "S".lower())
# screen.onkey(key="A".lower(), fun=counter_clockwise)
# screen.onkey(key="D".lower(), fun=clockwise)
# screen.onkey(key="C".lower(), fun=clear_drawing)
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 210:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win! the Winner is the {turtle.pencolor()} turtle")
                is_race_on = False
            else:
                print(f"You lose :( The Winner is the {turtle.pencolor()} turtle")
                is_race_on = False
        random_steps = random.randint(10, 30)
        turtle.forward(random_steps)
screen.exitonclick()
