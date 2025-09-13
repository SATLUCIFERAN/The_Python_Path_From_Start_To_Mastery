
# # A tuple of Force-sensitive children's names
# younglings = ("Grogu", "Ahsoka")

# # We can't change the tuple directly! This would be an error.
# # younglings.append("Leia Organa")

# # The Jedi way: convert, modify, and convert back
# younglings_list = list(younglings) # Convert to a list
# younglings_list.append("Leia Organa") # Add the new youngling
# updated_younglings = tuple(younglings_list) # Convert back to a tuple

# print(updated_younglings)
# # Output: ('Grogu', 'Ahsoka', 'Leia Organa')


younglings = ("Grogu", "Ahsoka")
younglings_list = list(younglings)
younglings_list.append("Leia Organa")
updated_younglings = tuple(younglings_list)
print(younglings_list)
print(updated_younglings)