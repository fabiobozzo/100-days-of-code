import turtle
import heroes as h
import random

polygons = [
    {"name": "triangle", "sides": 3, "color": "black"},
    {"name": "square", "sides": 4, "color": "red"},
    {"name": "pentagon", "sides": 5, "color": "orange"},
    {"name": "hexagon", "sides": 6, "color": "blue"},
    # {"name": "heptagon", "sides": 7, "color": "purple"},
    {"name": "octagon", "sides": 8, "color": "green"},
    {"name": "decagon", "sides": 10, "color": "cyan"}
]


def random_hex_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def reset_position(t):
    t.penup()
    t.setx(0)
    t.sety(0)
    t.setheading(0)
    t.pendown()


def square(t):
    for i in range(4):
        t.forward(100)
        t.left(90)


def dashed_line(t):
    for i in range(10):
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)


def draw_polygons(t):
    for p in polygons:
        reset_position(t)
        print(p["name"])
        t.color(p["color"])
        sides = p["sides"]
        for side in range(sides):
            angle = int(360 / sides)
            t.left(angle)
            t.forward(100)


def random_walk(t, steps):
    t.pensize(15)
    t.pendown()
    while steps > 0:
        t.color(random_hex_color())
        t.left(random.choice([0, 90, 180, 270]))
        t.forward(30)
        steps -= 1


def spirograph(t):
    for i in range(0, 360, 6):
        t.color(random_hex_color())
        # t.left(6)
        t.setheading(i)
        t.circle(100)


if __name__ == '__main__':
    print(f"Hi {h.gen()}")

    tim = turtle.Turtle()
    # tim.shape("turtle")
    # tim.color("red")

    # square(tim)
    # dashed_line(tim)
    # draw_polygons(tim)

    tim.speed(0)
    turtle.colormode(255)
    # random_walk(tim, 200)
    # spirograph(tim)

    screen = turtle.Screen()
    screen.exitonclick()
