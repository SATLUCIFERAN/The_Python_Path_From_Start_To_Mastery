
from pathlib import Path

def chunked_copy(source_file, destination_file, chunk_size=4096):
    """
    Copies a file in binary mode, chunk by chunk, to save memory.
    """
    with open(source_file, 'rb') as infile:
        with open(destination_file, 'wb') as outfile:
            while True:
                # Read a chunk of data
                chunk = infile.read(chunk_size)
                # If the chunk is empty, we've reached the end of the file
                if not chunk:
                    break
                # Write the chunk to the output file
                outfile.write(chunk)

# For demonstration, let's create a fake large file
fake_large_file = Path("big_binary_file.bin")
with open(fake_large_file, 'wb') as f:
    f.write(b"\x00" * (1024 * 1024 * 5)) # Create a 5MB file

# Now, copy the file using our chunked method
copied_file = Path("copied_binary_file.bin")
print("Initiating a chunked copy of the large file...")
chunked_copy(fake_large_file, copied_file)
print("Chunked copy complete!")

# Check if the files are the same size
print(f"Original file size: {fake_large_file.stat().st_size} bytes")
print(f"Copied file size: {copied_file.stat().st_size} bytes")

# Clean up
fake_large_file.unlink()
copied_file.unlink()