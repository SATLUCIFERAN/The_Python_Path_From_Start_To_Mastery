

from pathlib import Path

# This section demonstrates the errors in a controlled way

print("--- Common Errors Checkpoint ---")
non_existent_file = Path("non_existent_file.txt")
try:
    with open(non_existent_file, 'r') as f:
        pass
except FileNotFoundError as e:
    print(f"ERROR: {e}")

# Note: PermissionError is system-dependent.
# This code will only work on a Linux/macOS system where the user lacks write permission.
# We will use a try-except block to gracefully handle it.

read_only_file = Path("read_only_file.txt")
try:
    read_only_file.touch()
    read_only_file.chmod(0o444) # Make the file read-only
    with open(read_only_file, 'w') as f:
        f.write("This will not work.")
except PermissionError as e:
    print(f"ERROR: {e}")
finally:
    
    if read_only_file.exists():
        read_only_file.chmod(0o666) # Corrected line to make the file writable again
        read_only_file.unlink()