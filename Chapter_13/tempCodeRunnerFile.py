import pandas as pd
import numpy as np

# Create a full combat log from the Battle of Yavin
combat_log = pd.DataFrame({
    'Pilot ID': ['Luke', 'Luke', 'Wedge', 'Biggs', 'Wedge', 'Han', 'Han'],
    'Squadron': ['Red', 'Red', 'Red', 'Red', 'Red', 'Gold', 'Gold'],
    'Kills': [5, 2, 1, 3, 2, 4, 1],
    'Damage Taken': [10, 5, 2, 8, 3, 15, 6]
})

print("--- Full Combat Log ---")
print(combat_log)

# Group by Squadron AND Pilot ID (Multi-Index)
# Use .agg for total kills, total damage, and custom efficiency
squadron_pilot_summary = combat_log.groupby(['Squadron', 'Pilot ID']).agg(
    TotalKills=('Kills', 'sum'),
    TotalDamage=('Damage Taken', 'sum'),
    CombatEfficiency=lambda g: (
                                g['Kills'].sum() / g['Damage Taken'].sum()
                                if g['Damage Taken'].sum() > 0 else np.nan
                               )
).sort_values(by='TotalKills', ascending=False)

print("\n--- Combat Summary by Squadron and Pilot (Multi-Index) ---")
print(squadron_pilot_summary)

# Chaining to find the top pilot in each squadron
top_pilots_per_squadron = (
    combat_log.groupby(['Squadron', 'Pilot ID'])['Kills']
    .sum()
    .sort_values(ascending=False)
    .groupby(level=0)   # regroup by Squadron
    .head(1)            # take top pilot per squadron
)

print("\n--- Top Pilot per Squadron via Chaining ---")
print(top_pilots_per_squadron)
