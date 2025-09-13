
# The Blueprint: The Lightsaber Class
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

# The Object: We are now creating, or "instantiating," a lightsaber object from our blueprint.
# This single line calls the __init__ method automatically!
anakins_saber = Lightsaber('blue', 'apprentice', 'Ilum')

# We can now use our object's attributes and methods.
print("Wow! Look at that hilt!")
print(anakins_saber) # This uses the __str__ method we wrote!

print("\nAnakin tries to activate the saber...")
anakins_saber.ignite()
print(f"The blade is now: {anakins_saber.is_on}")

print("\nHe tries to ignite it again, just for fun...")
anakins_saber.ignite()