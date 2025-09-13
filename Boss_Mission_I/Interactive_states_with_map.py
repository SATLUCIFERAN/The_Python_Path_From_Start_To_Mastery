

import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("D: State Map"); root.geometry("320x140")
style = ttk.Style(root); style.theme_use("clam")
style.configure("CalendarDay.TButton", padding=6)
style.map("CalendarDay.TButton",
          background=[("active", "#2b4b7c"), ("pressed", "#1d355e")],
          foreground=[("active", "white"), ("pressed", "white")])
ttk.Button(root, text="Hover / Press me", style="CalendarDay.TButton")\
    .pack(padx=12, pady=20, fill="x")
root.mainloop()



