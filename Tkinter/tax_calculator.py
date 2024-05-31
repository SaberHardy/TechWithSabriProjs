from tkinter import *
from tkinter import messagebox


class BankSystem:
    def __init__(self, root: Tk):
        self.root = root
        self.root.geometry("500x400")
        self.root.configure(background="#8fa3c2")
        self.root.title("Bank system - Tax Calculator")

        self.income_label = Label(root, text="Enter your YEARLY income ")
        self.income_label.grid(row=0, column=0, padx=10, pady=10)

        self.income_entry = Entry(root)
        self.income_entry.grid(row=0, column=1, padx=10, pady=10)

        self.calculate_button = Button(root, text="Calculate Tax", command=self.calculate_tax)
        self.calculate_button.grid(row=1, column=1)

        self.result_label = Label(root, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def calculate_tax(self):
        try:
            income = float(self.income_entry.get())
            tax = self.compute_taxes(income)
            self.result_label.config(text=f"Tax amount: ${tax:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please provide a valid input.")

    def compute_taxes(self, income):
        # example tax rate of 20%
        tax_rate = 0.2
        return tax_rate * income


if __name__ == "__main__":
    root = Tk()
    app = BankSystem(root)
    root.mainloop()
