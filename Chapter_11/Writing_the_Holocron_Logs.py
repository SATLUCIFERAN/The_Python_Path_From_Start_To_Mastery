
import json

hyperspace_jumps = [
    {'pilot': 'Lando', 'ship': 'Millennium Falcon', 'destination': 'Bespin', 'duration': '4.2s'},
    {'pilot': 'Han Solo', 'ship': 'Millennium Falcon', 'destination': 'Kessel Run', 'duration': '12.0s'},
    {'pilot': 'Rey', 'ship': 'Millennium Falcon', 'destination': 'Ahch-To', 'duration': '8.1s'}
]

log_file_path = 'jedi_log.ndjson'
print(f"Opening the Holocron {log_file_path} for writing...")

# The 'w' mode opens the file for writing.
# The 'a' mode would be used to append new logs without overwriting old ones.

with open(log_file_path, 'w', encoding='utf-8') as holocron_file:   
    for jump in hyperspace_jumps:        
        json_line = json.dumps(jump)        
        holocron_file.write(json_line + '\n')

print("Log entries successfully written to the Holocron.")




