import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("crossing_game")
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
cars = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

playing = True
while playing:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    if player.reached_finish_line():
        player.reset_pos()
        cars.raise_speed()
        scoreboard.level_up()

    for car in cars.cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            playing = False


screen.exitonclick()
