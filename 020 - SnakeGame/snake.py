from turtle import Turtle

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
moving_distance = 20
directions = {"up": 90, "down": 270, "left": 180, "right": 0}


class Snake:
    def __init__(self):
        self.turtles = []
        self.create()
        self.head = self.turtles[0]

    def create(self):
        for pos in starting_pos:
            self.add_turtle(pos)

    def add_turtle(self, pos):
        turtle = Turtle(shape="square")
        turtle.color("yellow")
        turtle.penup()
        turtle.goto(pos)
        self.turtles.append(turtle)

    def extend(self):
        self.add_turtle(self.turtles[-1].position())

    def reset_pos(self):
        for turtle in self.turtles:
            turtle.goto(1000, 1000)
        self.turtles.clear()
        self.create()
        self.head = self.turtles[0]

    def move(self):
        for turtle_i in range(len(self.turtles) - 1, 0, -1):
            new_x_pos = self.turtles[turtle_i - 1].xcor()
            new_y_pos = self.turtles[turtle_i - 1].ycor()
            self.turtles[turtle_i].goto(new_x_pos, new_y_pos)
        self.head.forward(moving_distance)

    def up(self):
        if self.head.heading() != directions["down"]:
            self.head.setheading(directions["up"])

    def down(self):
        if self.head.heading() != directions["up"]:
            self.head.setheading(directions["down"])

    def left(self):
        if self.head.heading() != directions["right"]:
            self.head.setheading(directions["left"])

    def right(self):
        if self.head.heading() != directions["left"]:
            self.head.setheading(directions["right"])
