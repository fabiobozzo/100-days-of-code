import random
import time
from turtle import Turtle

SPEED = 6


class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        self.x_move = SPEED
        self.y_move = SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.x_move += 0.1 * random.randint(-SPEED, SPEED)
        if self.y_move < 0:
            self.y_move = SPEED
        else:
            self.y_move = -SPEED

    def bounce_x(self):
        self.y_move += 0.1 * random.randint(-SPEED, SPEED)
        if self.x_move < 0:
            self.x_move = SPEED
        else:
            self.x_move = -SPEED

    def reset_position(self):
        time.sleep(1)
        self.goto(0, 0)
        self.bounce_x()
