
import tkinter as tk; from tkinter import ttk
root = tk.Tk(); root.title("sticky + weight")
f = ttk.Frame(root, padding=6); f.grid(sticky="nsew")
root.rowconfigure(0, weight=1); root.columnconfigure(0, weight=1)
for r in range(3):
    f.rowconfigure(r, weight=1)
    for c in range(3):
        f.columnconfigure(c, weight=1)
        ttk.Label(f, text="TEXT", relief="solid").grid(row=r, column=c, 
                                                    sticky="nsew", padx=2, pady=2)
root.mainloop()



