
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("Jedi UI — Checkbutton")
shields = tk.BooleanVar(value=True)
ttk.Checkbutton(root, text="Show Past Missions", variable=shields,
                command=lambda: print("Past missions visible:", 
                                      shields.get())).pack(padx=10, pady=10)
root.mainloop()




