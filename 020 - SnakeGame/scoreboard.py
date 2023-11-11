from turtle import Turtle

alignemt = "center"
font = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("020 - SnakeGame\data.txt", "r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} | High Score: {self.high_score}",
            align=alignemt,
            font=font,
        )

    def restart(self):
        self.high_score = (
            self.score if self.score > self.high_score else self.high_score
        )
        with open("020 - SnakeGame\data.txt", "w") as file:
            file.write(f'{self.high_score}')
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align=alignemt, font=font)

    def increase_score(self):
        self.score += 1
        self.update_score()
