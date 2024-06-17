from tkinter import *
from tkinter import colorchooser, messagebox


def show_items_selected(event):
    selected_indices = listbox.curselection()
    # print(f"Selected Indices: {days[selected_indices[0]]}")
    selected_item = ", ".join([listbox.get(i) for i in selected_indices])
    messagebox.showinfo("Selected Item,", f"You have Selected: {selected_item}")


root = Tk()
root.title("Save Settings")
root.geometry('500x500')

frame = Frame(root)
frame.pack()

listbox = Listbox(frame, selectmode=MULTIPLE)
listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(frame, orient=VERTICAL, command=listbox.yview)
scrollbar.pack(pady=20)

listbox.config(yscrollcommand=scrollbar.set)

days = ["Saturday", "Sunday", "Monday",
        "Tuesday", "Wednesday", "Thursday", "Friday",
        "Tuesday", "Wednesday", "Thursday", "Friday",
        "Tuesday", "Wednesday", "Thursday", "Friday",
        "Tuesday", "Wednesday", "Thursday", "Friday",
        "Tuesday", "Wednesday", "Thursday", "Friday",
        "Tuesday", "Wednesday", "Thursday", "LAST",
        ]

for day in days:
    listbox.insert(0, day)

listbox.bind('<<ListboxSelect>>', show_items_selected)

root.mainloop()
