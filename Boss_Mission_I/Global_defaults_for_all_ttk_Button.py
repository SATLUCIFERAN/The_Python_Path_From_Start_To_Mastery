
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("B: Global Button Style"); root.geometry("300x140")
style = ttk.Style(root); style.theme_use("clam")
style.configure("TButton", padding=10, font=("Segoe UI", 11))
ttk.Button(root, text="Primary").pack(pady=10)
ttk.Button(root, text="Another").pack()
root.mainloop()





