
import gzip
from pathlib import Path

# Create a sample text file to compress in text mode
compressed_text_file = Path("jedi_scroll.txt.gz")
with gzip.open(compressed_text_file, 'wt', encoding='utf-8') as f:
    f.write("A Jedi's strength flows from the Force.")

# Now, read it back in using gzip.open in text mode
with gzip.open(compressed_text_file, 'rt', encoding='utf-8') as f:
    read_text = f.read()

print(f"Original text: A Jedi's strength flows from the Force.")
print(f"Decoded from compressed file: {read_text}")

# You can also work with binary mode if needed
binary_compressed_file = Path("binary_data.gz")
with gzip.open(binary_compressed_file, 'wb') as f:
    f.write(b"Raw binary data!")

# Read it back in binary mode
with gzip.open(binary_compressed_file, 'rb') as f:
    read_binary = f.read()

print(f"Read from binary compressed file: {read_binary}")

# Clean up
compressed_text_file.unlink()
binary_compressed_file.unlink()