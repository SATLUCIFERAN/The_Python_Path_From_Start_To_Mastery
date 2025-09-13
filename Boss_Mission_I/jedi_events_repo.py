# repo_concise.py
import sqlite3
from datetime import datetime, UTC

class EventRepository:
    

    def __init__(self, db_path="events.db"):
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

    def add_event(self, title: str, start_ts: str, end_ts: str, notes: str = "") -> int:
        """Insert an event. Timestamps are ISO strings. Returns new id."""
        created_at = datetime.now(UTC).isoformat()
        cur = self.conn.execute(
            "INSERT INTO events(title,start_ts,end_ts,notes,created_at) VALUES(?,?,?,?,?)",
            (title, start_ts, end_ts, notes, created_at)
        )
        self.conn.commit()
        return cur.lastrowid

    def get_event(self, event_id: int) -> dict | None:
        """Fetch one event by id (dict) or None if not found."""
        row = self.conn.execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
        return dict(row) if row else None

    def get_all_events(self) -> list[dict]:
        """Fetch all events ordered by start time (list of dicts)."""
        rows = self.conn.execute("SELECT * FROM events ORDER BY start_ts").fetchall()
        return [dict(r) for r in rows]

    def close(self) -> None:
        self.conn.close()

# --- Quick smoke test ---
if __name__ == "__main__":
    repo = EventRepository()
    eid = repo.add_event(
        "Meditate on the Force",
        "2025-09-06T09:00:00+00:00",
        "2025-09-06T10:00:00+00:00",
        notes="A deep meditation to center the mind."
    )
    print(f"Added event ID: {eid}")
    print("Fetch one:", repo.get_event(eid))
    print("All events:")
    for e in repo.get_all_events():
        print(f"  ID={e['id']} | {e['start_ts']} → {e['title']}")
    repo.close()
