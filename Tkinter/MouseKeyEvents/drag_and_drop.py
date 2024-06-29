from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Tk


class DragAndDrop:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Drag And Drop Object")
        self.image = Image.open("../../static_files/save.jpeg")
        self.image = ImageTk.PhotoImage(self.image)
        self.canvas = tk.Canvas(root, width=700, height=600)
        self.canvas.pack()
        self.image_id = self.canvas.create_image(400, 300, image=self.image)

        self.coordination_label = tk.Label(root, text="")
        self.coordination_label.pack()

        self.canvas.tag_bind(self.image_id, "<ButtonPress-1>", self.on_start)
        self.canvas.tag_bind(self.image_id, "<B1-Motion>", self.on_drag)

    def on_start(self, event):
        self.start_x = event.x
        self.start_y = event.y
        print(self.start_x, self.start_y)

    def on_drag(self, event):
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        self.canvas.move(self.image_id, dx, dy)
        self.start_x = event.x
        self.start_y = event.y

        coordination = self.canvas.coords(self.image_id)
        self.coordination_label.config(text=f"Coordination: ({int(coordination[0])}, {int(coordination[1])})")


root = Tk()
app = DragAndDrop(root)
root.mainloop()
