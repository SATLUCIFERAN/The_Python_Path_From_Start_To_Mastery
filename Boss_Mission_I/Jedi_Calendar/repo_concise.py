# repo_concise.py
# import sqlite3
# from datetime import datetime, UTC
# from models import Event

# class EventRepository:
    
#     def __init__(self, db_path="events.db"):
#         self.conn = sqlite3.connect(db_path)
#         self.conn.row_factory = sqlite3.Row
#         self.conn.execute("""
#             CREATE TABLE IF NOT EXISTS events (
#                 id INTEGER PRIMARY KEY,
#                 title      TEXT NOT NULL,
#                 start_ts   TEXT NOT NULL,
#                 end_ts     TEXT NOT NULL,
#                 notes      TEXT,
#                 created_at TEXT NOT NULL
#             )
#         """)
#         self.conn.commit()
#     def _row_to_event(self, row: sqlite3.Row) -> Event:
#         return Event(**dict(row))
#     def add_event(self, ev: Event) -> int:
#         """Insert an Event; returns new id. Fills created_at if missing."""
#         created = ev.created_at or datetime.now(UTC).isoformat()
#         cur = self.conn.execute(
#             "INSERT INTO events(title,start_ts,end_ts,notes,created_at) VALUES(?,?,?,?,?)",
#             (ev.title, ev.start_ts, ev.end_ts, ev.notes, created)
#         )
#         self.conn.commit()
#         return cur.lastrowid
#     def get_event(self, event_id: int) -> Event | None:
#         row = self.conn.execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
#         return self._row_to_event(row) if row else None
#     def get_all_events(self) -> list[Event]:
#         rows = self.conn.execute("SELECT * FROM events ORDER BY start_ts").fetchall()
#         return [self._row_to_event(r) for r in rows]
#     def close(self) -> None:
#         self.conn.close()





####################### Sprint 2  ############################

# import sqlite3
# from datetime import datetime, date, timedelta, UTC
# from models import Event

# class EventRepository:
#     def __init__(self, db_path="events.db"):
#         self.conn = sqlite3.connect(db_path)
#         self.conn.row_factory = sqlite3.Row
#         self.conn.execute("""
#             CREATE TABLE IF NOT EXISTS events (
#                 id INTEGER PRIMARY KEY,
#                 title      TEXT NOT NULL,
#                 start_ts   TEXT NOT NULL,  -- ISO 8601 with timezone
#                 end_ts     TEXT NOT NULL,
#                 notes      TEXT,
#                 created_at TEXT NOT NULL
#             )
#         """)
#         self.conn.commit()

#     def _row_to_event(self, row: sqlite3.Row) -> Event:
#         return Event(**dict(row))

#     # --- CRUD ---
#     def add_event(self, ev: Event) -> int:
#         created = ev.created_at or datetime.now(UTC).isoformat()
#         cur = self.conn.execute(
#             "INSERT INTO events(title,start_ts,end_ts,notes,created_at) VALUES(?,?,?,?,?)",
#             (ev.title, ev.start_ts, ev.end_ts, ev.notes, created)
#         )
#         self.conn.commit()
#         return cur.lastrowid

#     def update_event(self, ev: Event) -> None:
#         if ev.id is None:
#             raise ValueError("update_event requires ev.id")
#         self.conn.execute(
#             "UPDATE events SET title=?, start_ts=?, end_ts=?, notes=? WHERE id=?",
#             (ev.title, ev.start_ts, ev.end_ts, ev.notes, ev.id)
#         )
#         self.conn.commit()

#     def delete_event(self, event_id: int) -> None:
#         self.conn.execute("DELETE FROM events WHERE id=?", (event_id,))
#         self.conn.commit()

#     # --- Reads ---
#     def get_event(self, event_id: int) -> Event | None:
#         row = self.conn.execute("SELECT * FROM events WHERE id=?", (event_id,)).fetchone()
#         return self._row_to_event(row) if row else None

#     def get_all_events(self) -> list[Event]:
#         rows = self.conn.execute("SELECT * FROM events ORDER BY start_ts").fetchall()
#         return [self._row_to_event(r) for r in rows]

#     def by_month(self, year: int, month: int) -> list[Event]:        
#         if month == 12: y2, m2 = year + 1, 1
#         else:           y2, m2 = year, month + 1
#         start = f"{year:04d}-{month:02d}-01T00:00:00+00:00"
#         end   = f"{y2:04d}-{m2:02d}-01T00:00:00+00:00"
#         rows = self.conn.execute(
#             "SELECT * FROM events WHERE start_ts >= ? AND start_ts < ? ORDER BY start_ts",
#             (start, end)
#         ).fetchall()
#         return [self._row_to_event(r) for r in rows]

#     def by_day(self, d: date) -> list[Event]:
#         start = f"{d:%Y-%m-%d}T00:00:00+00:00"
#         end_d = d + timedelta(days=1)
#         end   = f"{end_d:%Y-%m-%d}T00:00:00+00:00"
#         rows = self.conn.execute(
#             "SELECT * FROM events WHERE start_ts >= ? AND start_ts < ? ORDER BY start_ts",
#             (start, end)
#         ).fetchall()
#         return [self._row_to_event(r) for r in rows]

#     def close(self) -> None:
#         self.conn.close()





###################################### Sprint 3 #######################################


# repo_concise.py — Sprint 3 

# import sqlite3
# from datetime import datetime, date, timedelta, UTC
# from models import Event

# class EventRepository:
#     def __init__(self, db_path="events.db"):
#         self.conn = sqlite3.connect(db_path)
#         self.conn.row_factory = sqlite3.Row
#         self.conn.execute("""
#             CREATE TABLE IF NOT EXISTS events (
#                 id INTEGER PRIMARY KEY,
#                 title      TEXT NOT NULL,
#                 start_ts   TEXT NOT NULL,
#                 end_ts     TEXT NOT NULL,
#                 notes      TEXT,
#                 created_at TEXT NOT NULL
#             )
#         """)
#         self.conn.commit()

#     def _row_to_event(self, row: sqlite3.Row) -> Event:
#         return Event(**dict(row))

#     # CRUD
#     def add_event(self, ev: Event) -> int:
#         created = ev.created_at or datetime.now(UTC).isoformat()
#         cur = self.conn.execute(
#             "INSERT INTO events(title,start_ts,end_ts,notes,created_at) VALUES(?,?,?,?,?)",
#             (ev.title, ev.start_ts, ev.end_ts, ev.notes, created)
#         )
#         self.conn.commit()
#         return cur.lastrowid

#     def update_event(self, ev: Event) -> None:
#         if ev.id is None: raise ValueError("update_event requires ev.id")
#         self.conn.execute(
#             "UPDATE events SET title=?, start_ts=?, end_ts=?, notes=? WHERE id=?",
#             (ev.title, ev.start_ts, ev.end_ts, ev.notes, ev.id)
#         )
#         self.conn.commit()

#     def delete_event(self, event_id: int) -> None:
#         self.conn.execute("DELETE FROM events WHERE id=?", (event_id,))
#         self.conn.commit()

#     # Reads
#     def by_month(self, year: int, month: int) -> list[Event]:
#         if month == 12: y2, m2 = year + 1, 1
#         else:           y2, m2 = year, month + 1
#         start = f"{year:04d}-{month:02d}-01T00:00:00+00:00"
#         end   = f"{y2:04d}-{m2:02d}-01T00:00:00+00:00"
#         rows = self.conn.execute(
#             "SELECT * FROM events WHERE start_ts >= ? AND start_ts < ? ORDER BY start_ts",
#             (start, end)
#         ).fetchall()
#         return [self._row_to_event(r) for r in rows]

#     def by_day(self, d: date) -> list[Event]:
#         start = f"{d:%Y-%m-%d}T00:00:00+00:00"
#         end_d = d + timedelta(days=1)
#         end   = f"{end_d:%Y-%m-%d}T00:00:00+00:00"
#         rows = self.conn.execute(
#             "SELECT * FROM events WHERE start_ts >= ? AND start_ts < ? ORDER BY start_ts",
#             (start, end)
#         ).fetchall()
#         return [self._row_to_event(r) for r in rows]

#     def close(self) -> None:
#         self.conn.close()




################################### Sprint 6 ###########################

# repo_concise.py — Sprint 6 (adds .db_path attribute for backup)

import sqlite3
from datetime import datetime, date, timedelta, UTC
from models import Event

class EventRepository:
    def __init__(self, db_path="events.db"):
        self.db_path = db_path                 # NEW: expose path for backup
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY,
                title      TEXT NOT NULL,
                start_ts   TEXT NOT NULL,
                end_ts     TEXT NOT NULL,
                notes      TEXT,
                created_at TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def _row_to_event(self, row: sqlite3.Row) -> Event:
        return Event(**dict(row))

    # CRUD
    def add_event(self, ev: Event) -> int:
        created = ev.created_at or datetime.now(UTC).isoformat()
        cur = self.conn.execute(
            "INSERT INTO events(title,start_ts,end_ts,notes,created_at) VALUES(?,?,?,?,?)",
            (ev.title, ev.start_ts, ev.end_ts, ev.notes, created)
        )
        self.conn.commit()
        return cur.lastrowid

    def update_event(self, ev: Event) -> None:
        if ev.id is None: raise ValueError("update_event requires ev.id")
        self.conn.execute(
            "UPDATE events SET title=?, start_ts=?, end_ts=?, notes=? WHERE id=?",
            (ev.title, ev.start_ts, ev.end_ts, ev.notes, ev.id)
        )
        self.conn.commit()

    def delete_event(self, event_id: int) -> None:
        self.conn.execute("DELETE FROM events WHERE id=?", (event_id,))
        self.conn.commit()

    # Reads
    def by_month(self, year: int, month: int) -> list[Event]:
        if month == 12: y2, m2 = year + 1, 1
        else:           y2, m2 = year, month + 1
        start = f"{year:04d}-{month:02d}-01T00:00:00+00:00"
        end   = f"{y2:04d}-{m2:02d}-01T00:00:00+00:00"
        rows = self.conn.execute(
            "SELECT * FROM events WHERE start_ts >= ? AND start_ts < ? ORDER BY start_ts",
            (start, end)
        ).fetchall()
        return [self._row_to_event(r) for r in rows]

    def by_day(self, d: date) -> list[Event]:
        start = f"{d:%Y-%m-%d}T00:00:00+00:00"
        end_d = d.replace(day=d.day) + timedelta(days=1)
        end   = f"{end_d:%Y-%m-%d}T00:00:00+00:00"
        rows = self.conn.execute(
            "SELECT * FROM events WHERE start_ts >= ? AND start_ts < ? ORDER BY start_ts",
            (start, end)
        ).fetchall()
        return [self._row_to_event(r) for r in rows]

    def close(self) -> None:
        self.conn.close()

