
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("Jedi UI — Spinbox")
year = tk.StringVar(value="2025")
day  = tk.StringVar(value="1")

ttk.Spinbox(root, from_=2000, to=2100, textvariable=year, 
            width=8).pack(padx=10,pady=6)
ttk.Spinbox(root, from_=1, to=31, textvariable=day,  width=5).pack(pady=6)
ttk.Button(root, text="Confirm",
           command=lambda: print(f"Chosen {year.get()}-{int(day.get()):02d}"))\
           .pack(pady=6)

root.mainloop()





