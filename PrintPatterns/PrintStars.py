from tkinter import *

root = Tk()

my_label = Label(root, text="First label")
my_label2 = Label(root, text="Second Label")
my_label3 = Label(root, text="                 ")
my_label.grid(row=0, column=0)
my_label2.grid(row=1, column=5)
my_label3.grid(row=1, column=1)

root.mainloop()
print("this is just a test to follow up the commits")