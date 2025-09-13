
import tkinter as tk
from tkinter import ttk

root = tk.Tk(); root.title("Jedi UI — Treeview")
cols = ("title","start","end")
tree = ttk.Treeview(root, columns=cols, show="headings", height=6)
for c in cols: tree.heading(c, text=c.title())

scroll = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)
tree.grid(row=0, column=0, sticky="nsew"); scroll.grid(row=0, column=1, sticky="ns")
root.grid_rowconfigure(0, weight=1); root.grid_columnconfigure(0, weight=1)
tree.insert("", "end", values=("Council Briefing","2025-09-05 09:00","09:30"))
tree.insert("", "end", values=("Lightsaber Drills","2025-09-05 12:00","13:00"))

root.mainloop()

