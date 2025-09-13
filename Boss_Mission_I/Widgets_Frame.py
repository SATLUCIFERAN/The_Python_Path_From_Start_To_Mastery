
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("Jedi UI — Frames")
header  = ttk.Frame(root, padding=8)   # cockpit
weekbar = ttk.Frame(root, padding=4)   # dashboard
gridpad = ttk.Frame(root, padding=8)   # main deck

header.pack(fill="x"); weekbar.pack(fill="x"); gridpad.pack(fill="both", expand=True)

ttk.Label(header, text="Galactic Calendar", 
          font=("Segoe UI", 16, "bold")).pack()
for name in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]:
    ttk.Label(weekbar, text=name, width=4, anchor="center").pack(side="left", expand=True)

root.mainloop()


