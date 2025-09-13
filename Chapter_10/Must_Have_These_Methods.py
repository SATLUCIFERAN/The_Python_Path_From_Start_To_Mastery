
from typing import Protocol

# We define a Protocol that any SaberWielder must conform to.
# This is a contract, not a parent class.
class SaberWielder(Protocol):
    def ignite_saber(self) -> None:
        ...  # This "..." tells the type checker that we don't care about the implementation, only that the method exists.

    def swing_saber(self) -> None:
        ...


class Jedi:
    def __init__(self, name: str):
        self.name = name

    def ignite_saber(self) -> None:
        print(f"{self.name} ignites their green lightsaber.")

    def swing_saber(self) -> None:
        print(f"{self.name} swings their saber with a practiced form.")


class Sith:
    def __init__(self, name: str):
        self.name = name

    def ignite_saber(self) -> None:
        print(f"{self.name} ignites their ominous red lightsaber.")

    def swing_saber(self) -> None:
        print(f"{self.name} swings their saber with a powerful, aggressive form.")


def duel_training(wielder: SaberWielder):
    """
    This function accepts any object that conforms to the SaberWielder Protocol.
    We can confidently call its methods because of the contract.
    """
    print("Beginning saber training...")
    wielder.ignite_saber()
    wielder.swing_saber()
    print("Training complete.\n")


# --- The demonstration ---

luke = Jedi("Luke Skywalker")
darth_vader = Sith("Darth Vader")

# Both Luke and Vader can be passed to our function because
# they both fulfill the SaberWielder Protocol contract!
duel_training(luke)
duel_training(darth_vader)