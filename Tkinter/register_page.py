from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class RegisterUser:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Register Form")
        self.root.geometry("800x600")

        self.canvas = Canvas(self.root)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.scrollbar = Scrollbar(self.root, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill='y')

        self.frame.bind("<Configure>", self.on_frame_configure)

        self.entries = {}

        self.create_register_form()

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def create_register_form(self):
        labels = ["First Name", "Last Name", "Email", "Username",
                  "Password", "Address", "City", "State", "ZipCode", "Phone number"]

        for index, label in enumerate(labels):
            Label(self.frame, text=label).grid(row=index, column=0, padx=10, pady=10)
            entry = Entry(self.frame, width=30)
            entry.grid(row=index, column=1, padx=10, pady=10)
            self.entries[label] = entry

        register_btn = Button(self.frame, text="Register", command=self.register_user)
        register_btn.grid(row=len(labels), columnspan=3, pady=20)

    def register_user(self):
        user_info = {label: entry.get() for label, entry in self.entries.items()}

        messagebox.showinfo("Registration", "You have registered successfully!")

        for entry in self.entries.values():
            entry.delete(0, END)


root = Tk()
app = RegisterUser(root)
root.mainloop()
