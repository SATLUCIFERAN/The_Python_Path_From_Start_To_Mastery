
import tkinter as tk; from tkinter import ttk

root = tk.Tk(); root.title("place"); root.geometry("240x110")
ttk.Label(root, text="Docking Bay 94").place(x=20, y=15)
ttk.Button(root, text="Launch").place(x=140, y=40)
root.mainloop()





