from tkinter import *

root = Tk()
root.title("Save Settings")
root.geometry('500x500')
root.configure(background="#8fa3c2")


def button_clicked(event):
    # my_label = Label(root, text="You clicked me" + str(event.x) + "  " + str(event.y))
    my_label = Label(root, text="You clicked me: " + event.char)
    print("You clicked me" + str(event.x) + "  " + str(event.y))
    my_label.pack(pady=5)

# Enter, Leave, FocusIn, FocusOut, Return, Key
click_btn = Button(root, text="Click Me!")
root.bind('<Enter>', button_clicked)
click_btn.pack(pady=20)

root.mainloop()
