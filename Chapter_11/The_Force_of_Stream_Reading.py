
import json

log_file_path = 'jedi_log.ndjson'
print(f"Reading the log entries from {log_file_path} one by one...")

# This list will hold the objects we've decoded.
# In a real-world scenario, you might process them without storing them all.
decoded_logs = []

with open(log_file_path, 'r', encoding='utf-8') as holocron_file:
    # The 'for line in holocron_file' pattern is the magic of stream reading.
    for line in holocron_file:
        # The .strip() method is crucial to remove the trailing newline character
        # that we added when writing the file.
        clean_line = line.strip()
        
        # Now we can safely decode the line into a Python dictionary
        log_entry = json.loads(clean_line)
        decoded_logs.append(log_entry)
        
        # A bit of a dramatic reveal for our progress...
        print(f"Decoded entry for pilot {log_entry['pilot']}...")

print("\nAll holocron logs successfully decoded!")
print(f"Total entries decoded: {len(decoded_logs)}")