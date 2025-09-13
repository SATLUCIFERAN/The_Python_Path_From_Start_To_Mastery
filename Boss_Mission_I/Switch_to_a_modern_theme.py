
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("A: Theme"); root.geometry("300x120")
style = ttk.Style(root); style.theme_use("clam")  # try: "vista", "alt", etc.
ttk.Label(root, text=f"Theme: {style.theme_use()}").pack(pady=10)
ttk.Button(root, text="A Button").pack()
root.mainloop()
