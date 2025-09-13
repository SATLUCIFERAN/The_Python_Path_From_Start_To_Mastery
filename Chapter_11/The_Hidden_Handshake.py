

from pathlib import Path

# Create a sample file with a BOM, simulating a file from another system
text_with_bom = "The Jedi archives are secured."
bom_file = Path("bom_data.txt")

# Writing the file with utf-8-sig adds the BOM for this example
with open(bom_file, 'w', encoding="utf-8-sig") as f:
    f.write(text_with_bom)

# Now, read it back with the correct encoding
print("--- Reading with utf-8-sig (The Correct Way) ---")
with open(bom_file, 'r', encoding="utf-8-sig") as f:
    content = f.read()
    print(f"Content: '{content}'")
    print(f"Length of content: {len(content)}")

# And read it with the wrong encoding to show the problem
print("\n--- Reading with utf-8 (The Wrong Way) ---")
try:
    with open(bom_file, 'r', encoding="utf-8") as f:
        content_wrong = f.read()
        print(f"Content: '{content_wrong}'")
        # Notice the extra character at the start, which is the BOM
        print(f"Length of content: {len(content_wrong)}")
        # We can prove it's there by looking at the first character's hexadecimal value
        print(f"Hex value of first char: {ord(content_wrong[0]):x}")
except UnicodeDecodeError as e:
    # This block will not be hit with a UTF-8 BOM, but it demonstrates how to catch
    # decoding errors with other encodings.
    print(f"ERROR: {e}")
finally:
    # Clean up the test file
    if bom_file.exists():
        bom_file.unlink()