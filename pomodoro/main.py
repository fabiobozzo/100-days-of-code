import math
import threading

from playsound import playsound
from tkinter import *


def ring_bell():
    threading.Thread(target=playsound, args=('ring.wav',), daemon=True).start()


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    tick_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN  # * 60
    short_break_sec = SHORT_BREAK_MIN  # * 60
    long_break_sec = LONG_BREAK_MIN  # * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long break 😴", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short break ☕️", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work 🤓", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    global timer

    if seconds == 0:
        ring_bell()

    minutes_part = math.floor(seconds / 60)
    seconds_part = seconds % 60

    # DYNAMIC TYPING EXPLAINED
    if seconds_part < 10:
        seconds_part = f"0{seconds_part}"
    if minutes_part < 10:
        minutes_part = f"0{minutes_part}"
    # --------------------------

    canvas.itemconfig(timer_text, text=f"{minutes_part}:{seconds_part}")

    if seconds > 0:
        timer = window.after(1000, count_down, seconds - 1)
    else:
        start_timer()
        ticks = ""
        for _ in range(math.floor(reps / 2)):
            ticks += "✓"
        tick_label.config(text=ticks)


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

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

tick_label = Label(bg=YELLOW, fg=GREEN, justify=CENTER, font=(FONT_NAME, 24))
tick_label.grid(row=3, column=1)

window.mainloop()
