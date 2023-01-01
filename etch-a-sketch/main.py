from turtle import Turtle, Screen
from event_handlers import *

STEP_MOVE = 10
STEP_ROTATION = 10

t = Turtle()

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move(t, STEP_MOVE, "forward"))
screen.onkey(key="s", fun=move(t, STEP_MOVE, "backward"))
screen.onkey(key="a", fun=rotate(t, STEP_ROTATION, "left"))
screen.onkey(key="d", fun=rotate(t, STEP_ROTATION, "right"))
screen.onkey(key="c", fun=t.reset)
screen.exitonclick()
