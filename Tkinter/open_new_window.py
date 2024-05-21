from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Main Window")
root.geometry('500x500')


def open_second_window():
    top = Toplevel()
    top.title("Second Window")
    top.geometry('300x200')

    close_btn = Button(top, text="Close Window", command=top.destroy)
    close_btn.pack()


btn_second_window = Button(root, text="Open Second Window", command=open_second_window)
btn_second_window.pack()

root.mainloop()
