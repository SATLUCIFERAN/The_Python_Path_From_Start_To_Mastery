
import json
from pathlib import Path
import os

# Create a sample Python dictionary to represent our holocron data.
holocron_data = {
    "title": "Jedi Council Records",
    "year": 128,
    "creator": "Master Yoda",
    "entry_count": 42,
    "artifact_id": 1,
    "unicode_char": "🚀"
}

# --- Part 1: Using `dumps` and `loads` for in-memory strings ---
# This is for when you need to work with JSON as a string,
# for example, sending it over a network.

print("--- Using dumps and loads (for strings) ---")

# Serialize the Python dictionary into a JSON string.
# We add `ensure_ascii=False` to prevent the rocket emoji from being escaped.
json_string = json.dumps(holocron_data, ensure_ascii=False)
print(f"Python object serialized to JSON string:\n{json_string}\n")

# Deserialize the JSON string back into a Python object.
python_object = json.loads(json_string)
print("JSON string deserialized back to Python object:")
print(python_object)
print(f"Type of the new object: {type(python_object)}\n")



# --- Part 2: Using `dump` and `load` for files ---
# This is for when you need to save or load JSON data to/from a file.

print("--- Using dump and load (for files) ---")
file_path = Path("jedi_holocron.json")
with open(file_path, "w", encoding="utf-8") as file_out:   
    json.dump(holocron_data, file_out, ensure_ascii=False)
    print(f"Python object dumped to file: {file_path}")

# 2. Read the data back from the file using `json.load()`.
with open(file_path, "r", encoding="utf-8") as file_in:
    # `json.load` reads the entire file and returns the Python object.
    loaded_data = json.load(file_in)
    print(f"Data loaded from file: {loaded_data}")

# Clean up the dummy file.
os.remove(file_path)
print(f"Cleaned up {file_path}.")