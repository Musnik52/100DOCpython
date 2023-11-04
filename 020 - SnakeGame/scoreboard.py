from turtle import Turtle

alignemt = "center"
font = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=alignemt, font=font)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=alignemt, font=font)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
