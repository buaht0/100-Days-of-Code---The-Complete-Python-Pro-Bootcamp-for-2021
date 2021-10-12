from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score = {self.score}', False, align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write('Game Over', False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()

