
import csv
from pathlib import Path

# The file we will be writing to
manifest_file = Path("cargo_manifest.csv")

# A list of dictionaries, where each dictionary represents a row of data
cargo_list = [
    # A standard dictionary with all fields
    {'item': 'Hyperdrive', 'quantity': 1, 'origin': 'Corellia'},

    # A dictionary with an extra field, which will be ignored
    {'item': 'Blaster Pistol', 'quantity': 50, 'origin': 'Corellia', 'notes': 'Class I'},

    # A dictionary missing a field, which will get a default value
    {'item': 'Proton Torpedo', 'quantity': 100},
]

# We must define the column headers (fieldnames) in a list.
# This also sets the order of the columns.
fieldnames = ['item', 'quantity', 'origin']


# Open the file and create a DictWriter object
with open(manifest_file, 'w', newline='', encoding='utf-8') as csvfile:
    # Create the DictWriter object, passing the file and fieldnames
    writer = csv.DictWriter(csvfile,
                            fieldnames=fieldnames,
                            extrasaction='ignore',
                            restval='n/a')
    # Write the header row
    writer.writeheader()
    # Write the data rows using writerows() for efficiency
    writer.writerows(cargo_list)

print(f"Successfully wrote data to '{manifest_file}'")
print("\nFile contents:")
print("-" * 20)
print(manifest_file.read_text())
print("-" * 20)

# Clean up the file
manifest_file.unlink()






