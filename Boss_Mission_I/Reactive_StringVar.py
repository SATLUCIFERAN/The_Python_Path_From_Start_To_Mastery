
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("StringVar")
name = tk.StringVar(value="Tatooine")
ttk.Entry(root, textvariable=name, width=22).pack(padx=8, pady=6)
ttk.Label(root, textvariable=name, font=("Segoe UI", 12, "bold")).pack(padx=8, pady=6)
root.after(1200, lambda: name.set("Dagobah"))
root.mainloop()


