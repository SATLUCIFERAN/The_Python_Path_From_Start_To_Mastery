from pathlib import Path

# Let's assume we have a simple jedi_orders.txt file
order_file = Path("jedi_orders.txt")
order_file.write_text("Use the Force.\n") # A quick way to create a file for our example

# Example 1: Using the 'a' (append) mode
print("--- Appending an order ---")
with open(order_file, 'a') as f:
    f.write("Do, or do not. There is no try.\n")

with open(order_file, 'r') as f:
    print(f.read())
print("-" * 20)

# Example 2: Using the 'w' (write) mode - WOW, the file is overwritten!
print("--- Overwriting the orders ---")
with open(order_file, 'w') as f:
    f.write("Seek peace and tranquility.\n")

with open(order_file, 'r') as f:
    print(f.read())
print("-" * 20)

# Example 3: Using the 'x' (exclusive creation) mode - The Jedi's safety guard

new_order_file = Path("new_jedi_orders.txt")
try:
    with open(new_order_file, 'x') as f:
        f.write("A new prophecy is written.")
    print("New prophecy file created successfully!")

    # Now, try to create it again with the 'x' mode.
    with open(new_order_file, 'x') as f:
        f.write("This line will never be written.")
except FileExistsError:
    print("WARNING: The prophecy file already exists. Overwrite denied!")