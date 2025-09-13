
# Our Jedi's dynamic utility belt for a mission to Tatooine
utility_belt = ["lightsaber", "comlink", 100, "rations", "jetpack"]

# To grab a single item, you use square brackets with the item's index
first_item = utility_belt[0]
print(f"You reach for the {first_item}.")
# Output: You reach for the lightsaber.

# A true master can count from the end of a list as well

last_item = utility_belt[-1]
print(f"You grab the {last_item} just as the Sand People attack!")
# Output: You grab the jetpack just as the Sand People attack!