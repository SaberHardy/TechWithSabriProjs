from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('500x500')


def clear_text_area():
    my_text.delete(1.0, END)


def get_content():
    mylabel.config(text=my_text.get(1.0, END))


my_text = Text(root, width=40, height=10, font=("", 20))
my_text.pack(pady=20)

my_frame = Frame(root)
my_frame.pack()

clear_button = Button(my_frame, text="Clear", command=clear_text_area)
clear_button.grid(row=0, column=0)

get_button = Button(my_frame, text="Get Content", command=get_content)
get_button.grid(row=1, column=0)

mylabel = Label(root, text="")
mylabel.pack()

root.mainloop()
