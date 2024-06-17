from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Save Settings")
root.geometry('500x500')


def color_picker_fun():
    color_picker = colorchooser.askcolor()[1]
    print(color_picker)
    color_label = Label(root, text=color_picker)
    color_label.pack(pady=10)

    label_color = Label(root, text="Color chosen", font=20, bg=color_picker)
    label_color.pack()

def bg_changer():
    color_picker = colorchooser.askcolor()[1]
    root.configure(background=color_picker)


btn_choose_color = Button(root, text="Pick a color", command=color_picker_fun)
btn_choose_color.pack()

background_btn = Button(root, text="Change background Color", command=bg_changer).pack()

root.mainloop()
