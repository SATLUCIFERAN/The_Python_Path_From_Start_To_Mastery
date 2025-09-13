
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("C: Custom Style"); root.geometry("320x160")
style = ttk.Style(root); style.theme_use("clam")
style.configure("CalendarDay.TButton", padding=4, font=("Segoe UI", 10, "bold"))

frame = ttk.Frame(root); frame.pack(padx=10, pady=10, fill="both", expand=True)
for i in range(1, 7):
    r, c = divmod(i-1, 3)
    ttk.Button(frame, text=str(i), style="CalendarDay.TButton")\
        .grid(row=r, column=c, padx=4, pady=4, sticky="nsew")
for r in range(2): frame.grid_rowconfigure(r, weight=1)
for c in range(3): frame.grid_columnconfigure(c, weight=1)

root.mainloop()



