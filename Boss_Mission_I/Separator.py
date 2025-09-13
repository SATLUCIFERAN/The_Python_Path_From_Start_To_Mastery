
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("Jedi UI — Separator")
ttk.Label(root, text="Mission Header").pack(padx=10, pady=(10,4))
ttk.Separator(root, orient="horizontal").pack(fill="x", padx=10, pady=6)
ttk.Label(root, text="Details below the line").pack(padx=10, pady=4)
root.mainloop()


