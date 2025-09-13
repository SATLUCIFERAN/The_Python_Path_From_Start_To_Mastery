
# We're making a simple password check
print("Welcome, Jedi. Enter your starship's launch code.")

# The Jedi's defensive barrier.
try:
    # We try to get the input and convert it to an integer.
    launch_code_str = input("Launch Code (a 4-digit number): ")
    launch_code = int(launch_code_str)

    # If the code runs this far without an error, it was a number.
    if launch_code == 4217:
        print("Access granted. May the Force be with you.")
    else:
        print("Launch code invalid. Access denied.")

except ValueError:
    # If the user enters anything that can't be an integer,
    # the code jumps here, and we handle the error gracefully.
    print("Launch code must be a number! Please try again.")

print("Mission concluded.")