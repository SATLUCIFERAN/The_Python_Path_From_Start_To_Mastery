
# The Holocron of Padawan names
padawan_archives = {"Ahsoka Tano": "Anakin", "Grogu": "Din Djarin"}
# Remove Grogu and his Master's name for a secret mission
removed_padawan_value = padawan_archives.pop("Grogu")
print(f"Removed: {removed_padawan_value}")
print(f"Updated Archive: {padawan_archives}")
# Output: Removed: Din Djarin, Updated Archive: {'Ahsoka Tano': 'Anakin'}



# An archive of Jedi Masters' homeworlds
jedi_homeworlds = {
    "Yoda": "Dagobah",
    "Obi-Wan Kenobi": "Stewjon",
    "Mace Windu": "Haruun Kal"
}
jedi_homeworlds.clear()
print(jedi_homeworlds)
# Output: {}