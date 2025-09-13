

from pathlib import Path

log_file = Path("jedi_log.txt")
log_content = """Jedi Log - Day 1
Mission: Investigate ancient ruins.
Weather: Clear skies.
Encounters: Local wildlife seems friendly.
Notes: Found strange markings on a stone wall.
End of Log."""


print("--- Part 1: Writing to the scroll ---")
with open(log_file, 'w') as f:
    f.write("Jedi Holocron\n")  # Write a single line
    lines_to_write = ["New Entry: Observed strange comet.\n", 
                      "Final Note: Mission complete.\n"]
    f.writelines(lines_to_write) # Write multiple lines at once
print("Written to file:", log_file.read_text())
print("-" * 20)


print("--- Part 2: Reading the scroll ---")
with open(log_file, 'r') as f:
    print("Reading the entire file with read():")
    full_content = f.read()
    print(full_content)

with open(log_file, 'r') as f:
    print("Reading line by line with readline():")
    line = f.readline()
    while line:
        print("  -", line.strip()) # strip() to remove the newline characters
        line = f.readline()

with open(log_file, 'r') as f:
    print("Reading all lines into a list with readlines():")
    lines_list = f.readlines()
    print(lines_list)

with open(log_file, 'r') as f:
    print("Reading line by line with a for loop:")
    for line in f:
        print(" -", line.strip())
print("-" * 20)
