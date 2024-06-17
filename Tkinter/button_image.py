from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Calculator")
root.geometry('500x500')
root.config(bg='red')


def print_hello():
    messagebox.showinfo("Information", "You have clicked the image button!")


save_image = Image.open('../static_files/save.jpeg')
save_btn = ImageTk.PhotoImage(save_image)

my_button = Button(root, image=save_btn, command=print_hello, borderwidth=0).pack()

root.mainloop()
