
class Jedi:

    def __init__(self, name, midichlorian_count):
        self.name = name
        self._jedi_rank = "Padawan"
        self.__midichlorian_count = midichlorian_count
        self.__is_on_mission = False

    def __perform_mind_trick(self):
        print(f"{self.name} uses the Force to trick a guard...")
        return True

    def _use_lightsaber(self):
        print(f"{self.name} ignites their lightsaber.")
        return True

    def go_on_mission(self):
        if self.__perform_mind_trick():
            print(f"{self.name} has successfully infiltrated the base.")
            self.__is_on_mission = True
        print(f"Is {self.name} on a mission? {self.__is_on_mission}")

    # Now using the @property decorator!
    
    @property
    def midichlorian_count(self):
        """The getter method, now accessed like an attribute."""
        return self.__midichlorian_count

    @midichlorian_count.setter
    def midichlorian_count(self, new_count):
        """The setter method, now accessed like an attribute."""
        if not isinstance(new_count, (int, float)) or new_count < 0:
            print("ERROR! Midichlorian count must be a positive number.")
            return
        self.__midichlorian_count = new_count






# --- Demonstration (using the @property decorator) ---

luke = Jedi("Luke Skywalker", 12000)

print("--- 1. Using @property for Clean Data Access ---")
# We get the value using simple attribute access.
luke_count = luke.midichlorian_count
print(f"Luke's midichlorian count is: {luke_count}.")

# We set the value using simple attribute assignment.
luke.midichlorian_count = -100 # This will fail.
luke.midichlorian_count = 14000 # This will succeed.



print("\n--- 2. Using Public Methods to perform ACTIONS ---")

luke.go_on_mission()





print("\n--- 3. Trying to Break the Rules (still fails!) ---")
try:
    print(luke.__midichlorian_count)
except AttributeError as e:
    print(f"  ERROR! {e}")

try:
    luke.__perform_mind_trick()
except AttributeError as e:
    print(f"  ERROR! {e}")

luke._use_lightsaber()