# from time import sleep
# from turtle import Turtle, Screen
#
# timmy = Turtle()  # We create an object (instance) from a class (blueprint).
# print(timmy)
#
# timmy.shape("turtle")
# timmy.color("green")
#
# for i in range(0, 100):
#     timmy.forward(1)
#     sleep(0.01)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
table.padding_width = 3
table.vertical_char = "I"

print(table)
