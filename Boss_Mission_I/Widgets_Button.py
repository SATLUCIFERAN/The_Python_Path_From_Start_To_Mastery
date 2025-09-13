
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("Jedi UI — Buttons")

def prev(): print("⟪ hyperspace to previous sector")
def next_(): print("hyperspace to next sector ⟫")

ttk.Button(root, text="◀", width=3, command=prev).pack(side="left", padx=6, pady=10)
ttk.Label(root, text="September 2025").pack(side="left")
ttk.Button(root, text="▶", width=3, command=next_).pack(side="left", padx=6)

root.mainloop()




