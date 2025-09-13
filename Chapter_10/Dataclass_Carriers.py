
from dataclasses import dataclass

# The dataclass version is much more concise!
@dataclass
class MissionReport:
    name: str
    date: str
    jedi: str
    

# Let's create an instance of our dataclass.
report = MissionReport("Destruction of the Death Star", "Yavin IV, 0 BBY", "Luke Skywalker")
print(report)
