import tkinter


def calculate():
    val = entry.get()
    if not val.isdigit():
        result_label.config(text="Error")
        entry.delete(0, tkinter.END)
        entry.insert(0, "0")
    else:
        result = round(int(val) * 1.6, 2)
        result_label.config(text=str(result))


window = tkinter.Tk()

window.title("Miles to Km Converter")
window.minsize(width=400, height=250)
window.config(padx=50, pady=50)

entry = tkinter.Entry(width=10)
entry.insert(0, string="0")
entry.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)

equalto_label = tkinter.Label(text="is equal to")
equalto_label.grid(row=1, column=0)
equalto_label.config(padx=10, pady=10)

result_label = tkinter.Label(text="0", font=("Arial", 18, "bold"))
result_label.grid(row=1, column=1)
result_label.config(padx=10, pady=10)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)
km_label.config(padx=10, pady=10)

calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()
