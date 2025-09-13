
from pathlib import Path

# Create a sample log file for our example
log_file = Path("jedi_log.txt")
log_content = """Jedi Log - Day 1
Mission: Investigate ancient ruins.
Weather: Clear skies.
Encounters: Local wildlife seems friendly.
Notes: Found strange markings on a stone wall.
End of Log."""
log_file.write_text(log_content) # Ensure the file exists for this example

print("--- Using seek() and tell() ---")
with open(log_file, 'r') as f:
    # Tell our starting position (should be 0)
    print("Starting position:", f.tell())
    
    # Read the first 10 characters
    first_part = f.read(10)
    print("Read 10 characters:", first_part)
    
    # Tell our new position    
    print("New position:", f.tell())
    
    # Go back to the beginning of the file (position 0)    
    f.seek(0)
    print("Position after seek(0):", f.tell())
    
    # Read the entire file again

    full_content = f.read()
    print("Read entire content:", full_content.strip())

    
print("-" * 20)