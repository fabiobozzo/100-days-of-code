import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()

    screen.listen()
    screen.onkey(key="space", fun=player.move)

    game_is_on = True
    while game_is_on:
        car_manager.move_cars()
        car_manager.recycle_cars()

        # Check if a car collided with player
        for car in car_manager.cars:
            if player.distance(car) < 35 and car.ycor() + 20 >= player.ycor() >= car.ycor() - 25:
                scoreboard.game_over()
                game_is_on = False

        # Check if player has reached the next level
        if player.ycor() > 300:
            player.next_level()
            scoreboard.next_level()
            car_manager.next_level()

        time.sleep(0.1)
        screen.update()

    screen.exitonclick()
