import tkinter

# empty window
window = tkinter.Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))

# show element in the window according to The Packer:
# https://docs.python.org/3/library/tkinter.html#the-packer

# Either use pack(), place() or grid() to show a widget

# my_label.pack()
# my_label.pack(side="left")
# my_label.pack(expand=True)
# why are those arguments not in the docs? -> see *args and **kwargs

# my_label["text"] = "New Text"
my_label.config(text="New text")
my_label.config(padx=50, pady=50)

# my_label.place(x=0, y=0)
# my_label.place(x=100, y=200)

my_label.grid(column=0, row=0)

def button_clicked():
    my_label["text"] = input_entry.get()


button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(row=1, column=1)

input_entry = tkinter.Entry(width=10)
input_entry.insert(tkinter.END, string="asd")
# input_entry.pack()
input_entry.grid(row=2, column=3)

# Challenge
button = tkinter.Button(text="New Button")
button.grid(row=0, column=2)

# always the last line
window.mainloop()
