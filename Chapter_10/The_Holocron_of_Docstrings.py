
class Jedi:

    def __init__(self, name, midichlorian_count):
        self.name = name
        self._jedi_rank = "Padawan"
        self.__midichlorian_count = midichlorian_count
        self.__is_on_mission = False
        
    def get_midichlorian_count(self):
        return self.__midichlorian_count

    def set_midichlorian_count(self, new_count):
        if not isinstance(new_count, (int, float)) or new_count < 0:
            print("ERROR: Midichlorian count must be a positive number!")
            return
        self.__midichlorian_count = new_count
        print(f"Midichlorian count for {self.name} has been updated to {self.__midichlorian_count}.")


    # This is a protected method that the class itself can use.
    def _use_lightsaber(self):
        print(f"{self.name} ignites their lightsaber.")
        return True       

    def __perform_mind_trick(self):
        # This is a hidden, private method. It has no docstring because
        # it is not part of the public API.
        print(f"{self.name} uses the Force to trick a guard...")
        return True

    def go_on_mission(self):
        """
        Sends the Jedi on a stealth mission.

        This public method serves as a simple interface, hiding all
        the internal details of the mission, such as how the Jedi
        infiltrates the base.
        """
        if self.__perform_mind_trick():
            print(f"{self.name} has successfully infiltrated the base.")
            self.__is_on_mission = True
        
        print(f"Is {self.name} on a mission? {self.__is_on_mission}")





# --- Demonstration of Docstrings as Holocron Notes ---

luke = Jedi("Luke Skywalker", 12000)
print("Querying the Jedi holocron for the 'go_on_mission' method...")
print(help(luke.go_on_mission))
