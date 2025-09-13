import csv
import io
from pathlib import Path

# --- Step 1: The Messy Data ---
data_messy = """ ship, cargo_class , count
 Millennium Falcon, Light Freighter,  1
 T-70 X-wing, Starfighter,   2
 """
# --- Step 2: The 15-line Tidy Code ---

with io.StringIO(data_messy) as messy_csv_file:
    reader = csv.DictReader(messy_csv_file, skipinitialspace=True)
    clean_data = []
    for row in reader:
        row_clean = {key.strip(): (value.strip() if value is not None else '') 
                     for key, value in row.items()}
        if not any(row_clean.values()):  # skip empty lines
            continue
        val = row_clean.get('count', '')
        row_clean['count'] = int(val) if val else ''  # guard against ''
        clean_data.append(row_clean)

with open('clean_manifest.csv', 'w', newline='', encoding='utf-8') as clean_csv_file:
    fieldnames = clean_data[0].keys()
    writer = csv.DictWriter(clean_csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(clean_data)

print("Cleaned data successfully written to clean_manifest.csv")
print("\nFile contents:")
print("-" * 20)
print(Path("clean_manifest.csv").read_text())
print("-" * 20)
Path("clean_manifest.csv").unlink()  # Clean up
