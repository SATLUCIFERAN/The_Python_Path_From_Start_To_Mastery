
# The Ultimate Shield
file_handle = None
try:
    # TRY to perform a risky file operation. This could fail!
    file_handle = open("jedi_scrolls.txt", "r")
    content = file_handle.read()
    print("Reading from the ancient Jedi Holocron.")

except FileNotFoundError:
    # If a bug strikes, gracefully handle it.
    print("WARNING: The Jedi Holocron was not found!")
    # We can perform a small, local recovery here.
    content = "The scroll is missing..."

except Exception as e:
    # A catch-all for any other unforeseen bugs.
    print(f"An unexpected error occurred: {e}")
    content = "Corrupted data!"

else:
    # The 'All Clear' signal. This only runs if no bugs were found.
    print("Reading successful! Content is now available.")
    print("The scroll says:", content)

finally:
    # The 'Final Protocol'. This ALWAYS runs, no matter what.
    if file_handle:
        file_handle.close()
        print("Access to Holocron terminated.")