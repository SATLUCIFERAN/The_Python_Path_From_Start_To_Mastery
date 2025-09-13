import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Command= Example")
root.geometry("250x100")

status_text = tk.StringVar()
status_text.set("Ready to click.")

def on_button_click():    
    status_text.set("Button was clicked!")

ttk.Button(root, text="Click Me", command=on_button_click).pack(pady=20)
ttk.Label(root, textvariable=status_text).pack()

root.mainloop()