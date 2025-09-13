
import csv
from pathlib import Path

data_with_spaces = """name, class
Obi-Wan Kenobi, Jedi Knight"""
csv_file = Path("spaced_manifest.csv")
csv_file.write_text(data_with_spaces)

# Adding skipinitialspace=True to handle the extra space
with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:    
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    for row in reader:
        # The key is now "class", not " class"
        print(f"Name: {row['name']}, Class: {row['class']}")

csv_file.unlink() # Clean up