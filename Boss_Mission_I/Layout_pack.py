
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("pack")
bar = ttk.Frame(root, padding=6); bar.pack(fill="x")
ttk.Button(bar, text="◀").pack(side="left")
ttk.Label(bar, text="September 2025", font=("Segoe UI", 12, "bold"))\
          .pack(side="left", padx=8)
ttk.Button(bar, text="▶").pack(side="left")
root.mainloop()





