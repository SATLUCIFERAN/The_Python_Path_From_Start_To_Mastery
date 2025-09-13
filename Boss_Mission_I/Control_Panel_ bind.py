
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Bind() Example")
root.geometry("320x180")
status = tk.StringVar(value="Click the canvas.")

def on_canvas_click(e):
    status.set(f"Canvas click at ({e.x}, {e.y})")

c = tk.Canvas(root, width=260, height=60, highlightthickness=1)
c.pack(pady=6)
c.create_text(130, 30, text="Click me")
c.bind("<Button-1>", on_canvas_click)

ttk.Label(root, textvariable=status).pack(pady=6)
root.mainloop()