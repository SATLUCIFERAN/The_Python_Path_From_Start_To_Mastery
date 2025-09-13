
import csv
import io

data = """item,quantity
Lightsaber,2
Blaster,
Jedi Robes,1"""

with io.StringIO(data) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # A careless attempt at casting
        try:
            qty = int(row['quantity'])
            print(f"Item: {row['item']}, Quantity: {qty}")
        except ValueError as e:
            print(f"Error casting '{row['quantity']}' to integer: {e}")





            