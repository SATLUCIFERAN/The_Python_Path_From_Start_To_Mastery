

from pathlib import Path

# Our absolute path, the "full address" from the core drive.
# We use a raw string (r"...") to handle the backslashes in Windows paths.
absolute_path = \
Path(r"C:\Users\ASUS\Desktop\Pythonbook_1\Chapter_11\jedi_data.csv")
print(f"Our mission file's absolute path is:\n{absolute_path}\n")

# A quick check to see if the file exists at this precise location.
if absolute_path.exists():
    print("Cargo manifest detected. The file exists!")
else:
    print("The manifest is not with us. The file is missing.")
print("-" * 20)


# WOW! The Relative Path in Action.
# We'll simulate our current location being the "Pythonbook_1" directory.
# This makes our path much shorter and more readable.

relative_path = Path("Chapter_11/jedi_data.csv")
print(f"We can find the file from our current location at:\n{relative_path}")



# Note: The `resolve()` method reveals the full coordinate of our relative path.
print(f"relative path resolves to absolute path:\n{relative_path.resolve()}\n")