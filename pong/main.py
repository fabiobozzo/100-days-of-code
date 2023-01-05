import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(key="Up", fun=r_paddle.go_up)
    screen.onkey(key="Down", fun=r_paddle.go_down)
    screen.onkey(key="w", fun=l_paddle.go_up)
    screen.onkey(key="s", fun=l_paddle.go_down)

    is_game_on = True
    while is_game_on:
        time.sleep(0.03)
        screen.update()
        ball.move()

        # Detect collision with the wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with the paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 325:
            ball.setx(325)
            ball.bounce_x()
        if ball.distance(l_paddle) < 50 and ball.xcor() < -325:
            ball.setx(-325)
            ball.bounce_x()

        # Detect R paddle misses
        if ball.xcor() > 380:
            scoreboard.l_point()
            ball.color("red")
            screen.update()
            ball.reset_position()
            ball.color("white")

        # Detect L paddle misses
        if ball.xcor() < -380:
            scoreboard.r_point()
            ball.color("red")
            screen.update()
            ball.reset_position()
            ball.color("white")

    screen.exitonclick()
