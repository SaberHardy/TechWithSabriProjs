import time
import tkinter as tk
from datetime import timedelta


class TimerCloackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer and Cloak")

        # Cloak
        self.cloak_label = tk.Label(root, font=('calibri', 40, 'bold'), background='green', foreground='white')
        self.cloak_label.pack()
        self.update_cloak()

        # Timer
        self.timer_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
        self.timer_label.pack()

        self.timer_entry = tk.Entry(root, font=('calibri', 20))
        self.timer_entry.pack(anchor='center')

        self.start_timer_button = tk.Button(root, text="Start Timer", command=self.start_timer, font=('calibri', 20))
        self.start_timer_button.pack(anchor='center')

        self.timer_seconds = 0
        self.running = False

    def update_cloak(self):
        now = time.strftime("%H:%M:%S")
        self.cloak_label.config(text=now)
        self.root.after(1000, self.update_cloak)

    def start_timer(self):
        if not self.running:
            self.timer_seconds = int(self.timer_entry.get())
            self.timer_entry.delete(0, 'end')
            self.running = True
            self.update_timer()

    def update_timer(self):
        if self.running:
            if self.timer_seconds > 0:
                self.timer_seconds -= 1
                self.timer_label.config(text=str(timedelta(seconds=self.timer_seconds)))
                self.root.after(1000, self.update_timer)
            else:
                self.timer_label.config(text="Time's UP!")
                self.running = False


root = tk.Tk()
app = TimerCloackApp(root)
root.mainloop()
