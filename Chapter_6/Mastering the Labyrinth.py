
# Create all possible pairings of Jedi and missions
jedi = ["Yoda", "Ahsoka"]
missions = ["Hoth", "Endor"]
pairs = [(j, m) for j in jedi for m in missions]
print(f"Jedi mission pairs: {pairs}")
# Output: Jedi mission pairs: [('Yoda', 'Hoth'), ('Yoda', 'Endor'), ('Ahsoka', 'Hoth'), ('Ahsoka', 'Endor')]


# Flatten a 2D grid of data
grid = [[1, 2], [3, 4], [5, 6]]
flat = [n for row in grid for n in row]
print(f"Flattened grid: {flat}")
# Output: Flattened grid: [1, 2, 3, 4, 5, 6]
