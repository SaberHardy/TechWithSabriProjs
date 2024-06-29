import tkinter as tk
from tkinter import Tk

from PIL import Image, ImageTk


class ImageMover:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Image Mover")

        self.image = Image.open("../../static_files/technology.png")
        self.image = ImageTk.PhotoImage(self.image)

        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        self.image_id = self.canvas.create_image(400, 300, image=self.image)

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)

    def move_left(self, event):
        self.canvas.move(self.image_id, -10, 0)

    def move_right(self, event):
        self.canvas.move(self.image_id, 10, 0)

    def move_up(self, event):
        self.canvas.move(self.image_id, 0, -10)

    def move_down(self, event):
        self.canvas.move(self.image_id, 0, 10)


root = Tk()
app = ImageMover(root)
root.mainloop()
