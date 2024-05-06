from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.geometry('500x500')


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def show_message():
    answer = messagebox.askquestion("Test Message", "This is a test for message!")
    if answer == "yes":
        Label(root, text="You clicked yes").pack()
    else:
        Label(root, text="You clicked no").pack()


Button(root, text="Click for more!", command=show_message).pack()
root.mainloop()
