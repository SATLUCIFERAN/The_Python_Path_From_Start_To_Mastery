import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("DoubleVar demo")
value = tk.DoubleVar(value=3.5)
tk.Scale(root, from_=0, to=10, orient="horizontal",
         resolution=0.1, variable=value, length=260).pack(padx=10, pady=6)  
ttk.Entry(root, textvariable=value, width=8).pack(pady=4)
ttk.Label(root, textvariable=value).pack(pady=6)

root.mainloop()


