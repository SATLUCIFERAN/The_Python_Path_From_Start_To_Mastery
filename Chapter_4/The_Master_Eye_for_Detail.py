
jedi_roster = [
    {"name": "Yoda", "rank": "Grand Master"},
    {"name": "Obi-Wan Kenobi", "rank": "Master"},
    {"name": "Anakin Skywalker", "rank": "Knight"},
    {"name": "Ahsoka Tano", "rank": "Padawan"},
    {"name": "Mace Windu", "rank": "Master"}
]

# We use the filter() function with a lambda.
# The lambda function checks if the 'rank' of a given Jedi is "Master".
jedi_masters = list(filter(lambda jedi: jedi["rank"] == "Master", jedi_roster))

# We print the result.
for jedi in jedi_masters:
    print(f"{jedi['name']} is a Master.")




