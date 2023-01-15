import math
import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(seconds):
    minutes_part = math.floor(seconds / 60)
    seconds_part = seconds % 60

    # DYNAMIC TYPING EXPLAINED
    if seconds_part < 10:
        seconds_part = f"0{seconds_part}"
    if minutes_part < 10:
        minutes_part = f"0{minutes_part}"

    canvas.itemconfig(timer_text, text=f"{minutes_part}:{seconds_part}")
    if seconds > 0:
        window.after(1000, count_down, seconds - 1)
    # --------------------------


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, justify=CENTER, font=(FONT_NAME, 40))
title_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

tick_label = Label(text="✓", bg=YELLOW, fg=GREEN, justify=CENTER, font=(FONT_NAME, 24))
tick_label.grid(row=3, column=1)

window.mainloop()
