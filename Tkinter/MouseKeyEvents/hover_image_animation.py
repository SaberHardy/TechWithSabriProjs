import tkinter as tk
from tkinter import Tk
from PIL import Image, ImageTk


class HoveImageAnimation:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Animation")
        self.original_image = Image.open("../../static_files/technology.png")
        self.image = ImageTk.PhotoImage(self.original_image)

        # Create Canvas
        self.canvas = tk.Canvas(root, width=800, height=700)
        self.canvas.pack()
        self.image_id = self.canvas.create_image(400, 300, image=self.image)

        self.canvas.tag_bind(self.image_id, "<Enter>", self.on_hover)
        self.canvas.tag_bind(self.image_id, "<Leave>", self.on_leave)

    def on_hover(self, event):
        self.zoom_image(1.2)

    def on_leave(self, event):
        self.zoom_image(1.0)

    def zoom_image(self, scale_factor):
        width, height = self.original_image.size
        new_size = (int(width * scale_factor), int(height * scale_factor))
        resized_image = self.original_image.resize(new_size, Image.Resampling.LANCZOS)
        # print(resized_image)
        self.image = ImageTk.PhotoImage(resized_image)
        self.canvas.itemconfig(self.image_id, image=self.image)


root = Tk()
app = HoveImageAnimation(root)
root.mainloop()
