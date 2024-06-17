from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar


def confirm_date():
    print(f"You have chose a date {calendar.get_date()}")
    date_selected = calendar.get_date()
    messagebox.showinfo("Selected Date", f"You have selected {date_selected}")


root = Tk()
root.title("Calculator")
root.geometry('500x500')

title_label = Label(root, text="Please, choose a date", font=("Helvetica", 20))
title_label.pack()

calendar = Calendar(root, selectmode="day", year=2024, month=5, day=20, date_pattern="mm-dd-yyyy",
                    background='lightblue', foreground='black', headersbackground='gray',
                    headersforground='white', weekendbackground='red', weekendforground='black')
calendar.pack()

confirm_date = Button(root, text="Confirm Date", command=confirm_date, pady=10)
confirm_date.pack()

root.mainloop()
