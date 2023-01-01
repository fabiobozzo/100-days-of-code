import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake, UP, DOWN, LEFT, RIGHT


def run():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(key="Up", fun=snake.set_heading(UP))
    screen.onkey(key="Down", fun=snake.set_heading(DOWN))
    screen.onkey(key="Left", fun=snake.set_heading(LEFT))
    screen.onkey(key="Right", fun=snake.set_heading(RIGHT))

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        # Compute new positions of snake's segments
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.score()
            snake.grow()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()


if __name__ == '__main__':
    run()
