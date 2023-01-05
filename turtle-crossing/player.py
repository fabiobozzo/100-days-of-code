from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(90)
        self.reset()

    def reset(self):
        self.color("green")
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
