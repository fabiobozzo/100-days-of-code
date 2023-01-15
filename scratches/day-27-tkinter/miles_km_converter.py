import tkinter


def calculate_km():
    error_label.config(text="")
    val = miles_entry.get()
    if not val.isdigit():
        error_label.config(text="Error")
        miles_entry.delete(0, tkinter.END)
        miles_entry.insert(0, "0")
    else:
        result = round(int(val) * 1.609)
        km_entry.delete(0, tkinter.END)
        km_entry.insert(0, str(result))


def calculate_miles():
    error_label.config(text="")
    val = km_entry.get()
    if not val.isdigit():
        error_label.config(text="Error")
        km_entry.delete(0, tkinter.END)
        km_entry.insert(0, "0")
    else:
        result = round(int(val) / 1.609)
        miles_entry.delete(0, tkinter.END)
        miles_entry.insert(0, str(result))


window = tkinter.Tk()

window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

to_miles_button = tkinter.Button(text="to Miles", command=calculate_miles)
to_miles_button.grid(row=0, column=0)

miles_entry = tkinter.Entry(width=10)
miles_entry.insert(0, string="0")
miles_entry.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)

to_km_button = tkinter.Button(text="to Km", command=calculate_km)
to_km_button.grid(row=1, column=0)

km_entry = tkinter.Entry(width=10)
km_entry.grid(row=1, column=1)
km_entry.insert(0, string="0")

km_label = tkinter.Label(text="Kilometers")
km_label.grid(row=1, column=2)
km_label.config(padx=10, pady=10)

error_label = tkinter.Label(text="")
error_label.grid(row=2, column=1)

window.mainloop()
