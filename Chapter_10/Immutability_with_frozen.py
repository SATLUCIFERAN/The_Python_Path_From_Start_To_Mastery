
from dataclasses import dataclass

@dataclass(frozen=True)
class Holocron:
    message: str
    sender: str
    recipient: str

# Create a frozen holocron.

jedi_holocron = Holocron("The Force is strong with this one.", "Master Yoda", 
                         "The Jedi Council")

try:
    jedi_holocron.message = "The Force is not strong with this one."
except Exception as e:
    print(f"Error! Cannot change a frozen holocron: {e}")
