from tkinter import *

root = Tk()
root.title("Radio Button")
root.geometry('500x500')

tk_var = IntVar()


def get_radio_value():
    selected_value = tk_var.get()
    label.config(text="You have selected: " + str(selected_value))


tk_var.set(2)

radio_button1 = Radiobutton(root, text='Option 1', value=1, variable=tk_var)  # , command=get_radio_value)
radio_button1.pack()

radio_button2 = Radiobutton(root, text='Option 2', value=2, variable=tk_var)  # , command=get_radio_value)
radio_button2.pack()

radio_button3 = Radiobutton(root, text='Option 3', value=3, variable=tk_var)  # , command=get_radio_value)
radio_button3.pack()

my_btn = Button(root, text="Get selected Value", command=get_radio_value, pady=20)
my_btn.pack()

label = Label(root, text='')
label.pack()

root.mainloop()
