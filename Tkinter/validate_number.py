from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('500x500')


def validate_number(input):
    if input.isdigit() or input == '':
        return True
    else:
        return False


def submit_number():
    print(f"The entry number got: {entry.get()}")


validate_command = (root.register(validate_number), '%P')

entry = Entry(root, validate='key', validatecommand=validate_command)
entry.pack()

submit_btn = Button(root, text="Submit number", command=submit_number)
submit_btn.pack()

root.mainloop()
