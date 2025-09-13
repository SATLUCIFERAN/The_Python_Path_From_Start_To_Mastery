
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("IntVar")
level = tk.IntVar(value=1)                 

def level_up(_=None): level.set(level.get()+1)

tk.Spinbox(root, from_=1, to=10, textvariable=level, width=5).pack(padx=8, pady=6)
ttk.Label(root, textvariable=level, font=("Segoe UI", 12, "bold")).pack()
ttk.Button(root, text="Level Up", command=level_up).pack(pady=6)
root.bind("<Control-Up>", level_up)    
root.mainloop()


