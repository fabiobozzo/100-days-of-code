from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.is_game_over = False
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-280, 260)
        if not self.is_game_over:
            self.write(f"Level {self.level}", font=FONT)
        else:
            self.write(f"Game Over! You reached level {self.level}", font=FONT)

    def next_level(self):
        self.level += 1
        self.refresh()

    def game_over(self):
        self.is_game_over = True
        self.refresh()
