import csv
from pathlib import Path

# The file uses a pipe (`|`) as a delimiter and a backslash (`\`)
# to escape the quote character.
data_escaped = """item|quantity
"Hyperdrive Motivator"|1
"Jedi Holocron"|1
"Lightsaber \"Blue\" Blade"|2"""
csv_file = Path("escaped_data.csv")
csv_file.write_text(data_escaped)

# Create the file with the expected data to read
with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
    # We set both the delimiter and the escapechar
    reader = csv.reader(csvfile, delimiter='|', escapechar='\\')
    for row in reader:
        print(row)

csv_file.unlink() # Clean up