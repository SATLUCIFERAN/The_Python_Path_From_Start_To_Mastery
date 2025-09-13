
import json
from pathlib import Path
import os

# Sample data with nested objects and a non-ASCII character

complex_data = {
    "entry_id": 101,
    "source_system": "Hyperspace Tracker",
    "timestamp": "2024-08-28T14:30:00Z",
    "starship": {
        "model": "Razor Crest",
        "pilot": "Din Djarin",
        "passengers": [
            "Grogu",
            "Kuiil",
            "IG-11"
        ]
    },
    "destination": "Exegol",
    "status": "In Transit",
    "unicode_char": "✨",
    "accented_char": "résumé"
}


# --- Part 1: Default, unreadable JSON ---
# The default output is a single, compact line.
print("--- Default JSON Output (Unreadable) ---")
default_json = json.dumps(complex_data)
print(default_json)
print("-" * 50 + "\n")


# --- Part 2: Readable JSON using `indent` ---
# This is what you'll use most of the time for humans.
print("--- Pretty-Printed JSON (indent=4) ---")
pretty_json = json.dumps(complex_data, indent=4)
print(pretty_json)
print("-" * 50 + "\n")


# --- Part 3: Global-friendly output with `ensure_ascii=False` ---
# This keeps special characters readable and intact.

print("--- Global-Friendly JSON (ensure_ascii=False) ---")
global_json = json.dumps(complex_data, indent=4, ensure_ascii=False)
print(global_json)
print("-" * 50 + "\n")


# --- Part 4: Stable, diff-friendly output with `sort_keys=True` ---
# This ensures a consistent key order every time.
print("--- Stable JSON (sort_keys=True) ---")
sorted_json = json.dumps(complex_data, indent=4, sort_keys=True)
print(sorted_json)
print("-" * 50 + "\n")


# --- Part 5: The most compact JSON for machine-to-machine transfer ---
# This removes all whitespace for minimal file size.

print("--- Compact JSON (separators) ---")
compact_json = json.dumps(complex_data, separators=(',', ':'))
print(compact_json)
print("-" * 50 + "\n")

# Note: These parameters are also available for json.dump() when writing to a file.

file_path = Path("formatted_data.json")
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(complex_data, f, indent=2, ensure_ascii=False, sort_keys=True)

print(f"Formatted JSON written to {file_path}. Deleting file now.")
os.remove(file_path)