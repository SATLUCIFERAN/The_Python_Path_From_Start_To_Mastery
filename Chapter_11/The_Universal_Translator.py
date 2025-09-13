


# Our original string contains a character that exists in UTF-8 but not in CP1252.

original_message = "I am a Python book writer. 🐍"


# Part 1: Encode the string into bytes using the correct UTF-8 key.
# This is our raw binary data, like a message transmission.
binary_data = original_message.encode("utf-8")


print("--- Attempting to decode with the WRONG language ---")
try:
    # Part 2: We try to read the binary data using the wrong key, 'cp1252'.
    # This is guaranteed to fail because the snake emoji is not in this character set.
    binary_data.decode("cp1252")

except UnicodeDecodeError as e:
    print("WARNING: The message is corrupted! Our translator is on the wrong frequency!")
    print(e)
    print("-" * 20)



# Part 3: We use the CORRECT key, 'utf-8'.
print("--- Successfully decoding with the correct language ---")
decoded_message = binary_data.decode("utf-8")
print(decoded_message)