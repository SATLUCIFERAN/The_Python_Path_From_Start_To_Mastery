
jedi_masters = ("Yoda", "Obi-Wan", "Mace Windu")
number_of_masters = len(jedi_masters)
print(f"There are {number_of_masters} Jedi Masters on the council.")
# Output: There are 3 Jedi Masters on the council.


# A tuple of mission difficulty ratings
mission_ratings = (8, 5, 9, 7)
min_rating = min(mission_ratings)
max_rating = max(mission_ratings)
print(f"The easiest mission has a rating of {min_rating}, and the hardest is {max_rating}.")
# Output: The easiest mission has a rating of 5, and the hardest is 9.


mission_ratings = (8, 5, 9, 7)
total_rating = sum(mission_ratings)
print(f"The total combined difficulty of the missions is {total_rating}.")
# Output: The total combined difficulty of the missions is 29.


jedi_masters = ("Yoda", "Obi-Wan", "Mace Windu")
for i, master in enumerate(jedi_masters):
    print(f"Master {i+1}: {master}")
    
# Output:
# Master 1: Yoda
# Master 2: Obi-Wan
# Master 3: Mace Windu