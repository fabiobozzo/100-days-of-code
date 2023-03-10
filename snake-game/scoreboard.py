from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = 0
        with open("data.txt") as file:
            file_content = file.read()
            self.high_score = int(file_content.replace("\n", "").strip())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 260)
        self.update_scoreboard()

    def score_point(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
