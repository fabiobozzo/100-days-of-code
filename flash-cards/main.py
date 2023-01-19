import random
import pandas

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

# -------------------------- DATA -------------------------- #
data = pandas.read_csv("./data/dutch_words.csv")
words = data.to_dict(orient="records")

# ------------------------- EVENTS ------------------------- #
timer = None


def new_random_word():
    global timer
    if timer is not None:
        window.after_cancel(timer)
    random_word = random.choice(words)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(language_text, text="Dutch", fill="black")
    canvas.itemconfig(word_text, text=random_word["dutch"].capitalize(), fill="black")
    canvas.itemconfig(word_tip_text, text=random_word["dutch_phrase"], fill="black")
    timer = window.after(3000, flip_card, random_word)


def flip_card(word):
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word["english"].capitalize(), fill="white")
    canvas.itemconfig(word_tip_text, text=word["english_phrase"], fill="white")


# --------------------------- UI --------------------------- #
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
word_tip_text = canvas.create_text(400, 310, font=("Ariel", 14))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=new_random_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=new_random_word)
right_button.grid(row=1, column=1)

new_random_word()

window.mainloop()
