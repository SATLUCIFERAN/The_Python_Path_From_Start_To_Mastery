

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x150")
img = tk.PhotoImage(file=r"icons/python.png").subsample(20,20)  
btn = ttk.Button(root, text=" Prev", image=img, compound="left")
btn.image = img  
btn.pack()
root.mainloop()



