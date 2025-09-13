
class Jedi:
    """
    A class representing a Jedi that demonstrates comprehensive encapsulation.
    """
    def __init__(self, name, midichlorian_count):
        self.name = name
        self._jedi_rank = "Padawan"
        self.__midichlorian_count = midichlorian_count
        self.__is_on_mission = False
    
    def get_midichlorian_count(self):
        return self.__midichlorian_count

    def set_midichlorian_count(self, new_count):
        if not isinstance(new_count, (int, float)) or new_count < 0:
            print("ERROR: Invalid midichlorian count!")
            return
        self.__midichlorian_count = new_count
        print(f"Midichlorian count for {self.name} has been updated.")

    def go_on_mission(self):
        if self.__perform_mind_trick():
            print(f"{self.name} has successfully infiltrated the base.")
            self.__is_on_mission = True
        print(f"Is {self.name} on a mission? {self.__is_on_mission}")

    def _use_lightsaber(self):
        print(f"{self.name} ignites their lightsaber.")
        return True    

    def __perform_mind_trick(self):
        print(f"{self.name} uses the Force to trick a guard...")
        return True

   





luke = Jedi("Luke Skywalker", 12000)

print("--- 1. Using Getters & Setters for DATA ---")
# CORRECT: Use the getter method to read the private attribute.
luke_count = luke.get_midichlorian_count()
print(f"Luke's midichlorian count is: {luke_count}.")
# CORRECT: Use the setter method to safely change the private attribute.
luke.set_midichlorian_count(-100) # This will fail.
luke.set_midichlorian_count(14000) # This will succeed.



print("\n--- 2. Using Public Methods to perform ACTIONS ---")
# CORRECT: Call the public method. It internally uses the private method.
luke.go_on_mission()



print("\n--- 3. Trying to Break the Rules ---")
# INCORRECT: Direct access to the private attribute fails.
try:
    print(luke.__midichlorian_count)
except AttributeError as e:
    print(f"  ERROR! {e}")
# This will fail because you cannot call a private method directly.
try:
    luke.__perform_mind_trick()
except AttributeError as e:
    print(f"  ERROR! {e}")
# This will work, but it's not recommended unless you are in a subclass!
# It's a "protected" method.
luke._use_lightsaber()