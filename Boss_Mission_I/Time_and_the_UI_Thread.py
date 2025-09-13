
import tkinter as tk
from tkinter import ttk
import threading, time

root = tk.Tk()
root.title("Modal + Thread (mini)")
root.geometry("280x150")

def open_dialog():
    dlg = tk.Toplevel(root)
    dlg.title("Sync")
    dlg.transient(root)
    dlg.grab_set()             # make it modal
    msg = tk.StringVar(value="Ready")
    ttk.Label(dlg, textvariable=msg).pack(pady=10)

    t = {"thr": None}                               # holder so inner funcs can see the thread

    def work():                                     # long task (off the UI thread)
        time.sleep(2.5)                             # pretend to do heavy work
                                                    # ... real code would go here ...

    def poll():                                     # check thread status without blocking
        if t["thr"].is_alive():
            dlg.after(100, poll)                    # keep polling
        else:
            msg.set("Done!")

    def start():
        if t["thr"] and t["thr"].is_alive(): return
        msg.set("Working…")
        t["thr"] = threading.Thread(target=work, daemon=True)
        t["thr"].start()
        poll()

    ttk.Button(dlg, text="Start", command=start).pack(pady=5)
    ttk.Button(dlg, text="Close", command=dlg.destroy).pack()
    root.wait_window(dlg)                           # wait here until dialog closes

ttk.Button(root, text="Open Modal", command=open_dialog).pack(pady=30)
root.mainloop()
