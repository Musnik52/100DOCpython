from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong_game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

playing = True
while playing:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50) and (
        ball.xcor() > 320 or ball.xcor() < -320
    ):
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()

screen.exitonclick()
