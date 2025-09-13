
import csv
import io
from typing import Any

# Our original data with a mix of numbers and missing values.
data = """item,quantity
Lightsaber,2
Blaster,
Jedi Robes,1
Droid, 4""" # Example with a space


# A small function to safely cast to an integer, with a default value.
def safe_int_cast(value: Any, default: int = 0) -> int:
    """
    Safely converts a value to an integer, returning a default if it fails.
    This handles empty strings and non-integer values gracefully.
    """
    # First, check for empty strings or None to avoid a ValueError
    if value is None or str(value).strip() == '':
        return default
    
    # Then, use a try-except block for values that can't be cast.
    try:
        return int(str(value).strip())
    except (ValueError, TypeError):
        return default

# Read the data and use our safe casting method
with io.StringIO(data) as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    print("Safely reading and casting quantities:")
    for row in reader:
        qty = safe_int_cast(row.get('quantity'))
        print(f"Item: {row['item']}, Quantity: {qty}")