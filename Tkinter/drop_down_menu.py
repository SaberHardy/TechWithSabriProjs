from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Drop Down Menu")
root.geometry("500x400")


def show_results():
    Label(root, text=var_choose.get()).pack()


var_choose = StringVar()
list_days = ["Saturday",
             "Sunday",
             "Monday",
             "Tuesday",
             "Wednesday",
             "Thursday",
             "Friday"]

var_choose.set(list_days[0])

drop_down = OptionMenu(root,
                       var_choose,
                       *list_days,
                       )
drop_down.pack()

Button(root, text="Show Results", command=show_results, padx=30, pady=30).pack()

root.mainloop()
