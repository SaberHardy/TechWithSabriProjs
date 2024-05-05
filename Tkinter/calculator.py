from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('500x500')


def click_button(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def add_two_numbers():
    received_number = entry.get()
    global first_number
    global status
    status = 'addition'
    first_number = int(received_number)
    clear_input()


def sub_two_numbers():
    received_number = entry.get()
    global first_number
    global status
    status = 'sub'
    first_number = int(received_number)
    clear_input()


def divi_two_numbers():
    received_number = entry.get()
    global first_number
    global status
    status = 'divide'

    first_number = int(received_number)
    clear_input()


def multi_two_numbers():
    received_number = entry.get()
    global first_number
    global status
    status = 'multi'

    first_number = int(received_number)
    clear_input()


def clear_input():
    entry.delete(0, END)


def show_results():
    second_number = entry.get()
    entry.delete(0, END)
    result = 0

    if status == 'addition':
        result = first_number + int(second_number)
    elif status == 'sub':
        result = first_number - int(second_number)
    elif status == 'multi':
        result = first_number * int(second_number)
    elif status == 'divide':
        result = first_number / int(second_number)

    entry.insert(0, str(result))


entry = Entry(root, width=45, borderwidth=3)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click_button(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click_button(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click_button(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click_button(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click_button(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click_button(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click_button(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click_button(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click_button(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click_button(9))

button_multi = Button(root, text="*", padx=40, pady=20, command=multi_two_numbers)
button_multi.grid(row=1, column=3)

button_division = Button(root, text="/", padx=40, pady=20, command=divi_two_numbers)
button_division.grid(row=2, column=3)

button_plus = Button(root, text="+", padx=40, pady=20, command=add_two_numbers)
button_plus.grid(row=3, column=3)

button_ac = Button(root, text="AC", padx=40, pady=20, command=clear_input)
button_ac.grid(row=4, column=0)

button_sub = Button(root, text="-", padx=40, pady=20, command=sub_two_numbers)
button_sub.grid(row=4, column=3)

button_equal = Button(root, text="=", padx=40, pady=20, command=show_results)
button_equal.grid(row=4, column=2)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=1)

root.mainloop()
