import time
from turtle import Screen

from player import Player

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()

    screen.listen()
    screen.onkey(key="space", fun=player.move)

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

    screen.exitonclick()
