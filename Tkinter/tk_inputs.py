from tkinter import *

root = Tk()

entry = Entry(root,
              width=50,
              bg="white",
              fg="black"
              )
entry.insert(0, "Enter your name")
entry.pack()


def submit_results():
    welcome_lbl = "Hello: " + entry.get()
    label_text = Label(root, text=welcome_lbl)
    label_text.pack()


button = Button(root, text="Submit Results", command=submit_results)
button.pack()

root.mainloop()
