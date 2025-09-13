
# A list of a Jedi's missions, in chronological order
mission_log = ["Coruscant", "Dagobah", "Hoth", "Endor", "Tatooine"]

first_three_mission = mission_log[0:3]
print(f"My first three mission:{first_three_mission}")


# Output: My first three mission:['Coruscant', 'Dagobah', 'Hoth']

last_mission = mission_log[-1] # The last item
print(f"Your last mission was to {last_mission}.")
# Output: Your last mission was to Tatooine.

pre_final_missions = mission_log[:-2]
print(f"All missions before the final two: {pre_final_missions}")
# Output: All missions before the final two: ['Coruscant', 'Dagobah', 'Hoth']


# Reverse the entire log to see the missions in reverse chronological order
reverse_log = mission_log[::-1]
print(f"missions in reverse: {reverse_log}")
# Output: missions in reverse: ['Tatooine', 'Endor', 'Hoth', 'Dagobah', 'Coruscant']