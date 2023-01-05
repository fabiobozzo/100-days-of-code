import random
import time
from turtle import Turtle

STEP = 6
BASE_SPEED = 0.04


class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        self.x_move = STEP
        self.y_move = STEP
        self.move_speed = BASE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.x_move += 0.1 * random.randint(-STEP, STEP)
        if self.y_move < 0:
            self.y_move = STEP
        else:
            self.y_move = -STEP

    def bounce_x(self):
        self.move_speed *= 0.9
        self.y_move += 0.1 * random.randint(-STEP, STEP)
        if self.x_move < 0:
            self.x_move = STEP
        else:
            self.x_move = -STEP

    def reset_position(self):
        self.move_speed = BASE_SPEED
        time.sleep(1)
        self.goto(0, 0)
        self.bounce_x()
