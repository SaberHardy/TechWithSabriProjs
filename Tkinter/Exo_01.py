import tkinter as tk


def button_click(symbol):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + symbol)


def clear_display():
    entry_display.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry_display.get())
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")


root = tk.Tk()
root.title("Simple Calculator")

# Display
entry_display = tk.Entry(root, width=25, font=('Arial', 14), justify="right")
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 12),
                       command=lambda symbol=text: button_click(symbol))
    button.grid(row=row, column=col, padx=5, pady=5)

# Clear button
button_clear = tk.Button(root, text='C', width=5, height=2, font=('Arial', 12), command=clear_display)
button_clear.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

# Calculate button
button_calculate = tk.Button(root, text='=', width=5, height=2, font=('Arial', 12), command=calculate)
button_calculate.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

root.mainloop()
