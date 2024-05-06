from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Upload File")
root.geometry('500x500')


def upload_file():
    filename = filedialog.askopenfilename(
        initialdir='/Desktop/',
        filetypes=(
            ('Png Files', '*.png'),
            ('Jpg Files', '*.jpg'),
            ('All Files', '*.*')
        )
    )

    Label(root, text=filename).pack()
    image_filename = Image.open(filename)
    my_image = ImageTk.PhotoImage(image_filename)
    label = Label(root, image=my_image)
    label.image = my_image
    label.pack()


Button(root, text="Upload File", padx=50, pady=25, command=upload_file).pack()

root.mainloop()
