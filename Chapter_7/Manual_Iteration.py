
# Our list of Jedi Masters
jedi_masters = ["Yoda", "Obi-Wan Kenobi", "Mace Windu"]

# Step 1: Get the archivist (the iterator object)
jedi_archivist = iter(jedi_masters)

# Step 2: Manually ask for the next piece of data, one at a time
print(f"Jedi Master 1: {next(jedi_archivist)}")
# Output: Jedi Master 1: Yoda

print(f"Jedi Master 2: {next(jedi_archivist)}")
# Output: Jedi Master 2: Obi-Wan Kenobi

print(f"Jedi Master 3: {next(jedi_archivist)}")
# Output: Jedi Master 3: Mace Windu

# WOW! We've run out of items. If we try to ask again...
# next(jedi_archivist) # This would raise a StopIteration error!