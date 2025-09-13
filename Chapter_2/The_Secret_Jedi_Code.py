
# We are given a secret code from a holocron
jedi_holocron_code = "J"

# We use our tool to look up its true identity in the catalog
numeric_address = ord(jedi_holocron_code)
print(f"The secret numeric address for the character '{jedi_holocron_code}' is {numeric_address}.")
# Output: The secret numeric address for the character 'J' is 74.

# We can also do the opposite with chr()
character_from_number = chr(74)
print(f"The character at numeric address 74 is '{character_from_number}'.")
# Output: The character at numeric address 74 is 'J'.