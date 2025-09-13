
# models.py
from dataclasses import dataclass

@dataclass
class Event:
    id: int | None          # DB id (None until inserted)
    title: str
    start_ts: str           # ISO 8601 strings
    end_ts: str
    notes: str = ""
    created_at: str | None = None
