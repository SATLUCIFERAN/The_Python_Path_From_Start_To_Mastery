
squadron = ["Red 1", "Red 2", "Gold Leader"]
squadron_size = len(squadron)
print(f"Our squadron has {squadron_size} pilots.")
# Output: Our squadron has 3 pilots.


# A list of Jedi's strength scores
force_scores = [120, 95, 150, 80]
min_score = min(force_scores)
max_score = max(force_scores)
print(f"The lowest Force score is {min_score}, and the highest is {max_score}.")
# Output: The lowest Force score is 80, and the highest is 150.

force_scores = [120, 95, 150, 80]
total_force = sum(force_scores)
print(f"The total Force potential of the group is {total_force}.")
# Output: The total Force potential of the group is 445.


squadron = ["Red 1", "Red 2", "Gold Leader"]
for i, pilot in enumerate(squadron):
    print(f"Pilot {i}: {pilot}")
# Output:
# Pilot 0: Red 1
# Pilot 1: Red 2
# Pilot 2: Gold Leader