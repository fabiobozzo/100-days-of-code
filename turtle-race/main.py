from turtle import Turtle, Screen
import random


def position_turtle_y(turtle_index, turtles_count, spacing):
    return (-spacing * turtle_index) + ((spacing / 2) * (turtles_count - 1))


screen = Screen()
screen.setup(500, 400)
screen.bgpic("turtles_bg.png")

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(len(colors)):
    t = Turtle()
    t.shape("turtle")
    t.penup()
    t.color(colors[i])
    t.goto(-230, position_turtle_y(i, len(colors), 68))
    turtles.append(t)
    print(t.width())

is_race_on = False
if user_bet in colors:
    is_race_on = True
else:
    print("Invalid bet. Please try again")
    screen.bye()
    exit(0)

while is_race_on:
    for t in turtles:
        if t.xcor() > screen.window_width()/2 - 40:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                outcome = "YOU WON!"
            else:
                outcome = "You lost..."
            print(f"{outcome} The winning turtle is: {winning_color}.")

        random_distance = random.randint(0, 10)
        t.forward(random_distance)

screen.exitonclick()
