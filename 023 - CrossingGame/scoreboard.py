from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(-260, 260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align='center', font=FONT)
