
# Two separate lists of Jedi names
# These are two different objects in memory
jedi_council_1 = ["Yoda", "Mace Windu"]
jedi_council_2 = ["Yoda", "Mace Windu"]

# Is the value the same? YES.
print(jedi_council_1 == jedi_council_2)
# Output: True

# Is it the exact same object? NO. They are two separate lists.
print(jedi_council_1 is jedi_council_2)
# Output: False


#########################################################################


# Assigning the second variable to be the same exact list

jedi_council_3 = jedi_council_1

# Is the value the same? YES.

print(jedi_council_1 == jedi_council_3)

# Output: True

# Is it the exact same object? YES.
# They are both pointing to the same list in memory.

print(jedi_council_1 is jedi_council_3)

# Output: True