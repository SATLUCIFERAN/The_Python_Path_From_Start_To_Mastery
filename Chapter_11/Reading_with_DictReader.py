
import csv
from pathlib import Path

# Let's assume we have a simple CSV file to read
data = """name,class,side
T-65 X-wing,Starfighter,Rebel
Millennium Falcon,Light Freighter,Rebel
Slave I,Patrol and attack craft,Bounty Hunter"""
csv_file = Path("starship_manifest.csv")
csv_file.write_text(data)

# Open the file and create a DictReader object
with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    # Now, let's loop through the rows and work with the data
    for row in reader:
        # Each 'row' is a dictionary, and we can access values by column name!
        print(f"Name: {row['name']}, Class: {row['class']}, Side: {row['side']}")

# Clean up the file
csv_file.unlink()