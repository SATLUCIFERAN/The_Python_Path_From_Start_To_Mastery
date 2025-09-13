
from dataclasses import dataclass

@dataclass(order=True)
class JediRanking:
    midichlorian_count: int
    name: str
    
jedi_rankings = [
    JediRanking(12000, "Luke Skywalker"),
    JediRanking(27700, "Anakin Skywalker"),
    JediRanking(17700, "Obi-Wan Kenobi")
]


print("Original list:")
print(jedi_rankings)


jedi_rankings.sort()
print("\nSorted list:")
print(jedi_rankings)