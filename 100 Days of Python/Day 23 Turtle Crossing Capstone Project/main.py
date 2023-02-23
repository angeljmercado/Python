import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
CAR_PACER = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    CAR_PACER += 1
    time.sleep(0.1)
    screen.update()
    car_manager.car_move()
    if player.ycor() > 280:
        player.back_to_start()
        car_manager.level_up()
        scoreboard.level_up()
    if CAR_PACER % 5 == 0:
        car_manager.create_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
