import tkinter
from tkinter import *


class ShapeMover:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Move canvas shapes with arrow keys")
        self.root.geometry("500x500")
        self.canvas = tkinter.Canvas(root, width=500, height=500, bg='white')
        self.canvas.pack()

        self.rectangle = self.canvas.create_rectangle(40, 40, 150, 150, fill='yellow')

        self.root.bind('<Left>', self.move_left)
        self.root.bind('<Right>', self.move_right)
        self.root.bind('<Up>', self.move_up)
        self.root.bind('<Down>', self.move_down)

    def move_left(self, event):
        self.canvas.move(self.rectangle, -10, 0)

    def move_right(self, event):
        self.canvas.move(self.rectangle, 10, 0)

    def move_up(self, event):
        self.canvas.move(self.rectangle, 0, -10)

    def move_down(self, event):
        self.canvas.move(self.rectangle, 0, 10)


root = Tk()
shape_mover = ShapeMover(root)
root.mainloop()
