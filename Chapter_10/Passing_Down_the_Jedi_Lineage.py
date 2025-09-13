
class Jedi:
    """
    The base class representing a Jedi, the foundation of our lineage.
    """
    def __init__(self, name):
        self.name = name
        self.jedi_rank = "Jedi"
        print(f"A new Jedi, {self.name}, has been created.")

    def use_force_push(self):
        """A core Jedi ability: pushing things with the Force."""
        print(f"{self.name} uses a powerful Force push!")

    def lightsaber_training(self):
        """A general method for saber training."""
        print(f"{self.name} is training with their lightsaber.")


class JediKnight(Jedi):
    """
    A class for a Jedi Knight, who is a specialized type of Jedi.
    """
    def __init__(self, name):
        super().__init__(name)
        self.jedi_rank = "Jedi Knight"
        print(f"{self.name} has achieved the rank of Jedi Knight.")

    def lead_squadron(self):
        """A unique ability for a Jedi Knight."""
        print(f"{self.name} leads a squadron into battle.")


class Padawan(JediKnight):
    
    def __init__(self, name):
        # The 'super()' function calls the __init__ method of the parent class (JediKnight).
        super().__init__(name)
        self.jedi_rank = "Padawan"
        print(f"{self.name} has been assigned the rank of Padawan.")

    def do_chores(self):
        """A unique Padawan duty: cleaning the temple archives."""
        print(f"{self.name} is cleaning the Jedi archives. Not every part of the training is glamorous.")



# --- The inheritance in action! ---
print("--- Creating a Jedi Knight ---")
obi_wan = JediKnight("Obi-Wan")
# A Jedi Knight can use core Jedi abilities.
obi_wan.use_force_push()
# And their own unique abilities.
obi_wan.lead_squadron()



print("\n--- Creating a Padawan ---")
# The Padawan inherits from JediKnight, which inherits from Jedi.
luke = Padawan("Luke")

# Now for the magic of multilevel inheritance!
# Luke can use methods from both his immediate parent (JediKnight)...
print("\n--- The Padawan inherits from their Knight... ---")
luke.lead_squadron()
# And from the original base class (Jedi)!
print("\n--- and from the original Jedi lineage! ---")
luke.use_force_push()

# And, of course, they have their own unique skills.
print("\n--- But the Padawan also has their own abilities... ---")
luke.do_chores()