# dialog_event.py

# import tkinter as tk
# from tkinter import ttk

# class EventDialog:
#     """Modal dialog that returns {'title': ...} or None on cancel."""
#     def __init__(self, parent, default_title=""):
#         dlg = tk.Toplevel(parent); dlg.title("New Event")
#         ttk.Label(dlg, text="Title:").grid(row=0, column=0, padx=8, pady=8)
#         self.var = tk.StringVar(value=default_title)
#         ttk.Entry(dlg, textvariable=self.var, width=28).grid(row=0, column=1, padx=8, pady=8)
#         ttk.Button(dlg, text="Cancel", command=dlg.destroy).grid(row=1, column=0, pady=8)
#         ttk.Button(
#             dlg, text="Save",
#             command=lambda: (setattr(self, "result", self.var.get().strip() or None), dlg.destroy())
#         ).grid(row=1, column=1, pady=8)

#         dlg.transient(parent); dlg.grab_set()
#         parent.wait_window(dlg)   # modal pause




######################### Sprint 3 ######################

# dialog_event.py 

import tkinter as tk
from tkinter import ttk

DEFAULT_START = "12:00"
DEFAULT_END   = "13:00"

def _coerce_hhmm(s: str, fallback: str) -> str:
    s = (s or "").strip()
    if not s: return fallback
    if len(s)==4 and s.isdigit(): return f"{s[:2]}:{s[2:]}"   # "0900" -> "09:00"
    parts = s.split(":")
    if len(parts)==2 and parts[0].isdigit() and parts[1].isdigit():
        hh, mm = int(parts[0]), int(parts[1])
        if 0<=hh<=23 and 0<=mm<=59: return f"{hh:02d}:{mm:02d}"
    return fallback

class EventDialog:
    """Modal dialog. Returns dict with title/notes/start_hhmm/end_hhmm + raw_* for delete-detect."""
    def __init__(self, parent, title="Event", init=None, date_for_label=None):
        dlg = tk.Toplevel(parent); dlg.title(title)

        ttk.Label(dlg, text="Title:").grid(row=0, column=0, padx=8, pady=4, sticky="e")
        self.var_title = tk.StringVar(value=(init.title if init else ""))
        ttk.Entry(dlg, textvariable=self.var_title, width=28).grid(row=0, column=1, padx=8, pady=4)

        r = 1
        if date_for_label:
            ttk.Label(dlg, text="Date:").grid(row=r, column=0, padx=8, pady=4, sticky="e")
            ttk.Label(dlg, text=date_for_label.strftime("%A, %B %d, %Y")).grid(row=r, column=1, padx=8, pady=4, sticky="w")
            r += 1

        ttk.Label(dlg, text="Start (HH:MM):").grid(row=r,   column=0, padx=8, pady=4, sticky="e")
        ttk.Label(dlg, text="End (HH:MM):").grid(  row=r+1, column=0, padx=8, pady=4, sticky="e")
        self.var_start = tk.StringVar(value=(init.start_ts[11:16] if init else DEFAULT_START))
        self.var_end   = tk.StringVar(value=(init.end_ts[11:16]   if init else DEFAULT_END))
        ttk.Entry(dlg, textvariable=self.var_start, width=10).grid(row=r,   column=1, sticky="w", padx=8, pady=4)
        ttk.Entry(dlg, textvariable=self.var_end,   width=10).grid(row=r+1, column=1, sticky="w", padx=8, pady=4)

        ttk.Label(dlg, text="Notes:").grid(row=r+2, column=0, padx=8, pady=4, sticky="ne")
        self.txt_notes = tk.Text(dlg, width=28, height=4)
        if init: self.txt_notes.insert("1.0", init.notes or "")
        self.txt_notes.grid(row=r+2, column=1, padx=8, pady=4)

        frm = ttk.Frame(dlg); frm.grid(row=r+3, column=0, columnspan=2, pady=8)
        ttk.Button(frm, text="Cancel", command=dlg.destroy).pack(side="left", padx=4)
        ttk.Button(frm, text="Save", command=lambda: self._save(dlg)).pack(side="right", padx=4)
        dlg.bind("<Return>", lambda e: self._save(dlg))

        dlg.transient(parent); dlg.grab_set()
        parent.wait_window(dlg)

    def _save(self, dlg):
        raw_title = (self.var_title.get() or "").strip()
        raw_notes = (self.txt_notes.get("1.0", "end") or "").strip()
        # Normalize safely; controller still sees raw_* for delete-detect
        title = raw_title or "Untitled"
        self.result = {
            "title": title,
            "notes": raw_notes,
            "start_hhmm": _coerce_hhmm(self.var_start.get(), DEFAULT_START),
            "end_hhmm":   _coerce_hhmm(self.var_end.get(),   DEFAULT_END),
            "raw_title": raw_title,
            "raw_notes": raw_notes,
        }
        dlg.destroy()
