
# Galaxy's planets
planets = ["Coruscant", "Dagobah", "Hoth", "Endor", "Tatooine"]

# map: Get the lengths of all planet names
lengths = [len(p) for p in planets]
print(f"Planet name lengths: {lengths}")
# Output: Planet name lengths: [9, 7, 4, 5, 8]


# filter: Only find planets that start with 'T'
t_planets = [p for p in planets if p.startswith("T")]
print(f"Planets starting with T: {t_planets}")
# Output: Planets starting with T: ['Tatooine']