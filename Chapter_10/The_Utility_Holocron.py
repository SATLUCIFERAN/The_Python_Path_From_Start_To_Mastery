
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


    @staticmethod
    def calculate_force_potential(crystal_type):
        """
        A static method that provides a utility function.
        It doesn't depend on a specific Lightsaber object.
        """
        potential_map = {
            "Ilum": "High",
            "Kaiburr": "Extremely High",
            "Lava": "Unstable",
        }
        return potential_map.get(crystal_type, "Unknown")

# We call the static method on the class.
ilum_crystal_force = Lightsaber.calculate_force_potential("Ilum")
print(f"An Ilum crystal has a Force potential of: {ilum_crystal_force}.")

# We can also call it on an object, but it's not the primary use.

anakins_saber = Lightsaber('blue', 'apprentice', 'Ilum')
anakins_saber_force = anakins_saber.\
                      calculate_force_potential(anakins_saber.kyber_crystal)
print("Anakin's saber has a crystal with a Force potential of: " \
      f"{anakins_saber_force}.")