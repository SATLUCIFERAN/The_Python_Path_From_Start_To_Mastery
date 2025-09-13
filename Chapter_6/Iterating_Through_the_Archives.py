

jedi_rankings = {
    "Yoda": 10,
    "Obi-Wan Kenobi": 8,
    "Mace Windu": 10,
    "Ahsoka Tano": 7,
    "Anakin Skywalker": 8,
}


for name in jedi_rankings.keys():
    print(f"Master: {name}")


for rating in jedi_rankings.values():
    print(f"Rating: {rating}")


# Our list of Jedi rankings
for name, rating in jedi_rankings.items():
    print(f"Master {name} has a rating of {rating}.")

  