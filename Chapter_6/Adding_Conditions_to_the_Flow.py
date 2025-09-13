
planets = ["Coruscant", "Dagobah", "Hoth", "Endor", "Tatooine"]

# Filter out any planet with 5 or more letters
long_only = [p for p in planets if len(p) >= 5]
print(f"Only long names: {long_only}")
# Output: Only long names: ['Coruscant', 'Dagobah', 'Endor', 'Tatooine']



# Tag each planet as 'long' or 'short'

planets = ["Coruscant", "Dagobah", "Hoth", "Endor", "Tatooine"]
tagged = [("long", p) if len(p) > 5 else ("short", p) for p in planets]
print(f"Tagged planets: {tagged}")

# Output: Tagged planets: [('long', 'Coruscant'), ('long', 'Dagobah'), ('short', 'Hoth'), ('short', 'Endor'), ('long', 'Tatooine')]