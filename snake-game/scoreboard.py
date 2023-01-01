from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_points = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 260)
        self.refresh()

    def score(self):
        self.score_points += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score_points}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
