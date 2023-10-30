from turtle import Turtle, Screen
import random

race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
pos_y = [-70, -40, -10, 20, 50, 80]
turtles = []

for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=pos_y[i])
    turtles.append(turtle)

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(
    title="Place Your Bet!", prompt="Who will win? Choose a color: "
).lower()
while bet not in colors:
    bet = screen.textinput(
        title="Place Your Bet!", prompt="Choose a NORMAL color: "
    ).lower()
if bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            outcome = "won!" if winner == bet else "lost..."
            print(f"{winner} turtle won the race! you {outcome}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
