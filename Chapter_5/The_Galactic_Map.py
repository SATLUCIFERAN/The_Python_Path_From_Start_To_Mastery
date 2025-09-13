
# A 2D list representing a squadron formation
# Each inner list represents a wing of starfighters

squadron_formation = [
    ["Z-Wing", "A-Wing"],
    ["Y-Wing", "X-Wing"],
    ["B-Wing", "W-Wing"]
]

# Access the X-Wing in the second wing (index 1)
pilot_2_ship = squadron_formation[1][1]
print(f"The pilot in the second wing is flying a {pilot_2_ship}.")
# Output: The pilot in the second wing is flying a X-Wing.