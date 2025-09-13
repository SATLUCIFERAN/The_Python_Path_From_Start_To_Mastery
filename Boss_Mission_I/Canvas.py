
import tkinter as tk
root = tk.Tk(); root.title("Jedi UI — Canvas")
c = tk.Canvas(root, width=320, height=120, bg="#0f1115", highlightthickness=0)
c.pack(padx=10, pady=10)
c.create_text(160, 30, text="JEDI TIMEKEEPER", fill="#66ccff",
              font=("Segoe UI", 18, "bold"))
c.create_oval(150, 70, 170, 90, fill="#ffbb33", outline="")  # event dot

root.mainloop()



