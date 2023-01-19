from tkinter import *
from tkinter import messagebox

import json
import pyperclip
import password_generator


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def suggest_password():
    generated_password = password_generator.generate_password()
    password_input.delete(0, END)
    password_input.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Ooops", message="Please make sure you haven't left any fields empty!")
    else:
        if messagebox.askokcancel(title=website, message=f"Is it ok to save the password for {username} @ {website}?"):
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()

        messagebox.showinfo(title="Thank you", message="Your password has been saved.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass Password Manager")
window.config(padx=50, pady=50, bg="white")

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
username_label = Label(text="Email / Username:", bg="white")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

website_input = Entry(width=35, highlightbackground="white")
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_input = Entry(width=35, highlightbackground="white")
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "fabio.bozzo@gmail.com")

password_input = Entry(width=20, highlightbackground="white")
password_input.grid(row=3, column=1)
new_password_button = Button(text="Generate Password", highlightbackground="white", width=11, command=suggest_password)
new_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=33, highlightbackground="white", command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
