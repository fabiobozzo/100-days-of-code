import turtle
import pandas

screen = turtle.Screen()
# screen.setup(width=725, height=491)
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states = pandas.read_csv("50_states.csv")
guessed_states = []

city_names_writer = turtle.Turtle()
city_names_writer.hideturtle()
city_names_writer.penup()
city_names_writer.color("black")

while len(guessed_states) < len(all_states):
    title = f"{len(guessed_states)}/{len(all_states)} Guess the State"
    answer = screen.textinput(title, "What's an american state name?").title()

    if answer == "Exit":
        missing_states = [state for state in all_states["state"] if state not in guessed_states]
        new_date = pandas.DataFrame(missing_states)
        new_date.to_csv("states_to_learn.csv")
        break

    found_state = all_states[all_states.state == answer]
    if not found_state.empty:
        guessed_states.append(answer)
        city_names_writer.goto(int(found_state.x), int(found_state.y))
        city_names_writer.write(found_state.state.item(), align="center", font=("Times New Roman", 11, "bold"))


