from tkinter import *
from tkinter import ttk


def hide_frame():
    notebook.hide(1)


def display_frame():
    notebook.add(frame2)


root = Tk()
root.title("Save Settings")
root.geometry('500x500')

notebook = ttk.Notebook(root)
notebook.pack()

frame = Frame(notebook, width=500, height=500, bg='red')
frame.pack(fill='both', expand=1)

frame2 = Frame(notebook, width=500, height=500, bg='blue')
frame2.pack(fill='both', expand=1)

notebook.add(frame, text="This is the red frame")
notebook.add(frame2, text="This is the blue frame")

Button(frame, text="Hide tab 2", command=hide_frame).pack()
Button(frame, text="display tab 2", command=display_frame).pack()

root.mainloop()
