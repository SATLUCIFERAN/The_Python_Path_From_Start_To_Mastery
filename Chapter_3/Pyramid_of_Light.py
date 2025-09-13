
height = 5
# The outer loop handles the rows, from 0 to 4.
for i in range(height):
    # Inner Loop 1: Print the leading spaces. The number of spaces decreases each time.
    print("  " * (height -i - 1), end="")
    # Inner Loop 2: Print the stars. The number of stars increases by 2 each time.
    print("⭐" * (2 * i + 1))