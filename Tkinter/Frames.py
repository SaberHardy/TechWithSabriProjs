from tkinter import *
from PIL import ImageTk, Image


def print_hello():
    print("hello this is me...!")


root = Tk()
root.title("Creating Frames")

frame = LabelFrame(root, text="This is my frame!", padx=100, pady=50)
frame.pack(pady=100)

mybtn = Button(frame, text="Click me", command=print_hello)
mybtn.grid(row=0, column=0)

root.mainloop()
