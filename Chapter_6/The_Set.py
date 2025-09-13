
# A set of unique Jedi Council members for today's meeting
todays_council_members = {"Yoda", "Obi-Wan Kenobi", "Mace Windu"}
print(todays_council_members)
# Output: {'Mace Windu', 'Yoda', 'Obi-Wan Kenobi'}





# Imagine a mission log filled with redundant entries
unfiltered_mission_log = ["Evacuate", "Search for Rebels", "Evacuate", "Scout the System", "Search for Rebels"]

# WOW! Use the Force of set() to instantly remove duplicates
unique_orders = set(unfiltered_mission_log)
print(unique_orders)
# Output: {'Evacuate', 'Search for Rebels', 'Scout the System'}