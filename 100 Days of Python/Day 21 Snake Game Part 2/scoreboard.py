from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Calibri", 20, "normal"))

    def score_up(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=("Calibri", 20, "normal"))



