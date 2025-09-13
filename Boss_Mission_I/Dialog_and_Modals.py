
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Modal demo")
status = tk.StringVar(value="Ready.")

def ask_title():
    # 1) make the dialog
    dlg = tk.Toplevel(root)
    dlg.title("New Event")
    ttk.Label(dlg, text="Title:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
    title = tk.StringVar()
    ttk.Entry(dlg, textvariable=title, width=24).grid(row=0, column=1, padx=8, pady=8)

    # buttons
    ttk.Button(dlg, text="Cancel", command=dlg.destroy).grid(row=1, column=0, pady=8)
    def save_and_close():
        dlg.result = title.get().strip()  # stash data on the dialog
        dlg.destroy()
    ttk.Button(dlg, text="Save", command=save_and_close).grid(row=1, column=1, pady=8)

    # 2) make it modal
    dlg.transient(root)   # follow the main window
    dlg.grab_set()        # focus here only
    root.wait_window(dlg) # <- code STOPS here until dialog closes

    # 3) after the dialog closes, read the result
    result = getattr(dlg, "result", "")
    status.set(f"Saved: {result}" if result else "Canceled.")

ttk.Button(root, text="New Event", command=ask_title).pack(padx=12, pady=12)
ttk.Label(root, textvariable=status).pack(pady=(0,12))
root.mainloop()
