
import csv
from pathlib import Path

# This file uses a semicolon (;) as a delimiter
data_semicolon = """product;price;in_stock
Hyperdrive motivator;999;True
Proton torpedo;150;True
Jedi holocron;50000;False"""
csv_file = Path("semicolon_data.csv")
csv_file.write_text(data_semicolon)

with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
    # We set the delimiter to a semicolon
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        print(f"Product: {row['product']}, Price: {row['price']}, In Stock: {row['in_stock']}")

        

csv_file.unlink() # Clean up