
jedi_council = {"Yoda", "Obi-Wan"}
jedi_council.add("Anakin Skywalker")
jedi_council.add("Obi-Wan")  # This will not be added again
print(jedi_council)
# Output: {'Yoda', 'Obi-Wan', 'Anakin Skywalker'}




jedi_council = {"Yoda", "Obi-Wan"}
jedi_council.clear()
print(jedi_council)
# Output: set()



jedi_ships = {"X-Wing", "Y-Wing", "A-Wing"}
popped_ship = jedi_ships.pop()
print(f"The ship that retreated: {popped_ship}")
# Output: The ship that retreated: X-Wing (or Y-Wing, or A-Wing)



jedi_ships = {"X-Wing", "Y-Wing", "A-Wing"}
jedi_ships.remove("X-Wing")
print(jedi_ships)
# Output: {'Y-Wing', 'A-Wing'}