import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            rand_y = random.randint(-250, 280)
            car.goto(300, rand_y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def raise_speed(self):
        self.car_speed += MOVE_INCREMENT
