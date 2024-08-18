from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('500x500')


def select_name():
    my_label.config(text=spin_box.get())


# spin_box = Spinbox(root, from_=0, to=10, font=("", 30))
# spin_box.pack()

list_name = ("Med", "Ibrahim", "Saber", "Mahdi", "Tina", "Samir")
spin_box = Spinbox(root, values=list_name, font=("", 30))
spin_box.pack()

button_select = Button(root, text="Select Name", command=select_name)
button_select.pack()

my_label = Label(root, text="")
my_label.pack()

root.mainloop()
