from turtle import Turtle

FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.level = 1
        self.scoreboard_update()

    def scoreboard_update(self):
        self.write(arg=f"Level: {self.level}", move=False, font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.scoreboard_update()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over.", align="center", font=FONT)
