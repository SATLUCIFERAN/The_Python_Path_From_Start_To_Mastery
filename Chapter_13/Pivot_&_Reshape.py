import pandas as pd
import numpy as np

# A "long" dataset of combat actions
combat_actions = pd.DataFrame({
    'Pilot ID': ['Luke', 'Luke', 'Wedge', 'Wedge'],
    'Weapon Type': ['Laser Cannon', 'Proton Torpedo', 'Laser Cannon', 
                    'Proton Torpedo'],
    'Kills': [1, 5, 2, 1]
})
print("--- Original Combat Actions (Long Format) ---")
print(combat_actions)

# --- Pivoting with pivot_table() ---
# Summarize total kills by pilot and weapon type
pilot_kills_summary = combat_actions.pivot_table(
    values='Kills',
    index='Pilot ID',
    columns='Weapon Type',
    aggfunc='sum'
)
print("\n--- Pivot Table Summary ---")
print(pilot_kills_summary)


# --- Melting the Data ---
# Convert the wide pivot table back into a long format

melted_data = pilot_kills_summary.melt(
    ignore_index=False,
    value_name='Total Kills',
    var_name='Weapon Type'
).dropna().reset_index()
print("\n--- Melted Data (back to long format) ---")
print(melted_data)

# --- Stacking and Unstacking ---
# Create a MultiIndex from the original data
multi_index_df = combat_actions.set_index(['Pilot ID', 'Weapon Type'])
print(multi_index_df)


# Unstack to turn 'Weapon Type' into a column
unstacked_df = multi_index_df.unstack(level='Weapon Type')
print("\n--- Unstacked Data (from MultiIndex) ---")
print(unstacked_df)

# Now, stack it back to its original MultiIndex form, using the new parameter

stacked_df = unstacked_df.stack(level='Weapon Type', future_stack=True)
print("\n--- Stacked Data (back to MultiIndex) ---")
print(stacked_df)