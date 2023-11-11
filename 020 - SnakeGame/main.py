from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("snake_game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

playing = True


def end_game():
    scoreboard.game_over()
    return False


while playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        scoreboard.increase_score()

    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.restart()
        snake.reset_pos()

    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            scoreboard.restart()
            snake.reset_pos()


screen.exitonclick()
