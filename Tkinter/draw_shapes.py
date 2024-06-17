from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('500x500')

canvas = Canvas(root, width=500, height=500, bg='white')
canvas.pack()

# canvas.create_line(50, 50, 200, 200, fill='black', width=2)
# ---------------------- x1, y1, x2,  y2
canvas.create_rectangle(50, 250, 150, 350, outline='green', width=2)

canvas.create_oval(200, 50, 300, 150, outline='green', width=2)

canvas.create_polygon(200, 250, 250, 300, 400, 250, 250, 200,
                      fill='yellow', outline='red', width=2)

canvas.create_arc(50, 50, 150, 150, start=0, extent=150, outline='blue', width=2)


root.mainloop()
