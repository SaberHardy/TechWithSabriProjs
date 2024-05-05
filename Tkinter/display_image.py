from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Display Image to the User")
root.iconbitmap('/Users/macbook/PycharmProjects/TechWithSabri/static_files/technology.png')
root.geometry('500x400')
read_image = Image.open('../static_files/kid.jpg')

resized_image = read_image.resize((400, 400))

my_image = ImageTk.PhotoImage(resized_image)
img_label = Label(image=my_image)
img_label.pack()

quit_btn = Button(root, text='Exit', command=root.quit)
quit_btn.pack()

root.mainloop()
