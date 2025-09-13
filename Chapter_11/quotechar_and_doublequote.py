
import csv
from pathlib import Path

# This file has a comma inside a value, and a double quote inside a quoted value.
# Notice how the inner quote is doubled ("").
data_quoted = """item,quantity,details
"Droid, Protocol",1,"This ""droid"" is not the one you're looking for."
"Bacta Tank, ""Jumbo"" Size",2,"A "large" tank." """
csv_file = Path("quoted_data.csv")
csv_file.write_text(data_quoted)

with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
    # Here, we're using all the defaults, which is why it works perfectly.
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Item: {row['item']}, Quantity: {row['quantity']}, Details: {row['details']}")

csv_file.unlink() # Clean up