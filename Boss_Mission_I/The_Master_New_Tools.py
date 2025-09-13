
import sqlite3
from datetime import datetime, UTC

class EventRepository:
    """The complete SQLite repo for the Jedi Timekeeper with full data manipulation."""

    def __init__(self, db_path="events.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        
        # Applying Constraints: The CREATE TABLE command is now more disciplined with a CHECK constraint.
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
        
        # Creating an Index: This index will make lookups on 'start_ts' lightning-fast.
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

    def update_event(self, event_id: int, title: str | None = None,
                     start_ts: str | None = None, end_ts: str | None = None,
                     notes: str | None = None) -> bool:
        """Update an event by id. Returns True if updated, False otherwise."""
        updates = []
        params = []

        if title is not None:
            updates.append("title = ?")
            params.append(title)
        if start_ts is not None:
            updates.append("start_ts = ?")
            params.append(start_ts)
        if end_ts is not None:
            updates.append("end_ts = ?")
            params.append(end_ts)
        if notes is not None:
            updates.append("notes = ?")
            params.append(notes)

        if not updates:
            return False

        sql = f"UPDATE events SET {', '.join(updates)} WHERE id = ?"
        params.append(event_id)
        
        cur = self.conn.execute(sql, tuple(params))
        self.conn.commit()
        return cur.rowcount > 0

    def delete_event(self, event_id: int) -> bool:
        """Delete an event by id. Returns True if deleted, False otherwise."""
        cur = self.conn.execute("DELETE FROM events WHERE id = ?", (event_id,))
        self.conn.commit()
        return cur.rowcount > 0

    def search_events(self, query: str) -> list[dict]:
        """Search for events by title or notes using a keyword query."""
        search_term = f"%{query}%"
        rows = self.conn.execute(
            "SELECT * FROM events WHERE title LIKE ? OR notes LIKE ?",
            (search_term, search_term)
        ).fetchall()
        return [dict(r) for r in rows]

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
        This query leverages the 'idx_events_start_ts' index for speed.
        """
        prefix = f"{year:04d}-{month:02d}-"
        rows = self.conn.execute(
            "SELECT * FROM events WHERE start_ts LIKE ? ORDER BY start_ts",
            (prefix + "%",)
        ).fetchall()
        return [dict(r) for r in rows]

    def close(self) -> None:
        self.conn.close()

# --- The Ultimate Proving Ground: Testing all methods ---
if __name__ == "__main__":
    repo = EventRepository()
    
    # Clean the slate for a fresh test run
    repo.conn.execute("DELETE FROM events")
    repo.conn.commit()

    # Add a set of events for testing
    print("--- Adding a set of events for testing ---")
    event1_id = repo.add_event(
        "Meditate on the Force",
        "2025-09-06T09:00:00+00:00",
        "2025-09-06T10:00:00+00:00",
        notes="A deep meditation to center the mind."
    )
    event2_id = repo.add_event(
        "Study ancient texts",
        "2025-09-07T14:00:00+00:00",
        "2025-09-07T16:00:00+00:00",
        notes="Research the history of the Sith."
    )
    event3_id = repo.add_event(
        "Saber training",
        "2025-09-06T11:00:00+00:00",
        "2025-09-06T12:00:00+00:00",
        notes="Practice defense techniques."
    )
    print("Events added.\n")

    # Test 1: Search for an event    
    print("--- Testing the new search_events method ---")
    search_results = repo.search_events("meditation")
    print(f"Found {len(search_results)} event(s) for 'meditation':")
    for e in search_results:
        print(f"  ID={e['id']} | {e['title']} → {e['notes']}")
    print("")

    # Test 2: Update an event
    print("--- Testing the new update_event method ---")
    is_updated = repo.update_event(event3_id, title="Advanced Saber Forms")
    print(f"Update successful: {is_updated}")
    updated_event = repo.get_event(event3_id)
    print(f"Updated event: {updated_event['title']}\n")

    # Test 3: Delete an event
    print("--- Testing the new delete_event method ---")
    is_deleted = repo.delete_event(event1_id)
    print(f"Deletion successful: {is_deleted}\n")
    
    # Final check of all events
    
    print("--- Final state of the Timekeeper's archive ---")
    all_events = repo.get_all_events()
    print(f"Total events remaining: {len(all_events)}")
    for e in all_events:
        print(f"  ID={e['id']} | {e['start_ts']} → {e['title']}")

    repo.close()
