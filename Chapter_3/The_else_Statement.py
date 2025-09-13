
# The status of the door is "locked"
security_door = "locked"

# Check the primary condition
if security_door == "open":
    print("Proceed down the corridor.")
else:
    # This block runs only if the 'if' condition is false
    print("Wait for the signal.")