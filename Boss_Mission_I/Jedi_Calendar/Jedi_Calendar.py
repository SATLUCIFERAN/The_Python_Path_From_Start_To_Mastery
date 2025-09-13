# Jedi_Calendar.py

########################## Project Structure ##################

# import tkinter as tk
# from tkinter import ttk
# from datetime import date, datetime, time, UTC
# from repo_concise import EventRepository
# from dialog_event import EventDialog
# from models import Event

# # --- View ---
# class CalendarView(ttk.Frame):
#     def __init__(self, master, on_new_event):
#         super().__init__(master, padding=8)
#         self.on_new_event = on_new_event

#         # Header (Prev ◀  Month Year  ▶)
#         hdr = ttk.Frame(self); hdr.grid(row=0, column=0, sticky="ew")
#         ttk.Button(hdr, text="◀", width=3).pack(side="left")
#         self.title = ttk.Label(hdr, text="September 2025", font=("Segoe UI", 11, "bold"))
#         self.title.pack(side="left", expand=True, padx=6)
#         ttk.Button(hdr, text="▶", width=3).pack(side="right")

#         # Weekday bar (Mon..Sun)
#         wk = ttk.Frame(self); wk.grid(row=1, column=0, sticky="ew", pady=(6, 0))
#         for name in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]:
#             ttk.Label(wk, text=name, anchor="center", width=4).pack(side="left", expand=True)

#         # Day grid 6x7 (placeholder: all buttons call new_event with today)
#         grid = ttk.Frame(self); grid.grid(row=2, column=0, sticky="nsew", pady=(4,0))
#         for r in range(6):
#             grid.rowconfigure(r, weight=1)
#             for c in range(7):
#                 grid.columnconfigure(c, weight=1)
#                 ttk.Button(
#                     grid, text=" ", width=4,
#                     command=lambda r=r, c=c: self.on_new_event(date.today())
#                 ).grid(row=r, column=c, sticky="nsew", padx=1, pady=1)

#         self.columnconfigure(0, weight=1)
#         self.rowconfigure(2, weight=1)

# # --- Controller ---
# class TimekeeperApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Jedi Timekeeper")                  
#         self.view = CalendarView(self.root, self.new_event)
#         self.view.pack(fill="both", expand=True)

#     def new_event(self, day):        
#         print(f"[controller] New event requested for {day}")

#     def run(self):
#         self.root.mainloop()

# if __name__ == "__main__":
#     TimekeeperApp().run()





########################## Sprint 1 #######################

# import tkinter as tk
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






########################## Sprint 2  ##########################

#Jedi_Calendar.py

# import tkinter as tk
# from tkinter import ttk
# import calendar
# from datetime import date, datetime, time, UTC

# from repo_concise import EventRepository
# from dialog_event import EventDialog
# from models import Event


# # --- View ---
# class CalendarView(ttk.Frame):
#     """Sprint 2: Sprint 1 + dots on days with events."""
#     WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

#     def __init__(self, master, on_new_event, get_badge_dates=None):
#         super().__init__(master, padding=8)
#         self.on_new_event = on_new_event              # kept for Sprint 3
#         self.get_badge_dates = get_badge_dates        # NEW: callable(year, month) -> set[int]
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

#         # Weekday bar (flex)
#         wk = ttk.Frame(self); wk.grid(row=1, column=0, sticky="ew", pady=(6, 0))
#         for i, name in enumerate(self.WEEKDAYS):
#             wk.columnconfigure(i, weight=1)
#             ttk.Label(wk, text=name, anchor="center").grid(row=0, column=i, sticky="nsew")

#         # 6x7 grid
#         grid = ttk.Frame(self); grid.grid(row=2, column=0, sticky="nsew", pady=(4, 0))
#         self.columnconfigure(0, weight=1); self.rowconfigure(2, weight=1)
#         for r in range(6): grid.rowconfigure(r, weight=1)
#         for c in range(7): grid.columnconfigure(c, weight=1)
#         self.cells: list[list[ttk.Button]] = []
#         for r in range(6):
#             row=[]
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

#     # Paint current month (+ dots)
#     def render_month(self):
#         self.title.set(date(self.year, self.month, 1).strftime("%B %Y"))
#         weeks = calendar.monthcalendar(self.year, self.month)
#         while len(weeks) < 6: weeks.append([0] * 7)
#         today = date.today()

#         # NEW: ask controller which day numbers have events
#         badges = set()
#         if callable(self.get_badge_dates):
#             try:
#                 badges = set(self.get_badge_dates(self.year, self.month))
#             except Exception:
#                 badges = set()

#         for r in range(6):
#             for c in range(7):
#                 dnum = weeks[r][c]
#                 btn = self.cells[r][c]
#                 if dnum == 0:
#                     btn.config(text=" ", state="disabled", command=lambda: None)
#                 else:
#                     d = date(self.year, self.month, dnum)
#                     label = f"{dnum}"
#                     if d == today: label = f"[{dnum}]"
#                     if dnum in badges: label = f"{label} •"      # NEW: dot for busy day
#                     if d == self.selected: label = f"★ {label}"
#                     btn.config(text=label, state="normal",
#                               command=lambda dd=d: self.select_day(dd))

#     def select_day(self, d: date):
#         self.selected = d
#         self.render_month()


# # --- Controller ---
# class TimekeeperApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Jedi Timekeeper")
#         self.root.geometry("900x620")

#         self.repo = EventRepository()

#         # NEW: provide the view a way to know “which days have events”
#         def get_badge_dates(year: int, month: int) -> set[int]:
#             days = set()
#             for ev in self.repo.by_month(year, month):
#                 try:
#                     # ISO 8601: 'YYYY-MM-DD...' → take DD as int
#                     days.add(int(ev.start_ts[8:10]))
#                 except Exception:
#                     pass
#             return days

#         self.view = CalendarView(self.root, self.new_event, get_badge_dates=get_badge_dates)
#         self.view.pack(fill="both", expand=True)

#     # (used in Sprint 3; kept here)
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




########################## Sprint 3 #########################

# Jedi_Calendar.py 

# import tkinter as tk
# from tkinter import ttk, messagebox
# import calendar
# from datetime import date, datetime, time, UTC

# from repo_concise import EventRepository
# from dialog_event import EventDialog
# from models import Event


# # --- View ---
# class CalendarView(ttk.Frame):
#     """Sprint 3: Sprint 2 + double-click edit/add + right-click menu (Add / View All / Quick Delete)."""
#     WEEKDAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

#     def __init__(self, master,
#                  on_new_event,
#                  on_day_double,
#                  on_day_delete,
#                  on_view_day,
#                  get_badge_dates):
#         super().__init__(master, padding=8)
#         self.on_new_event  = on_new_event
#         self.on_day_double = on_day_double
#         self.on_day_delete = on_day_delete
#         self.on_view_day   = on_view_day
#         self.get_badge_dates = get_badge_dates

#         t = date.today()
#         self.year, self.month = t.year, t.month
#         self.selected: date | None = None

#         # Header: ◀ Month Year ▶
#         hdr = ttk.Frame(self); hdr.grid(row=0, column=0, sticky="ew")
#         hdr.columnconfigure(1, weight=1)
#         ttk.Button(hdr, text="◀", width=3, command=self.prev_month).grid(row=0, column=0)
#         self.title = tk.StringVar()
#         ttk.Label(hdr, textvariable=self.title, font=("Segoe UI", 11, "bold")).grid(row=0, column=1)
#         ttk.Button(hdr, text="▶", width=3, command=self.next_month).grid(row=0, column=2)

#         # Weekdays (flex)
#         wk = ttk.Frame(self); wk.grid(row=1, column=0, sticky="ew", pady=(6, 0))
#         for i, name in enumerate(self.WEEKDAYS):
#             wk.columnconfigure(i, weight=1)
#             ttk.Label(wk, text=name, anchor="center").grid(row=0, column=i, sticky="nsew")

#         # 6x7 grid (build once)
#         grid = ttk.Frame(self); grid.grid(row=2, column=0, sticky="nsew", pady=(4,0))
#         self.columnconfigure(0, weight=1); self.rowconfigure(2, weight=1)
#         for r in range(6): grid.rowconfigure(r, weight=1)
#         for c in range(7): grid.columnconfigure(c, weight=1)
#         self.cells: list[list[ttk.Button]] = []
#         for r in range(6):
#             row=[]
#             for c in range(7):
#                 b = ttk.Button(grid, text=" ")
#                 b.grid(row=r, column=c, sticky="nsew", padx=1, pady=1, ipady=6)
#                 b.bind("<Button-1>",  lambda e, rr=r, cc=c: self._select(rr, cc))
#                 b.bind("<Double-1>",  lambda e, rr=r, cc=c: self._dbl(rr, cc))
#                 b.bind("<Button-3>",  lambda e, rr=r, cc=c: self._menu(rr, cc, e))
#                 row.append(b)
#             self.cells.append(row)

#         # Context menu (right-click)
#         self.menu = tk.Menu(self, tearoff=0)
#         self.menu.add_command(label="Add",       command=lambda: self._menu_action("add"))
#         self.menu.add_command(label="View All",  command=lambda: self._menu_action("view"))
#         self.menu.add_separator()
#         self.menu.add_command(label="Quick Delete (all on day)", command=lambda: self._menu_action("del"))

#         self.render_month()

#     # Navigation
#     def prev_month(self):
#         self.month = 12 if self.month == 1 else self.month - 1
#         self.year  = self.year - 1 if self.month == 12 else self.year
#         self.selected = None; self.render_month()

#     def next_month(self):
#         self.month = 1 if self.month == 12 else self.month + 1
#         self.year  = self.year + 1 if self.month == 1 else self.year
#         self.selected = None; self.render_month()

#     # Month paint (+ dots)
    
#     def render_month(self):
#         self.title.set(date(self.year, self.month, 1).strftime("%B %Y"))
#         weeks = calendar.monthcalendar(self.year, self.month)
#         while len(weeks) < 6: weeks.append([0]*7)
#         today = date.today()

#         badges = set()
#         if callable(self.get_badge_dates):
#             try: badges = set(self.get_badge_dates(self.year, self.month))
#             except Exception: badges = set()

#         self.daymap = {}
#         for r in range(6):
#             for c in range(7):
#                 dnum = weeks[r][c]; btn = self.cells[r][c]
#                 if dnum == 0:
#                     btn.config(text=" ", state="disabled")
#                     self.daymap[(r,c)] = None
#                 else:
#                     d = date(self.year, self.month, dnum)
#                     self.daymap[(r,c)] = d
#                     label = f"{dnum}"
#                     if d == today: label = f"[{dnum}]"
#                     if dnum in badges: label = f"{label} •"
#                     if d == self.selected: label = f"★ {label}"
#                     btn.config(text=label, state="normal")

#     # Clicks

#     def _select(self, r, c):
#         d = self.daymap.get((r,c))
#         if d:
#             self.selected = d
#             self.render_month()

#     def _dbl(self, r, c):
#         d = self.daymap.get((r,c))
#         if d:
#             self.selected = d
#             self.on_day_double(d)
#             self.render_month()

#     def _menu(self, r, c, e):
#         d = self.daymap.get((r,c))
#         self._menu_target = d
#         if d:
#             self.selected = d
#             self.render_month()
#             self.menu.tk_popup(e.x_root, e.y_root)

#     def _menu_action(self, which: str):
#         d = getattr(self, "_menu_target", None)
#         if not d: return
#         if which == "add":
#             self.on_new_event(d)
#         elif which == "view":
#             self.on_view_day(d)
#         elif which == "del":
#             if messagebox.askyesno("Delete","Delete all events on this day?"):
#                 self.on_day_delete(d)
#         self.render_month()


# # --- Controller ---
# class TimekeeperApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Jedi Timekeeper")
#         self.root.geometry("900x620")

#         self.repo = EventRepository()

#         def get_badge_dates(year: int, month: int) -> set[int]:           
#             days = set()
#             for ev in self.repo.by_month(year, month):
#                 try:
#                     days.add(int(ev.start_ts[8:10]))
#                 except Exception:
#                     pass
#             return days

#         self.view = CalendarView(
#             self.root,
#             on_new_event=self.new_event,
#             on_day_double=self.day_double,
#             on_day_delete=self.day_delete,
#             on_view_day=self.view_day,
#             get_badge_dates=get_badge_dates
#         )
#         self.view.pack(fill="both", expand=True)

#     # New event (12:00–13:00 default)
#     def new_event(self, d: date):
#         dlg = EventDialog(self.root, title="New Event", init=None, date_for_label=d)
#         if not getattr(dlg, "result", None): return
#         hh, mm   = map(int, dlg.result["start_hhmm"].split(":"))
#         hh2, mm2 = map(int, dlg.result["end_hhmm"].split(":"))
#         start = datetime.combine(d, time(hh,mm), tzinfo=UTC).isoformat()
#         end   = datetime.combine(d, time(hh2,mm2), tzinfo=UTC).isoformat()
#         ev = Event(id=None, title=dlg.result["title"], start_ts=start, end_ts=end, notes=dlg.result["notes"])
#         self.repo.add_event(ev)
#         self.view.selected = d; self.view.render_month()

#     # Double-click → edit existing first event OR add new
#     def day_double(self, d: date):
#         evs = self.repo.by_day(d)
#         init = evs[0] if evs else None

#         dlg = EventDialog(self.root, title=("Edit Event" if init else "New Event"),
#                           init=init, date_for_label=d)
#         if not getattr(dlg, "result", None): return

#         # If editing and both cleared → delete
#         if init and dlg.result.get("raw_title","")=="" and dlg.result.get("raw_notes","")=="":
#             self.repo.delete_event(init.id)
#         else:
#             hh, mm   = map(int, dlg.result["start_hhmm"].split(":"))
#             hh2, mm2 = map(int, dlg.result["end_hhmm"].split(":"))
#             start = datetime.combine(d, time(hh,mm), tzinfo=UTC).isoformat()
#             end   = datetime.combine(d, time(hh2,mm2), tzinfo=UTC).isoformat()
#             if init:
#                 init.title, init.notes = dlg.result["title"], dlg.result["notes"]
#                 init.start_ts, init.end_ts = start, end
#                 self.repo.update_event(init)
#             else:
#                 self.repo.add_event(Event(id=None, title=dlg.result["title"],
#                                           start_ts=start, end_ts=end, notes=dlg.result["notes"]))
#         self.view.selected = d; self.view.render_month()

#     # Right-click → delete all on day
#     def day_delete(self, d: date):
#         for ev in self.repo.by_day(d):
#             self.repo.delete_event(ev.id)
#         self.view.selected = d; self.view.render_month()

#     # Right-click → View All (simple list)
#     def view_day(self, d: date):
#         evs = self.repo.by_day(d)
#         if not evs:
#             messagebox.showinfo("Events", f"No events on {d}.")
#             return
#         lines = []
#         for ev in evs:
#             lines.append(f"{ev.start_ts[11:16]}–{ev.end_ts[11:16]}  {ev.title}")
#         messagebox.showinfo(d.strftime("%A, %B %d, %Y"), "\n".join(lines))

#     def run(self):
#         self.root.mainloop()


# if __name__ == "__main__":
#     TimekeeperApp().run()



########################### Sprint 4 ############################

# Jedi_Calendar.py

# import tkinter as tk
# from tkinter import ttk, messagebox
# import calendar
# from datetime import date, datetime, time, UTC

# from repo_concise import EventRepository
# from dialog_event import EventDialog
# from models import Event


# # --- View ---
# class CalendarView(ttk.Frame):
#     """
#     Sprint 4: Sprint 3 + Toolbar (Today, New, Jump-to) + Prev/Next + shortcuts handled by controller.
#     Single-click selects (★), double-click add/edit, right-click menu (Add / View All / Quick Delete),
#     dots (•) from DB.
#     """
#     WEEKDAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
#     MONTHS = [calendar.month_name[m] for m in range(1,13)]

#     def __init__(self, master,
#                  on_new_event,
#                  on_day_double,
#                  on_day_delete,
#                  on_view_day,
#                  get_badge_dates,
#                  on_quick_new):
#         super().__init__(master, padding=8)
#         self.on_new_event   = on_new_event
#         self.on_day_double  = on_day_double
#         self.on_day_delete  = on_day_delete
#         self.on_view_day    = on_view_day
#         self.get_badge_dates = get_badge_dates
#         self.on_quick_new   = on_quick_new

#         t = date.today()
#         self.year, self.month = t.year, t.month
#         self.selected: date | None = None

#         # --- Toolbar (Today | New | Jump-to Month/Year + Go)
#         bar = ttk.Frame(self); bar.grid(row=0, column=0, sticky="ew", pady=(0,6))
#         bar.columnconfigure(5, weight=1)
#         ttk.Button(bar, text="Today", width=7, command=self.go_today).grid(row=0, column=0, padx=(0,6))
#         ttk.Button(bar, text="New",   width=7, command=self.quick_new).grid(row=0, column=1, padx=(0,12))

#         ttk.Label(bar, text="Jump to:").grid(row=0, column=2, padx=(0,4))
#         self.month_var = tk.StringVar(value=calendar.month_name[self.month])
#         self.year_var  = tk.StringVar(value=str(self.year))
#         ttk.Combobox(bar, textvariable=self.month_var, values=self.MONTHS, width=11, state="readonly").grid(row=0, column=3)
#         ttk.Spinbox(bar, from_=1900, to=3000, textvariable=self.year_var, width=6).grid(row=0, column=4, padx=(6,0))
#         ttk.Button(bar, text="Go", width=4, command=self.jump_to).grid(row=0, column=6, padx=(8,0))

#         # --- Header: ◀ Month Year ▶
#         hdr = ttk.Frame(self); hdr.grid(row=1, column=0, sticky="ew")
#         hdr.columnconfigure(1, weight=1)
#         ttk.Button(hdr, text="◀", width=3, command=self.prev_month).grid(row=0, column=0)
#         self.title = tk.StringVar()
#         ttk.Label(hdr, textvariable=self.title, font=("Segoe UI", 11, "bold")).grid(row=0, column=1)
#         ttk.Button(hdr, text="▶", width=3, command=self.next_month).grid(row=0, column=2)

#         # --- Weekdays (flex)
#         wk = ttk.Frame(self); wk.grid(row=2, column=0, sticky="ew", pady=(6, 0))
#         for i, name in enumerate(self.WEEKDAYS):
#             wk.columnconfigure(i, weight=1)
#             ttk.Label(wk, text=name, anchor="center").grid(row=0, column=i, sticky="nsew")

#         # --- 6x7 grid (build once)
#         grid = ttk.Frame(self); grid.grid(row=3, column=0, sticky="nsew", pady=(4,0))
#         self.columnconfigure(0, weight=1); self.rowconfigure(3, weight=1)
#         for r in range(6): grid.rowconfigure(r, weight=1)
#         for c in range(7): grid.columnconfigure(c, weight=1)
#         self.cells: list[list[ttk.Button]] = []
#         for r in range(6):
#             row=[]
#             for c in range(7):
#                 b = ttk.Button(grid, text=" ")
#                 b.grid(row=r, column=c, sticky="nsew", padx=1, pady=1, ipady=6)
#                 b.bind("<Button-1>",  lambda e, rr=r, cc=c: self._select(rr, cc))
#                 b.bind("<Double-1>",  lambda e, rr=r, cc=c: self._dbl(rr, cc))
#                 b.bind("<Button-3>",  lambda e, rr=r, cc=c: self._menu(rr, cc, e))
#                 row.append(b)
#             self.cells.append(row)

#         # Context menu (right-click)
#         self.menu = tk.Menu(self, tearoff=0)
#         self.menu.add_command(label="Add",       command=lambda: self._menu_action("add"))
#         self.menu.add_command(label="View All",  command=lambda: self._menu_action("view"))
#         self.menu.add_separator()
#         self.menu.add_command(label="Quick Delete (all on day)", command=lambda: self._menu_action("del"))

#         self.render_month()

#     # --- Toolbar actions
#     def go_today(self):
#         t = date.today()
#         self.year, self.month, self.selected = t.year, t.month, t
#         self.render_month()

#     def quick_new(self):
#         d = self.selected or date.today()
#         if callable(self.on_quick_new):
#             self.on_quick_new(d)
#         self.selected = d
#         self.render_month()

#     def jump_to(self):
#         try:
#             m = self.MONTHS.index(self.month_var.get()) + 1
#             y = int(self.year_var.get())
#             self.year, self.month, self.selected = y, m, None
#             self.render_month()
#         except Exception:
#             messagebox.showerror("Jump to", "Please choose a valid month and year.")

#     # --- Navigation
#     def prev_month(self):
#         self.month = 12 if self.month == 1 else self.month - 1
#         self.year  = self.year - 1 if self.month == 12 else self.year
#         self.selected = None; self.render_month()

#     def next_month(self):
#         self.month = 1 if self.month == 12 else self.month + 1
#         self.year  = self.year + 1 if self.month == 1 else self.year
#         self.selected = None; self.render_month()

#     # --- Paint month (+ dots + star + today)
#     def render_month(self):
#         self.title.set(date(self.year, self.month, 1).strftime("%B %Y"))
#         weeks = calendar.monthcalendar(self.year, self.month)
#         while len(weeks) < 6: weeks.append([0]*7)
#         today = date.today()
#         badges = set()
#         if callable(self.get_badge_dates):
#             try: badges = set(self.get_badge_dates(self.year, self.month))
#             except Exception: badges = set()

#         self.daymap = {}
#         for r in range(6):
#             for c in range(7):
#                 dnum = weeks[r][c]; btn = self.cells[r][c]
#                 if dnum == 0:
#                     btn.config(text=" ", state="disabled"); self.daymap[(r,c)] = None
#                 else:
#                     d = date(self.year, self.month, dnum)
#                     self.daymap[(r,c)] = d
#                     label = f"{dnum}"
#                     if d == today: label = f"[{dnum}]"
#                     if dnum in badges: label = f"{label} •"
#                     if d == self.selected: label = f"★ {label}"
#                     btn.config(text=label, state="normal")

#     # --- Click handlers
#     def _select(self, r, c):
#         d = self.daymap.get((r,c))
#         if d:
#             self.selected = d
#             self.render_month()

#     def _dbl(self, r, c):
#         d = self.daymap.get((r,c))
#         if d:
#             self.selected = d
#             self.on_day_double(d)
#             self.render_month()

#     def _menu(self, r, c, e):
#         d = self.daymap.get((r,c)); self._menu_target = d
#         if d:
#             self.selected = d
#             self.render_month()
#             self.menu.tk_popup(e.x_root, e.y_root)

#     def _menu_action(self, which: str):
#         d = getattr(self, "_menu_target", None)
#         if not d: return
#         if   which == "add":  self.on_new_event(d)
#         elif which == "view": self.on_view_day(d)
#         elif which == "del":
#             if messagebox.askyesno("Delete", "Delete all events on this day?"):
#                 self.on_day_delete(d)
#         self.selected = d
#         self.render_month()


# # --- Controller ---
# class TimekeeperApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Jedi Timekeeper")
#         self.root.geometry("980x650")

#         self.repo = EventRepository()

#         def get_badge_dates(year: int, month: int) -> set[int]:
#             days = set()
#             for ev in self.repo.by_month(year, month):
#                 try:
#                     days.add(int(ev.start_ts[8:10]))   # 'YYYY-MM-DD...'
#                 except Exception:
#                     pass
#             return days

#         self.view = CalendarView(
#             self.root,
#             on_new_event=self.new_event,
#             on_day_double=self.day_double,
#             on_day_delete=self.day_delete,
#             on_view_day=self.view_day,
#             get_badge_dates=get_badge_dates,
#             on_quick_new=self.quick_new,
#         )
#         self.view.pack(fill="both", expand=True)

#         # --- Shortcuts (controller-level)
#         self.root.bind("<Control-n>",         lambda e: self.quick_new(self.view.selected or date.today()))
#         self.root.bind("<Control-BackSpace>", lambda e: self.quick_delete())
#         self.root.bind("<Control-f>",         lambda e: messagebox.showinfo("Search", "Search arrives in Sprint 5 ⚡"))

#     # New event (dialog)
#     def new_event(self, d: date):
#         dlg = EventDialog(self.root, title="New Event", init=None, date_for_label=d)
#         if not getattr(dlg, "result", None): return
#         hh, mm   = map(int, dlg.result["start_hhmm"].split(":"))
#         hh2, mm2 = map(int, dlg.result["end_hhmm"].split(":"))
#         start = datetime.combine(d, time(hh,mm), tzinfo=UTC).isoformat()
#         end   = datetime.combine(d, time(hh2,mm2), tzinfo=UTC).isoformat()
#         self.repo.add_event(Event(id=None, title=dlg.result["title"], start_ts=start, end_ts=end, notes=dlg.result["notes"]))
#         self.view.selected = d; self.view.render_month()

#     # Quick New (toolbar or Ctrl+N)
#     def quick_new(self, d: date):
#         self.new_event(d)

#     # Double-click → edit existing first event OR add new
#     def day_double(self, d: date):
#         evs = self.repo.by_day(d)
#         init = evs[0] if evs else None
#         dlg = EventDialog(self.root, title=("Edit Event" if init else "New Event"),
#                           init=init, date_for_label=d)
#         if not getattr(dlg, "result", None): return

#         # delete-if-cleared (both raw fields empty)
#         if init and dlg.result.get("raw_title","")=="" and dlg.result.get("raw_notes","")=="":
#             self.repo.delete_event(init.id)
#         else:
#             hh, mm   = map(int, dlg.result["start_hhmm"].split(":"))
#             hh2, mm2 = map(int, dlg.result["end_hhmm"].split(":"))
#             start = datetime.combine(d, time(hh,mm), tzinfo=UTC).isoformat()
#             end   = datetime.combine(d, time(hh2,mm2), tzinfo=UTC).isoformat()
#             if init:
#                 init.title, init.notes = dlg.result["title"], dlg.result["notes"]
#                 init.start_ts, init.end_ts = start, end
#                 self.repo.update_event(init)
#             else:
#                 self.repo.add_event(Event(id=None, title=dlg.result["title"],
#                                           start_ts=start, end_ts=end, notes=dlg.result["notes"]))
#         self.view.selected = d; self.view.render_month()

#     # Right-click → delete all on day
#     def day_delete(self, d: date):
#         for ev in self.repo.by_day(d):
#             self.repo.delete_event(ev.id)
#         self.view.selected = d; self.view.render_month()

#     # Right-click → View All (simple list)
#     def view_day(self, d: date):
#         evs = self.repo.by_day(d)
#         if not evs:
#             messagebox.showinfo("Events", f"No events on {d}."); return
#         lines = [f"{ev.start_ts[11:16]}–{ev.end_ts[11:16]}  {ev.title}" for ev in evs]
#         messagebox.showinfo(d.strftime("%A, %B %d, %Y"), "\n".join(lines))

#     # Ctrl+Backspace helper
#     def quick_delete(self):
#         d = self.view.selected or date.today()
#         if messagebox.askyesno("Delete", f"Delete all events on {d}?"):
#             self.day_delete(d)

#     def run(self):
#         self.root.mainloop()


# if __name__ == "__main__":
#     TimekeeperApp().run()




############################## Sprint 5 #################################

# Jedi_Calendar.p

# import tkinter as tk
# from tkinter import ttk, messagebox
# import calendar
# from datetime import date, datetime, time, UTC

# from repo_concise import EventRepository
# from dialog_event import EventDialog
# from models import Event


# # --- View ---
# class CalendarView(ttk.Frame):
#     """
#     Sprint 5:
#       - Search box filters current month's dots (•) by title/notes
#       - Right-side list shows:
#           * search matches when query present, OR
#           * events for selected day when query empty
#       - Keeps Sprint 4 behavior (single-click select ★, double-click edit/add, right-click menu)
#     """
#     WEEKDAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
#     MONTHS = [calendar.month_name[m] for m in range(1,13)]

#     def __init__(self, master,
#                  on_new_event,
#                  on_day_double,
#                  on_day_delete,
#                  on_view_day,
#                  get_badge_dates,
#                  on_quick_new,          # controller.quick_new
#                  search_month):         # callable(year, month, query) -> list[Event]
#         super().__init__(master, padding=8)
#         self.on_new_event   = on_new_event
#         self.on_day_double  = on_day_double
#         self.on_day_delete  = on_day_delete
#         self.on_view_day    = on_view_day
#         self.get_badge_dates = get_badge_dates
#         self.on_quick_new   = on_quick_new
#         self.search_month   = search_month

#         t = date.today()
#         self.year, self.month = t.year, t.month
#         self.selected: date | None = None

#         # --- Toolbar (Today | New | Jump-to + Search)
#         top = ttk.Frame(self); top.grid(row=0, column=0, sticky="ew", pady=(0,6))
#         top.columnconfigure(3, weight=1)
#         ttk.Button(top, text="Today", width=7, command=self.go_today).grid(row=0, column=0, padx=(0,6))
#         ttk.Button(top, text="New",   width=7, command=self.quick_new).grid(row=0, column=1, padx=(0,12))
#         ttk.Label(top, text="Jump to:").grid(row=0, column=2, padx=(0,4))
#         self.month_var = tk.StringVar(value=calendar.month_name[self.month])
#         self.year_var  = tk.StringVar(value=str(self.year))
#         ttk.Combobox(top, textvariable=self.month_var, values=self.MONTHS, width=11, state="readonly").grid(row=0, column=3, sticky="w")
#         ttk.Spinbox(top, from_=1900, to=3000, textvariable=self.year_var, width=6).grid(row=0, column=4, padx=(6,0))
#         ttk.Button(top, text="Go", width=4, command=self.jump_to).grid(row=0, column=5, padx=(8,12))
#         ttk.Label(top, text="Search:").grid(row=0, column=6, sticky="e", padx=(12,4))
#         self.search_var = tk.StringVar()
#         self.search_entry = ttk.Entry(top, textvariable=self.search_var, width=24)
#         self.search_entry.grid(row=0, column=7, sticky="e")
#         self.search_entry.bind("<KeyRelease>", lambda e: (self.render_month(), self.update_side()))
#         ttk.Button(top, text="Clear", command=lambda: self._clear_search()).grid(row=0, column=8, padx=(6,0))

#         # --- Header: ◀ Month Year ▶
#         hdr = ttk.Frame(self); hdr.grid(row=1, column=0, sticky="ew")
#         hdr.columnconfigure(1, weight=1)
#         ttk.Button(hdr, text="◀", width=3, command=self.prev_month).grid(row=0, column=0)
#         self.title = tk.StringVar()
#         ttk.Label(hdr, textvariable=self.title, font=("Segoe UI", 11, "bold")).grid(row=0, column=1)
#         ttk.Button(hdr, text="▶", width=3, command=self.next_month).grid(row=0, column=2)

#         # --- Main: calendar (left) + list (right)
#         main = ttk.Frame(self); main.grid(row=2, column=0, sticky="nsew")
#         self.columnconfigure(0, weight=1); self.rowconfigure(2, weight=1)
#         main.columnconfigure(0, weight=3); main.columnconfigure(1, weight=2)

#         # Weekdays (flex)
#         wk = ttk.Frame(main); wk.grid(row=0, column=0, sticky="ew", pady=(6, 0))
#         for i, name in enumerate(self.WEEKDAYS):
#             wk.columnconfigure(i, weight=1)
#             ttk.Label(wk, text=name, anchor="center").grid(row=0, column=i, sticky="nsew")

#         # 6x7 grid
#         grid = ttk.Frame(main); grid.grid(row=1, column=0, sticky="nsew", pady=(4,0))
#         for r in range(6): grid.rowconfigure(r, weight=1)
#         for c in range(7): grid.columnconfigure(c, weight=1)
#         self.cells: list[list[ttk.Button]] = []
#         for r in range(6):
#             row=[]
#             for c in range(7):
#                 b = ttk.Button(grid, text=" ")
#                 b.grid(row=r, column=c, sticky="nsew", padx=1, pady=1, ipady=6)
#                 b.bind("<Button-1>",  lambda e, rr=r, cc=c: self._select(rr, cc))
#                 b.bind("<Double-1>",  lambda e, rr=r, cc=c: self._dbl(rr, cc))
#                 b.bind("<Button-3>",  lambda e, rr=r, cc=c: self._menu(rr, cc, e))
#                 row.append(b)
#             self.cells.append(row)

#         # Context menu
#         self.menu = tk.Menu(self, tearoff=0)
#         self.menu.add_command(label="Add",       command=lambda: self._menu_action("add"))
#         self.menu.add_command(label="View All",  command=lambda: self._menu_action("view"))
#         self.menu.add_separator()
#         self.menu.add_command(label="Quick Delete (all on day)", command=lambda: self._menu_action("del"))

#         # Right side list
#         side = ttk.Frame(main); side.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=(8,0))
#         side.rowconfigure(1, weight=1)
#         ttk.Label(side, text="Events", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w")
#         self.listbox = tk.Listbox(side, height=18)
#         self.listbox.grid(row=1, column=0, sticky="nsew")
#         self.listbox.bind("<Double-Button-1>", lambda e: self._open_from_list())

#         self.render_month(); self.update_side()

#     # --- Toolbar / nav
#     def go_today(self):
#         t = date.today()
#         self.year, self.month, self.selected = t.year, t.month, t
#         self.render_month(); self.update_side()

#     def quick_new(self):
#         d = self.selected or date.today()
#         if callable(self.on_quick_new): self.on_quick_new(d)
#         self.selected = d; self.render_month(); self.update_side()

#     def jump_to(self):
#         try:
#             m = self.MONTHS.index(self.month_var.get()) + 1
#             y = int(self.year_var.get())
#             self.year, self.month, self.selected = y, m, None
#             self.render_month(); self.update_side()
#         except Exception:
#             messagebox.showerror("Jump to", "Please choose a valid month and year.")

#     def prev_month(self):
#         self.month = 12 if self.month == 1 else self.month - 1
#         self.year  = self.year - 1 if self.month == 12 else self.year
#         self.selected = None; self.render_month(); self.update_side()

#     def next_month(self):
#         self.month = 1 if self.month == 12 else self.month + 1
#         self.year  = self.year + 1 if self.month == 1 else self.year
#         self.selected = None; self.render_month(); self.update_side()

#     def _clear_search(self):
#         self.search_var.set(""); self.render_month(); self.update_side()

#     # --- Paint month (search-aware dots)
#     def render_month(self):
#         self.title.set(date(self.year, self.month, 1).strftime("%B %Y"))
#         weeks = calendar.monthcalendar(self.year, self.month)
#         while len(weeks) < 6: weeks.append([0]*7)
#         today = date.today()

#         badges = set(self.get_badge_dates(self.year, self.month))
#         q = self.search_var.get().strip()
#         if q:
#             matches = self.search_month(self.year, self.month, q)
#             days_with_matches = {self._iso_day(ev.start_ts) for ev in matches}
#             badges &= days_with_matches

#         self.daymap = {}
#         for r in range(6):
#             for c in range(7):
#                 dnum = weeks[r][c]; btn = self.cells[r][c]
#                 if dnum == 0:
#                     btn.config(text=" ", state="disabled"); self.daymap[(r,c)] = None
#                 else:
#                     d = date(self.year, self.month, dnum)
#                     self.daymap[(r,c)] = d
#                     label = f"{dnum}"
#                     if d == today: label = f"[{dnum}]"
#                     if dnum in badges: label = f"{label} •"
#                     if d == self.selected: label = f"★ {label}"
#                     btn.config(text=label, state="normal")

#     @staticmethod
#     def _iso_day(iso: str) -> int:
#         try:
#             return datetime.fromisoformat(iso.replace("Z","+00:00")).day
#         except Exception:
#             return int(iso[8:10])

#     # --- Side list
#     def update_side(self):
#         self.listbox.delete(0, "end")
#         q = self.search_var.get().strip()

#         def fmt(ev: Event) -> str:
#             return f"{ev.start_ts[11:16]} - {ev.end_ts[11:16]} -- {ev.title}"

#         if q:
#             for ev in self.search_month(self.year, self.month, q):
#                 self.listbox.insert("end", f"{ev.start_ts[:10]} {fmt(ev)}")
#         else:
#             if self.selected:
#                 prefix = self.selected.strftime("%Y-%m-%d")
#                 todays = [ev for ev in self.search_month(self.year, self.month, "")
#                           if ev.start_ts.startswith(prefix)]
#                 for ev in todays:
#                     self.listbox.insert("end", fmt(ev))

#     def _open_from_list(self):
#         sel = self.listbox.curselection()
#         if not sel: return
#         text = self.listbox.get(sel[0])
#         q = self.search_var.get().strip()
#         if q:
#             day = text[:10]
#             try:
#                 y,m,d = map(int, day.split("-"))
#                 self.on_day_double(date(y,m,d))
#             except Exception:
#                 pass
#         else:
#             if self.selected:
#                 self.on_day_double(self.selected)
#         self.render_month(); self.update_side()

#     # --- Clicks
#     def _select(self, r, c):
#         d = self.daymap.get((r,c))
#         if d:
#             self.selected = d
#             self.render_month(); self.update_side()

#     def _dbl(self, r, c):
#         d = self.daymap.get((r,c))
#         if d:
#             self.selected = d
#             self.on_day_double(d)
#             self.render_month(); self.update_side()

#     def _menu(self, r, c, e):
#         d = self.daymap.get((r,c)); self._menu_target = d
#         if d:
#             self.selected = d
#             self.render_month(); self.update_side()
#             self.menu.tk_popup(e.x_root, e.y_root)

#     def _menu_action(self, which: str):
#         d = getattr(self, "_menu_target", None)
#         if not d: return
#         if   which == "add":  self.on_new_event(d)
#         elif which == "view": self.on_view_day(d)
#         elif which == "del":
#             if messagebox.askyesno("Delete", "Delete all events on this day?"):
#                 self.on_day_delete(d)
#         self.selected = d
#         self.render_month(); self.update_side()


# # --- Controller ---
# class TimekeeperApp:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Jedi Timekeeper")
#         self.root.geometry("1100x680")

#         self.repo = EventRepository()

#         def get_badge_dates(year: int, month: int) -> set[int]:
#             days = set()
#             for ev in self.repo.by_month(year, month):
#                 try: days.add(int(ev.start_ts[8:10]))
#                 except Exception: pass
#             return days

#         def search_month(year: int, month: int, query: str) -> list[Event]:
#             q = (query or "").strip().lower()
#             events = self.repo.by_month(year, month)
#             if not q: return events
#             return [ev for ev in events
#                     if q in (ev.title or "").lower() or q in (ev.notes or "").lower()]

#         self.view = CalendarView(
#             self.root,
#             on_new_event=self.new_event,
#             on_day_double=self.day_double,
#             on_day_delete=self.day_delete,
#             on_view_day=self.view_day,
#             get_badge_dates=get_badge_dates,
#             on_quick_new=self.quick_new,      # <-- this exists now
#             search_month=search_month,
#         )
#         self.view.pack(fill="both", expand=True)

#         # Shortcuts
#         self.root.bind("<Control-n>",         lambda e: self.quick_new(self.view.selected or date.today()))
#         self.root.bind("<Control-BackSpace>", lambda e: self.quick_delete())
#         self.root.bind("<Control-f>",         lambda e: self.focus_search())

#     # NEW: quick_new was missing → add it
#     def quick_new(self, d: date):
#         self.new_event(d)

#     def focus_search(self):
#         try:
#             self.view.search_entry.focus_set()
#             self.view.search_entry.select_range(0, "end")
#         except Exception:
#             pass

#     def new_event(self, d: date):
#         dlg = EventDialog(self.root, title="New Event", init=None, date_for_label=d)
#         if not getattr(dlg, "result", None): return
#         hh, mm   = map(int, dlg.result["start_hhmm"].split(":"))
#         hh2, mm2 = map(int, dlg.result["end_hhmm"].split(":"))
#         start = datetime.combine(d, time(hh,mm), tzinfo=UTC).isoformat()
#         end   = datetime.combine(d, time(hh2,mm2), tzinfo=UTC).isoformat()
#         self.repo.add_event(Event(id=None, title=dlg.result["title"], start_ts=start, end_ts=end, notes=dlg.result["notes"]))
#         self.view.selected = d; self.view.render_month(); self.view.update_side()

#     def day_double(self, d: date):
#         evs = self.repo.by_day(d)
#         init = evs[0] if evs else None
#         dlg = EventDialog(self.root, title=("Edit Event" if init else "New Event"),
#                           init=init, date_for_label=d)
#         if not getattr(dlg, "result", None): return

#         if init and dlg.result.get("raw_title","")=="" and dlg.result.get("raw_notes","")=="":
#             self.repo.delete_event(init.id)
#         else:
#             hh, mm   = map(int, dlg.result["start_hhmm"].split(":"))
#             hh2, mm2 = map(int, dlg.result["end_hhmm"].split(":"))
#             start = datetime.combine(d, time(hh,mm), tzinfo=UTC).isoformat()
#             end   = datetime.combine(d, time(hh2,mm2), tzinfo=UTC).isoformat()
#             if init:
#                 init.title, init.notes = dlg.result["title"], dlg.result["notes"]
#                 init.start_ts, init.end_ts = start, end
#                 self.repo.update_event(init)
#             else:
#                 self.repo.add_event(Event(id=None, title=dlg.result["title"],
#                                           start_ts=start, end_ts=end, notes=dlg.result["notes"]))
#         self.view.selected = d; self.view.render_month(); self.view.update_side()

#     def day_delete(self, d: date):
#         for ev in self.repo.by_day(d):
#             self.repo.delete_event(ev.id)
#         self.view.selected = d; self.view.render_month(); self.view.update_side()

#     def view_day(self, d: date):
#         evs = self.repo.by_day(d)
#         if not evs:
#             messagebox.showinfo("Events", f"No events on {d}."); return
#         lines = [f"{ev.start_ts[11:16]}–{ev.end_ts[11:16]}  {ev.title}" for ev in evs]
#         messagebox.showinfo(d.strftime("%A, %B %d, %Y"), "\n".join(lines))

#     def quick_delete(self):
#         d = self.view.selected or date.today()
#         if messagebox.askyesno("Delete", f"Delete all events on {d}?"):
#             self.day_delete(d)

#     def run(self):
#         self.root.mainloop()


# if __name__ == "__main__":
#     TimekeeperApp().run()





################################### Sprint 6 #####################################


# Jedi_Calendar.py — Sprint 6 (Export CSV + Backup DB)

import tkinter as tk
from tkinter import ttk, messagebox
import calendar, csv, shutil
from pathlib import Path
from datetime import date, datetime, time, UTC

from repo_concise import EventRepository
from dialog_event import EventDialog
from models import Event


# --- View ---
class CalendarView(ttk.Frame):
    """
    Sprint 6:
      - Adds Export CSV & Backup buttons to the toolbar
      - Keeps Sprint 5 search/dots/side-list and Sprint 4 clicks/menu
    """
    WEEKDAYS = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    MONTHS = [calendar.month_name[m] for m in range(1,13)]

    def __init__(self, master,
                 on_new_event, on_day_double, on_day_delete, on_view_day,
                 get_badge_dates, on_quick_new, search_month,
                 on_export_csv, on_backup_db):
        super().__init__(master, padding=8)
        self.on_new_event   = on_new_event
        self.on_day_double  = on_day_double
        self.on_day_delete  = on_day_delete
        self.on_view_day    = on_view_day
        self.get_badge_dates = get_badge_dates
        self.on_quick_new   = on_quick_new
        self.search_month   = search_month
        self.on_export_csv  = on_export_csv
        self.on_backup_db   = on_backup_db

        t = date.today()
        self.year, self.month = t.year, t.month
        self.selected: date | None = None

        # --- Toolbar (Today | New | Jump-to + Search + Export + Backup)
        top = ttk.Frame(self); top.grid(row=0, column=0, sticky="ew", pady=(0,6))
        top.columnconfigure(3, weight=1)
        ttk.Button(top, text="Today", width=7, command=self.go_today).grid(row=0, column=0, padx=(0,6))
        ttk.Button(top, text="New",   width=7, command=self.quick_new).grid(row=0, column=1, padx=(0,12))
        ttk.Label(top, text="Jump to:").grid(row=0, column=2, padx=(0,4))
        self.month_var = tk.StringVar(value=calendar.month_name[self.month])
        self.year_var  = tk.StringVar(value=str(self.year))
        ttk.Combobox(top, textvariable=self.month_var, values=self.MONTHS, width=11, state="readonly").grid(row=0, column=3, sticky="w")
        ttk.Spinbox(top, from_=1900, to=3000, textvariable=self.year_var, width=6).grid(row=0, column=4, padx=(6,0))
        ttk.Button(top, text="Go", width=4, command=self.jump_to).grid(row=0, column=5, padx=(8,12))

        ttk.Label(top, text="Search:").grid(row=0, column=6, sticky="e", padx=(12,4))
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(top, textvariable=self.search_var, width=24)
        self.search_entry.grid(row=0, column=7, sticky="e")
        self.search_entry.bind("<KeyRelease>", lambda e: (self.render_month(), self.update_side()))
        ttk.Button(top, text="Clear", command=lambda: self._clear_search()).grid(row=0, column=8, padx=(6,0))

        ttk.Button(top, text="Export CSV", command=lambda: self.on_export_csv(self.year, self.month)).grid(row=0, column=9, padx=(8,6))
        ttk.Button(top, text="Backup",     command=self.on_backup_db).grid(row=0, column=10)

        # --- Header: ◀ Month Year ▶
        hdr = ttk.Frame(self); hdr.grid(row=1, column=0, sticky="ew")
        hdr.columnconfigure(1, weight=1)
        ttk.Button(hdr, text="◀", width=3, command=self.prev_month).grid(row=0, column=0)
        self.title = tk.StringVar()
        ttk.Label(hdr, textvariable=self.title, font=("Segoe UI", 11, "bold")).grid(row=0, column=1)
        ttk.Button(hdr, text="▶", width=3, command=self.next_month).grid(row=0, column=2)

        # --- Main: calendar (left) + list (right)
        main = ttk.Frame(self); main.grid(row=2, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1); self.rowconfigure(2, weight=1)
        main.columnconfigure(0, weight=3); main.columnconfigure(1, weight=2)

        # Weekdays
        wk = ttk.Frame(main); wk.grid(row=0, column=0, sticky="ew", pady=(6, 0))
        for i, name in enumerate(self.WEEKDAYS):
            wk.columnconfigure(i, weight=1)
            ttk.Label(wk, text=name, anchor="center").grid(row=0, column=i, sticky="nsew")

        # 6x7 grid
        grid = ttk.Frame(main); grid.grid(row=1, column=0, sticky="nsew", pady=(4,0))
        for r in range(6): grid.rowconfigure(r, weight=1)
        for c in range(7): grid.columnconfigure(c, weight=1)
        self.cells: list[list[ttk.Button]] = []
        for r in range(6):
            row=[]
            for c in range(7):
                b = ttk.Button(grid, text=" ")
                b.grid(row=r, column=c, sticky="nsew", padx=1, pady=1, ipady=6)
                b.bind("<Button-1>",  lambda e, rr=r, cc=c: self._select(rr, cc))
                b.bind("<Double-1>",  lambda e, rr=r, cc=c: self._dbl(rr, cc))
                b.bind("<Button-3>",  lambda e, rr=r, cc=c: self._menu(rr, cc, e))
                row.append(b)
            self.cells.append(row)

        # Context menu
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label="Add",       command=lambda: self._menu_action("add"))
        self.menu.add_command(label="View All",  command=lambda: self._menu_action("view"))
        self.menu.add_separator()
        self.menu.add_command(label="Quick Delete (all on day)", command=lambda: self._menu_action("del"))

        # Right side list
        side = ttk.Frame(main); side.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=(8,0))
        side.rowconfigure(1, weight=1)
        ttk.Label(side, text="Events", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w")
        self.listbox = tk.Listbox(side, height=18)
        self.listbox.grid(row=1, column=0, sticky="nsew")
        self.listbox.bind("<Double-Button-1>", lambda e: self._open_from_list())

        self.render_month(); self.update_side()

    # --- Toolbar / nav
    def go_today(self):
        t = date.today()
        self.year, self.month, self.selected = t.year, t.month, t
        self.render_month(); self.update_side()

    def quick_new(self):
        d = self.selected or date.today()
        if callable(self.on_quick_new): self.on_quick_new(d)
        self.selected = d; self.render_month(); self.update_side()

    def jump_to(self):
        try:
            m = self.MONTHS.index(self.month_var.get()) + 1
            y = int(self.year_var.get())
            self.year, self.month, self.selected = y, m, None
            self.render_month(); self.update_side()
        except Exception:
            messagebox.showerror("Jump to", "Please choose a valid month and year.")

    def prev_month(self):
        self.month = 12 if self.month == 1 else self.month - 1
        self.year  = self.year - 1 if self.month == 12 else self.year
        self.selected = None; self.render_month(); self.update_side()

    def next_month(self):
        self.month = 1 if self.month == 12 else self.month + 1
        self.year  = self.year + 1 if self.month == 1 else self.year
        self.selected = None; self.render_month(); self.update_side()

    def _clear_search(self):
        self.search_var.set(""); self.render_month(); self.update_side()

    # --- Paint month (search-aware dots)
    def render_month(self):
        self.title.set(date(self.year, self.month, 1).strftime("%B %Y"))
        weeks = calendar.monthcalendar(self.year, self.month)
        while len(weeks) < 6: weeks.append([0]*7)
        today = date.today()

        badges = set(self.get_badge_dates(self.year, self.month))
        q = self.search_var.get().strip()
        if q:
            matches = self.search_month(self.year, self.month, q)
            days_with_matches = {self._iso_day(ev.start_ts) for ev in matches}
            badges &= days_with_matches

        self.daymap = {}
        for r in range(6):
            for c in range(7):
                dnum = weeks[r][c]; btn = self.cells[r][c]
                if dnum == 0:
                    btn.config(text=" ", state="disabled"); self.daymap[(r,c)] = None
                else:
                    d = date(self.year, self.month, dnum)
                    self.daymap[(r,c)] = d
                    label = f"{dnum}"
                    if d == today: label = f"[{dnum}]"
                    if dnum in badges: label = f"{label} •"
                    if d == self.selected: label = f"★ {label}"
                    btn.config(text=label, state="normal")

    @staticmethod
    def _iso_day(iso: str) -> int:
        try:
            return datetime.fromisoformat(iso.replace("Z","+00:00")).day
        except Exception:
            return int(iso[8:10])

    # --- Side list
    def update_side(self):
        self.listbox.delete(0, "end")
        q = self.search_var.get().strip()

        def fmt(ev: Event) -> str:
            return f"{ev.start_ts[11:16]} - {ev.end_ts[11:16]} -- {ev.title}"

        if q:
            for ev in self.search_month(self.year, self.month, q):
                self.listbox.insert("end", f"{ev.start_ts[:10]} {fmt(ev)}")
        else:
            if self.selected:
                prefix = self.selected.strftime("%Y-%m-%d")
                todays = [ev for ev in self.search_month(self.year, self.month, "")
                          if ev.start_ts.startswith(prefix)]
                for ev in todays:
                    self.listbox.insert("end", fmt(ev))

    def _open_from_list(self):
        sel = self.listbox.curselection()
        if not sel: return
        text = self.listbox.get(sel[0])
        q = self.search_var.get().strip()
        if q:
            day = text[:10]
            try:
                y,m,d = map(int, day.split("-"))
                self.on_day_double(date(y,m,d))
            except Exception:
                pass
        else:
            if self.selected: self.on_day_double(self.selected)
        self.render_month(); self.update_side()

    # --- Clicks
    def _select(self, r, c):
        d = self.daymap.get((r,c))
        if d: self.selected = d; self.render_month(); self.update_side()

    def _dbl(self, r, c):
        d = self.daymap.get((r,c))
        if d: self.selected = d; self.on_day_double(d); self.render_month(); self.update_side()

    def _menu(self, r, c, e):
        d = self.daymap.get((r,c)); self._menu_target = d
        if d:
            self.selected = d; self.render_month(); self.update_side()
            self.menu.tk_popup(e.x_root, e.y_root)

    def _menu_action(self, which: str):
        d = getattr(self, "_menu_target", None)
        if not d: return
        if   which == "add":  self.on_new_event(d)
        elif which == "view": self.on_view_day(d)
        elif which == "del":
            if messagebox.askyesno("Delete", "Delete all events on this day?"):
                self.on_day_delete(d)
        self.selected = d; self.render_month(); self.update_side()


# --- Controller ---
class TimekeeperApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jedi Timekeeper")
        self.root.geometry("1120x700")

        self.repo = EventRepository()

        def get_badge_dates(year: int, month: int) -> set[int]:
            days = set()
            for ev in self.repo.by_month(year, month):
                try: days.add(int(ev.start_ts[8:10]))
                except Exception: pass
            return days

        def search_month(year: int, month: int, query: str) -> list[Event]:
            q = (query or "").strip().lower()
            events = self.repo.by_month(year, month)
            if not q: return events
            return [ev for ev in events if q in (ev.title or "").lower()
                                   or q in (ev.notes or "").lower()]

        self.view = CalendarView(
            self.root,
            on_new_event=self.new_event,
            on_day_double=self.day_double,
            on_day_delete=self.day_delete,
            on_view_day=self.view_day,
            get_badge_dates=get_badge_dates,
            on_quick_new=self.quick_new,
            search_month=search_month,
            on_export_csv=self.export_csv,
            on_backup_db=self.backup_db,
        )
        self.view.pack(fill="both", expand=True)

        # Shortcuts
        self.root.bind("<Control-n>",         lambda e: self.quick_new(self.view.selected or date.today()))
        self.root.bind("<Control-BackSpace>", lambda e: self.quick_delete())
        self.root.bind("<Control-f>",         lambda e: self.focus_search())

    def quick_new(self, d: date):  # reuse dialog flow
        self.new_event(d)

    def focus_search(self):
        try:
            self.view.search_entry.focus_set()
            self.view.search_entry.select_range(0, "end")
        except Exception:
            pass

    # --- Add / Edit / Delete (unchanged from Sprint 5)
    def new_event(self, d: date):
        dlg = EventDialog(self.root, title="New Event", init=None, date_for_label=d)
        if not getattr(dlg, "result", None): return
        hh, mm   = map(int, dlg.result["start_hhmm"].split(":"))
        hh2, mm2 = map(int, dlg.result["end_hhmm"].split(":"))
        start = datetime.combine(d, time(hh,mm), tzinfo=UTC).isoformat()
        end   = datetime.combine(d, time(hh2,mm2), tzinfo=UTC).isoformat()
        self.repo.add_event(Event(id=None, title=dlg.result["title"], start_ts=start, end_ts=end, notes=dlg.result["notes"]))
        self.view.selected = d; self.view.render_month(); self.view.update_side()

    def day_double(self, d: date):
        evs = self.repo.by_day(d)
        init = evs[0] if evs else None
        dlg = EventDialog(self.root, title=("Edit Event" if init else "New Event"),
                          init=init, date_for_label=d)
        if not getattr(dlg, "result", None): return

        # delete-if-cleared (both raw fields empty)
        if init and dlg.result.get("raw_title","")=="" and dlg.result.get("raw_notes","")=="":
            self.repo.delete_event(init.id)
        else:
            hh, mm   = map(int, dlg.result["start_hhmm"].split(":"))
            hh2, mm2 = map(int, dlg.result["end_hhmm"].split(":"))
            start = datetime.combine(d, time(hh,mm), tzinfo=UTC).isoformat()
            end   = datetime.combine(d, time(hh2,mm2), tzinfo=UTC).isoformat()
            if init:
                init.title, init.notes = dlg.result["title"], dlg.result["notes"]
                init.start_ts, init.end_ts = start, end
                self.repo.update_event(init)
            else:
                self.repo.add_event(Event(id=None, title=dlg.result["title"],
                                          start_ts=start, end_ts=end, notes=dlg.result["notes"]))
        self.view.selected = d; self.view.render_month(); self.view.update_side()

    def day_delete(self, d: date):
        for ev in self.repo.by_day(d):
            self.repo.delete_event(ev.id)
        self.view.selected = d; self.view.render_month(); self.view.update_side()

    def quick_delete(self):
        d = self.view.selected or date.today()
        if messagebox.askyesno("Delete", f"Delete all events on {d}?"):
            self.day_delete(d)

    def view_day(self, d: date):
        evs = self.repo.by_day(d)
        if not evs:
            messagebox.showinfo("Events", f"No events on {d}."); return
        lines = [f"{ev.start_ts[11:16]}–{ev.end_ts[11:16]}  {ev.title}" for ev in evs]
        messagebox.showinfo(d.strftime("%A, %B %d, %Y"), "\n".join(lines))

    # --- Sprint 6: Export + Backup
    def export_csv(self, year: int, month: int):
        rows = self.repo.by_month(year, month)
        outdir = Path("exports"); outdir.mkdir(parents=True, exist_ok=True)
        path = outdir / f"events_{year:04d}_{month:02d}.csv"
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["id","title","start_ts","end_ts","notes","created_at"])
            for ev in rows:
                w.writerow([ev.id, ev.title, ev.start_ts, ev.end_ts, ev.notes, ev.created_at or ""])
        messagebox.showinfo("Export CSV", f"Saved:\n{path}")

    def backup_db(self):
        src = Path(self.repo.db_path)
        if not src.exists():
            messagebox.showwarning("Backup", "No database file found yet."); return
        ts = datetime.now().strftime("%Y%m%d_%H%M")
        outdir = Path("backups"); outdir.mkdir(parents=True, exist_ok=True)
        dst = outdir / f"events_{ts}.db"
        shutil.copy2(src, dst)
        messagebox.showinfo("Backup", f"Copied DB to:\n{dst}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    TimekeeperApp().run()
