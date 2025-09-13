
jedi_council = ["Yoda", "Mace Windu"]
jedi_council.append("Obi-Wan Kenobi")
print(jedi_council)
# Output: ['Yoda', 'Mace Windu', 'Obi-Wan Kenobi']

jedi_council = ["Yoda", "Mace Windu"]
new_recruits = ["Anakin Skywalker", "Ahsoka Tano"]
jedi_council.extend(new_recruits)
print(jedi_council)
# Output: ['Yoda', 'Mace Windu', 'Obi-Wan Kenobi', 'Anakin Skywalker', 'Ahsoka Tano']


jedi_council = ["Yoda", "Mace Windu"]
jedi_council.insert(1, "Ki-Adi-Mundi")
print(jedi_council)
# Output: ['Yoda', 'Ki-Adi-Mundi', 'Mace Windu']


# Obi-Wan goes on a secret mission
removed_jedi = jedi_council.pop(1)
print(f"Removed: {removed_jedi}")
print(f"Council members: {jedi_council}")
# Output:
# Removed: Ki-Adi-Mundi
# Council members: ['Yoda', 'Mace Windu']


jedi_council = ['Yoda', 'Mace Windu', 'Anakin Skywalker', 'Ahsoka Tano']
jedi_council.remove("Anakin Skywalker")
print(f"The traitor is gone: {jedi_council}")
# Output: The traitor is gone: ['Yoda', 'Mace Windu', 'Ahsoka Tano']


jedi_council = ['Yoda', 'Mace Windu', 'Anakin Skywalker', 'Ahsoka Tano']
jedi_council.clear()
print(f"The archives are empty: {jedi_council}")
# Output: The archives are empty: []


squadron = ["Red 1", "Red 2", "Gold Leader", "Red 3"]
gold_index = squadron.index("Gold Leader")
print(f"Gold Leader is at position {gold_index}.")
# Output: Gold Leader is at position 2.


squadron = ["Red 1", "Red 2", "Gold Leader", "Red 3", "Red 1"]
red_count = squadron.count("Red 1")
print(f"There are {red_count} Red 1s in the squadron.")
# Output: There are 2 Red 1s in the squadron.


# A list of Jedi names
jedi_names = ["Yoda", "Mace Windu", "Obi-Wan Kenobi", "Anakin Skywalker"]
jedi_names.sort()
print(f"Sorted ranks: {jedi_names}")
# Output: Sorted ranks: ['Anakin Skywalker', 'Mace Windu', 'Obi-Wan Kenobi', 'Yoda']

jedi_names = ["Yoda", "Mace Windu", "Obi-Wan Kenobi", "Anakin Skywalker"]
jedi_names.reverse()
print(f"Reversed ranks: {jedi_names}")
# Output: Reversed ranks: ['Yoda', 'Obi-Wan Kenobi', 'Mace Windu', 'Anakin Skywalker']