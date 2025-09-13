
from pathlib import Path

# Our starting point, the "Pythonbook_1" folder.
current_location = Path(r"C:\Users\ASUS\Desktop\Pythonbook_1")

# WOW! We can build the rest of the path by 'chaining' to our location.
# This feels natural and is far cleaner than building a string.

full_chained_path = current_location / "Chapter_11" / "jedi_data.csv"
print(f"The path to the file, built by chaining, is:\n{full_chained_path}")

# And just to prove it's the same, let's compare it to the original absolute path.

original_path = \
Path(r"C:\Users\ASUS\Desktop\Pythonbook_1\Chapter_11\jedi_data.csv")
print(f"Is this the same path? {original_path == full_chained_path}")




