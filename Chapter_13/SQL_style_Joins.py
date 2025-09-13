
import pandas as pd

# Roster of X-Wing pilots (our 'left' DataFrame)

pilots_roster = pd.DataFrame({
    'Pilot ID': [1, 2, 3, 4],
    'Pilot Name': ['Luke', 'Wedge', 'Biggs', 'Porkins'],
    'Squadron': ['Red', 'Red', 'Red', 'Red']
})

# A combat log with mission data (our 'right' DataFrame)
mission_log = pd.DataFrame({
    'Pilot ID': [1, 2, 3, 5],
    'Kills': [5, 2, 3, 1],
    'Damage Taken': [10, 5, 8, 3]
})

print("--- Pilot Roster ---")
print(pilots_roster)
print("\n--- Mission Log ---")
print(mission_log)

# Inner Merge: Combine on Pilot ID, only including matching pilots
inner_merge = pd.merge(pilots_roster, mission_log, on='Pilot ID', how='inner')
print("\n--- Inner Merge (matching pilots only) ---")
print(inner_merge)

# Left Merge: Keep all pilots from the roster and add mission data if available

left_merge = pd.merge(pilots_roster, mission_log, on='Pilot ID', how='left')
print("\n--- Left Merge (all pilots from roster) ---")
print(left_merge)