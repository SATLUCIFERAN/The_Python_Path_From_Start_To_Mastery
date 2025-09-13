
import tkinter as tk
from tkinter import ttk
import calendar

root = tk.Tk(); root.title("Jedi UI — Combobox")
month = tk.StringVar(value=calendar.month_name[9])
year  = tk.StringVar(value="2025")

ttk.Combobox(root, textvariable=month, values=list(calendar.month_name)[1:],
             state="readonly", width=14).pack(padx=8, pady=6)
ttk.Combobox(root, textvariable=year, values=[str(y) for y in range(2020,2031)],
             state="readonly", width=8).pack(pady=6)
ttk.Button(root, text="Jump", 
           command=lambda: print("Jump to:", month.get(), year.get())).pack(pady=6)

root.mainloop()



