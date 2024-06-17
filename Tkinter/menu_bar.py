from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('500x500')

def print_hello():
    print("This is hello message!")

main_menu = Menu(root)
root.config(menu=main_menu)
main_menu.add_command(label="File", command=print_hello)

file_menu = Menu(main_menu)
main_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label='Save', command=print_hello)
file_menu = Menu(main_menu)
main_menu.add_cascade(label="Edit", menu=file_menu)

save_menu = Menu(file_menu)
save_menu.add_command(label="SAVE", command=print_hello)


root.mainloop()
