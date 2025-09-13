

from pathlib import Path

# Create a sample file with some intentionally invalid bytes
corrupted_text = "Hello\xe9world"  # \xe9 is a bad byte in UTF-8
corrupted_file = Path("corrupted_data.txt")
corrupted_file.write_bytes(corrupted_text.encode("latin-1"))

print("--- Handling errors with `replace` ---")
with open(corrupted_file, 'r', encoding="utf-8", errors="replace") as f:
    content = f.read()
    # The invalid character \xe9 will be replaced by the replacement character 
    print(f"Replaced content: '{content}'")
print("-" * 20)

print("--- Handling errors with `ignore` ---")
with open(corrupted_file, 'r', encoding="utf-8", errors="ignore") as f:
    content = f.read()
    # The invalid character will be completely ignored
    print(f"Ignored content: '{content}'")
print("-" * 20)
    
# Clean up the test file
if corrupted_file.exists():
    corrupted_file.unlink()
