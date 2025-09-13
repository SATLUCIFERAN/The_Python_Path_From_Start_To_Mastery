
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("BooleanVar")
shields_up = tk.BooleanVar(value=False)

def update_status(*_):
    status["text"] = "Shields: UP" if shields_up.get() else "Shields: DOWN"

ttk.Checkbutton(root, text="Raise shields", variable=shields_up, 
                command=update_status).pack(padx=8, pady=6)
status = ttk.Label(root); status.pack(padx=8, pady=6)
update_status()
root.mainloop()





