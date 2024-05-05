from tkinter import *

root = Tk()
root.title("Save Settings")
root.geometry('500x500')


def save_settings():
    print(f"Settings for datk mode saved Successfully {dark_mode.get()}")
    print(f"Settings for notification mode are saved Successfully {notification_mode.get()}")


dark_mode = IntVar()
dark_mode_checkbox = Checkbutton(root, text="Dark Mode", variable=dark_mode)
dark_mode_checkbox.pack()

notification_mode = IntVar()
dark_mode_checkbox = Checkbutton(root, text="Enable Notifications", variable=notification_mode)
dark_mode_checkbox.pack()

save_btn = Button(root, text="Save Settings", command=save_settings)
save_btn.pack()

root.mainloop()
