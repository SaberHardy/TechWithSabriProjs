import string
import tkinter as tk
import random


def generate_password():
    password_length = int(length_entry.get())

    if password_length < 1:
        length_entry.delete(0, tk.END)
        length_entry.insert(0, 'Invalid Password Length')
        return

    password = ''.join(random.choices(
        string.ascii_letters + string.digits + string.punctuation, k=password_length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)



root = tk.Tk()
root.geometry('500x400')
root.title("Password Generator")

length_label = tk.Label(root, text="Give me Password Length")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=1)

password_label = tk.Label(root, text="Generated Password")
password_label.grid(row=2, column=0)

password_entry = tk.Entry(root)
password_entry.grid(row=2, column=1, padx=5, pady=5)

print("This is another commit also to check it . . .")

root.mainloop()
