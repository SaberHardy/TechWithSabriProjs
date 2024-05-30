from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Save Settings")
root.geometry('500x500')
root.configure(background="#8fa3c2")


def multi_selection(event):
    Label(root, text=drop_choices.get(), pady=10).pack()


def combobox_function(event):
    if combo_box.get() == "Friday":
        Label(root, text="Happy Friday").pack()
    else:
        Label(root, text="See you next Day!").pack()

days = [
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]

drop_choices = StringVar()
drop_choices.set(days[0])

dropdown = OptionMenu(root, drop_choices, *days, command=multi_selection)
dropdown.pack()

combo_box = ttk.Combobox(root, values=days)
combo_box.current(0)
combo_box.bind("<<ComboboxSelected>>", combobox_function)
combo_box.pack()

root.mainloop()
