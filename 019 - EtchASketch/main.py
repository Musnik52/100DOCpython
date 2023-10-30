from turtle import Turtle, Screen

turtle = Turtle()
turtle.color("magenta")
turtle.shape('turtle')
turtle.speed("fastest")
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_left():
    # new_heading = turtle.heading() + 10
    # turtle.setheading(new_heading)
    turtle.left(10)


def turn_right():
    # new_heading = turtle.heading() - 10
    # turtle.setheading(new_heading)
    turtle.right(10)
    
def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
