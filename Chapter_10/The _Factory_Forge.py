
import random

class Lightsaber:
    """A blueprint for creating powerful lightsabers."""

    def __init__(self, color, hilt_style, kyber_crystal_type):
        """
        The constructor. This method is called automatically when we create a new Lightsaber object.
        We give it the specific properties for this unique lightsaber.
        """
        # We assign the passed-in values to the object's attributes.
        # 'self' refers to the specific lightsaber we're building.
        self.color = color
        self.hilt_style = hilt_style
        self.kyber_crystal = kyber_crystal_type
        self.is_on = False  # Every lightsaber starts in the 'off' state.

    def __str__(self):
        """
        A special method for humans! When someone tries to print the object,
        this is what will be shown.
        """
        return f"A {self.hilt_style} hilt with a {self.color} blade."

    def ignite(self):
        """
        A method (ability) to safely turn the blade on.
        """
        if not self.is_on:
            print(f"FOOM! The {self.color} blade ignites with a hum.")
            self.is_on = True
        else:
            print("The blade is already ignited!")

    @classmethod
    def from_salvaged_parts(cls, salvaged_hilt):
        """
        A class method that acts as a factory.
        It creates a new Lightsaber object from a salvaged hilt.
        """
        crystal_types = ["Ilum", "Kaiburr", "Lava"]
        new_crystal = random.choice(crystal_types)
        print(f"A salvaged {salvaged_hilt} hilt was found! Forging a new saber with a {new_crystal} crystal.")
        return cls("blue", salvaged_hilt, new_crystal)

# We use the class method to create a new lightsaber.

salvaged_saber = Lightsaber.from_salvaged_parts("old_apprentice")
salvaged_saber.ignite()