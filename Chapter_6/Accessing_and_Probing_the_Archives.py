
jedi_homeworlds = {
    "Yoda": "Dagobah",
    "Obi-Wan Kenobi": "Stewjon",
    "Mace Windu": "Haruun Kal"
}

# Accessing a value by its key
yodas_planet = jedi_homeworlds["Yoda"]
print(f"Yoda's homeworld is {yodas_planet}.")
# Output: Yoda's homeworld is Dagobah.
# This would cause a KeyError if the key doesn't exist
# luke_homeworld = jedi_homeworlds["Luke Skywalker"]


# The Force is strong with this method, no error is thrown
luke_homeworld = jedi_homeworlds.get("Luke Skywalker", "Unknown")
print(f"Luke's homeworld: {luke_homeworld}")
# Output: Luke's homeworld: Unknown