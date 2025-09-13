
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("Jedi UI — Entry")
query = tk.StringVar()
ttk.Entry(root, textvariable=query, width=28).pack(padx=10, pady=8)
ttk.Button(root, text="Scan", command=lambda: print("Scan:", query.get())).pack(pady=6)

root.mainloop()



