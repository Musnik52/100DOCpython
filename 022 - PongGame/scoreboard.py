from turtle import Turtle

alignemt = "center"
font = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=alignemt, font=font)
        self.goto(100, 200)
        self.write(self.r_score, align=alignemt, font=font)

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_score()
