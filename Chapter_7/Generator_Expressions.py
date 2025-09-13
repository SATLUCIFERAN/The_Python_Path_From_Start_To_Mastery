
# List of Planets
planets = ["Coruscant", "Dagobah", "Hoth"]

# A list comprehension (creates the full list immediately)
planet_lengths_list = [len(p) for p in planets]
print(f"List: {planet_lengths_list}")
# Output: List: [9, 7, 4]

# A generator expression (creates an iterator that waits)
planet_lengths_generator = (len(p) for p in planets)
print(f"Generator Object: {planet_lengths_generator}")
# Output: Generator Object: <generator object <genexpr> at ...>


# Now, we can iterate over it to get the values one by one

print(f"First length: {next(planet_lengths_generator)}")
print(f"Second length: {next(planet_lengths_generator)}")
print(f"Third length: {next(planet_lengths_generator)}")

# Output: First length: 9
# Second length: 7
# Third length: 4


