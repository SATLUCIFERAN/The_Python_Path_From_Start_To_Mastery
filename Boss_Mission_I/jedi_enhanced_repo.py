import sqlite3
from datetime import datetime, UTC

class EventRepository:
    """Enhanced SQLite repo for the Jedi Timekeeper with constraints and indexes."""

    def __init__(self, db_path="events.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        
        # 1. Applying Constraints
        # The CREATE TABLE command is now more disciplined with a CHECK constraint.
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY,
                title      TEXT NOT NULL CHECK(length(title) > 0),
                start_ts   TEXT NOT NULL,
                end_ts     TEXT NOT NULL,
                notes      TEXT,
                created_at TEXT NOT NULL
            )
        """)
        
        # 2. Creating an Index
        # This index will make lookups on 'start_ts' lightning-fast.
        self.conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_events_start_ts ON events(start_ts);
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

    def events_by_month(self, year: int, month: int) -> list[dict]:
        """
        Fetch all events for a given month and year.
        This query leverages the new 'idx_events_start_ts' index for speed.
        """
        prefix = f"{year:04d}-{month:02d}-"
        rows = self.conn.execute(
            "SELECT * FROM events WHERE start_ts LIKE ? ORDER BY start_ts",
            (prefix + "%",)
        ).fetchall()
        return [dict(r) for r in rows]

    def close(self) -> None:
        self.conn.close()

# --- Quick smoke test ---
if __name__ == "__main__":
    repo = EventRepository()
    
    # Test 1: Add a valid event    
    print("--- Testing valid event addition ---")
    eid = repo.add_event(
        "Meditate on the Force",
        "2025-09-06T09:00:00+00:00",
        "2025-09-06T10:00:00+00:00",
        notes="A deep meditation to center the mind."
    )
    print(f"Added event ID: {eid}\n")
    
    # Test 2: Prove the CHECK constraint works    
    print("--- Testing the CHECK constraint ---")
    try:
        repo.add_event("", "2025-09-06T11:00:00+00:00", 
                       "2025-09-06T12:00:00+00:00")
    except sqlite3.IntegrityError as e:
        print(f"Failed to add event as expected: {e}\n")

    # Test 3: Prove the INDEX works with a new method
    
    print("--- Testing the new events_by_month method (with index) ---")
    events_in_september = repo.events_by_month(2025, 9)
    print(f"Found {len(events_in_september)} events in September 2025:")
    for e in events_in_september:
        print(f"  ID={e['id']} | {e['start_ts']} → {e['title']}")

    repo.close()
