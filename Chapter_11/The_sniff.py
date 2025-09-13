
import csv
import io
from pathlib import Path

# A file with an unknown dialect: semicolon delimiter, single-quote character.
data_unknown_dialect = """ship;cargo_class;details
T-70 X-wing;Starfighter;'R2 unit, droid'
Millennium Falcon;Light Freighter;'Smuggler, cargo'"""

# The Sniffer needs a sample string to analyze
# We'll use the entire string here for simplicity
sniffer = csv.Sniffer()
dialect = sniffer.sniff(data_unknown_dialect)

# Now we can use the guessed dialect to read the file correctly
with io.StringIO(data_unknown_dialect) as csvfile:
    # We pass the dialect object directly to the reader
    reader = csv.DictReader(csvfile, dialect=dialect)
    print("Reading data with the sniffed dialect:")
    for row in reader:
        print(f"Ship: {row['ship']}, Class: {row['cargo_class']}, Details: {row['details']}")

    # Let's also test if the sniffer correctly identified the header
    if sniffer.has_header(data_unknown_dialect):
        print("\nThe sniffer correctly identified a header row.")
    else:
        print("\nThe sniffer did not detect a header.")