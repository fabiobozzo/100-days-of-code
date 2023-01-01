import math
import random
import colorgram
import turtle

turtle.colormode(255)

grid_size = 10
dot_size = 20

RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270

def is_light_color(rgb_tuple):
    r = rgb_tuple[0]
    g = rgb_tuple[1]
    b = rgb_tuple[2]
    hsp = math.sqrt(0.299 * (r * r) + 0.587 * (g * g) + 0.114 * (b * b))
    if hsp > 230:
        return True
    return False


def generate_color_list():
    colors = colorgram.extract('image.jpg', 16)
    color_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_tuple = (r, g, b)
        if not is_light_color(rgb_tuple):
            color_list.append(rgb_tuple)
    return color_list


def move_top_left(t):
    t.setheading(LEFT)
    t.penup()
    t.forward(dot_size * grid_size)
    t.setheading(UP)
    t.forward(dot_size * grid_size)
    t.pendown()
    t.setheading(RIGHT)


def move_to_next_row(t, x):
    t.penup()
    t.setx(x)
    t.setheading(DOWN)
    t.forward(dot_size * 2)
    t.setheading(RIGHT)
    t.pendown()


hirst = turtle.Turtle()
hirst.hideturtle()
hirst.speed(0)

move_top_left(hirst)
rgb_colors = generate_color_list()

initial_x = hirst.xcor()
initial_y = hirst.ycor()

for _ in range(grid_size):
    for _ in range(grid_size):
        hirst.dot(dot_size, random.choice(rgb_colors))
        hirst.penup()
        hirst.forward(dot_size * 2)
        hirst.pendown()

    move_to_next_row(hirst, initial_x)

screen = turtle.Screen()
screen.exitonclick()
