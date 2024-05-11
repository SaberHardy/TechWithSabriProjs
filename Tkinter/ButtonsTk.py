from tkinter import *

# create a tkinter window
master = Tk()

# Open window having dimension 200x100
master.geometry('200x100')

# Create a Button
Button(master,
       text='Submit',
       bg='blue').pack()

master.mainloop()
