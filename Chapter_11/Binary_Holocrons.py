

from pathlib import Path

binary_file = Path("secret_data.bin")

# Write some raw data to the file in binary mode ('wb')
message = b"The secret Jedi code is 100101."
with open(binary_file, 'wb') as f:
    f.write(message)

# Read the data back from the file in binary mode ('rb')
with open(binary_file, 'rb') as f:
    holocron_data = f.read()

print(f"Read data (as a bytes object): {holocron_data}")
print(f"Data type: {type(holocron_data)}")
print(f"Length of data: {len(holocron_data)} bytes")

# Cleanup the file
if binary_file.exists():
    binary_file.unlink()