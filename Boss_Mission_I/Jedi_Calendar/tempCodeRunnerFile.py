import tkinter as tk
# from tkinter import ttk
# import calendar  # real month layout
# from datetime import date, datetime, time, UTC

# from repo_concise import EventRepository
# from dialog_event import EventDialog
# from models import Event


# # --- View ---
# class CalendarView(ttk.Frame):
#     """Sprint 1: Month header, flexible weekdays, 6x7 grid. Click → highlight day."""
#     WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

#     def __init__(self, master, on_new_event):
#         super().__init__(master, padding=8)
#         self.on_new_event = on_new_event  # kept for Sprint 3 reuse
#         today = date.today()
#         self.year, self.month = today.year, today.month
#         self.selected: date | None = None

#         # Header: ◀ Month Year ▶
#         hdr = ttk.Frame(self); hdr.grid(row=0, column=0, sticky="ew")
#         hdr.columnconfigure(1, weight=1)
#         ttk.Button(hdr, text="◀", width=3, command=self.prev_month).grid(row=0, column=0)
#         self.title = tk.StringVar()
#         ttk.Label(hdr, textvariable=self.title, font=("Segoe UI", 11, "bold")).grid(row=0, column=1)
#         ttk.Button(hdr, text="▶", width=3, command=self.next_month).grid(row=0, column=2)

#         # Weekday bar (flexible columns)
#         wk = ttk.Frame(self); wk.grid(row=1, column=0, sticky="ew", pady=(6, 0))
#         for i, name in enumerate(self.WEEKDAYS):
#             wk.columnconfigure(i, weight=1)  # share space evenly
#             ttk.Label(wk, text=name, anchor="center").grid(row=0, column=i, sticky="nsew")

#         # 6x7 grid (build once, repaint monthly)
#         grid = ttk.Frame(self); grid.grid(row=2, column=0, sticky="nsew", pady=(4, 0))
#         self.columnconfigure(0, weight=1); self.rowconfigure(2, weight=1)
#         for r in range(6): grid.rowconfigure(r, weight=1)
#         for c in range(7): grid.columnconfigure(c, weight=1)
#         self.cells: list[list[ttk.Button]] = []
#         for r in range(6):
#             row = []
#             for c in range(7):
#                 b = ttk.Button(grid, text=" ", command=lambda: None)
#                 b.grid(row=r, column=c, sticky="nsew", padx=1, pady=1, ipady=6)
#                 row.append(b)
#             self.cells.append(row)

#         self.render_month()

#     # Navigation
#     def prev_month(self):
#         self.month = 12 if self.month == 1 else self.month - 1
#         self.year  = self.year - 1 if self.month == 12 else self.year
#         self.selected = None
#         self.render_month()

#     def next_month(self):
#         self.month = 1 if self.month == 12 else self.month + 1
#         self.year  = self.year + 1 if self.month == 1 else self.year
#         self.selected = None
#         self.render_month()

#     # Paint current month
#     def render_month(self):
#         self.title.set(date(self.year, self.month, 1).strftime("%B %Y"))
#         weeks = calendar.monthcalendar(self.year, self.month)  # [[Mon..Sun], ...]
#         while len(weeks) < 6: weeks.append([0] * 7)            # pad to 6 rows
#         today = date.today()

#         for r in range(6):
#             for c in range(7):
#                 day_num = weeks[r][c]
#                 btn = self.cells[r][c]
#                 if day_num == 0:
#                     btn.config(text=" ", state="disabled", command=lambda: None)
#                 else:
#                     d = date(self.year, self.month, day_num)
#                     label = f"{day_num}"
#                     if d == today: label = f"[{day_num}]"        # today hint
#                     if d == self.selected: label = f"★ {label}"  # clicked star
#                     btn.config(text=label, state="normal",
#                               command=lambda dd=d: self.select_day(dd))

#     # Click → highlight
#     def select_day(self, d: date):
#         self.selected = d
#         self.render_month()
#         # (Sprint 3: EventDialog + DB save will go here)


# # --- Controller ---
# class TimekeeperApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Jedi Timekeeper")
#         self.root.geometry("900x620")  # comfy grid

#         self.repo = EventRepository()  # DB not used in Sprint 1
#         self.view = CalendarView(self.root, self.new_event)
#         self.view.pack(fill="both", expand=True)

#     # placeholder for Sprint 3
#     def new_event(self, day: date):
#         dlg = EventDialog(self.root)
#         title = getattr(dlg, "result", None)
#         if not title:
#             return
#         start = datetime.combine(day, time(12, 0), tzinfo=UTC).isoformat()
#         end   = datetime.combine(day, time(13, 0), tzinfo=UTC).isoformat()
#         ev = Event(id=None, title=title, start_ts=start, end_ts=end, notes="")
#         new_id = self.repo.add_event(ev)
#         print(f"[controller] Saved event #{new_id}: {ev.title} on {day}")

#     def run(self):
#         self.root.mainloop()


# if __name__ == "__main__":
#     TimekeeperApp().run()
