
import pandas as pd

# Mission log for Day 1
log_day1 = pd.DataFrame({
    'Pilot ID': [1, 2],
    'Kills': [5, 2]
})

# Mission log for Day 2
log_day2 = pd.DataFrame({
    'Pilot ID': [1, 3],
    'Kills': [2, 3]
})

print("--- Mission Log Day 1 ---")
print(log_day1)
print("\n--- Mission Log Day 2 ---")
print(log_day2)

# Concatenate the two logs, stacking them on top of each other

combined_log = pd.concat([log_day1, log_day2], ignore_index=True)
print("\n--- Concatenated Mission Log (day1 + day2) ---")
print(combined_log)