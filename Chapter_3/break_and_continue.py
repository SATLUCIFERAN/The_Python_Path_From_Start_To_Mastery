
mission_items = ["datapad", "grappling hook", "broken comms unit", "lightsaber", "sith artifact"]

print("Commencing mission equipment check...")

for item in mission_items:
    # The 'continue' statement allows us to skip a single item.
    if item == "broken comms unit":
        print(f"Found a broken item: {item}. Skipping to the next one.")
        continue  # Skips the rest of this loop and moves to the next item

    # The 'break' statement allows us to exit the entire loop prematurely.
    if item == "sith artifact":
        print(f"Warning: Found a forbidden item: {item}. Aborting mission immediately!")
        break  # Exits the 'for' loop entirely

    # This line will only run for items that are not skipped or do not break the loop.
    print(f"Item found: {item}. Status: OK.")

print("Mission check complete.")