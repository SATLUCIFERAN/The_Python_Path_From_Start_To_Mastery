
# The goal is to perform quick aggregations to get high-level intelligence.

import pandas as pd
import numpy as np

# --- The Cleaned Data Manifest ---
# This is our pre-cleaned DataFrame from the previous section.
clean_data = {
    'Item_Name': ['Hyperdrive Coil', 'Plasma Generator', 'Energy Cell', 'Hyperdrive Coil', 'Shield Emitter'],
    'Cost in Credits': [2500, 9000, 800, 2500, 1500],
    'Weight (kg)': [150.5, 950.2, 800.0, 150.5, 200.0],
    'Planet': ['Tatooine', 'Coruscant', 'Tatooine', 'Tatooine', np.nan],
    'Ship Class': ['Freighter', 'Freighter', 'Fighter', 'Freighter', 'Fighter']
}

galactic_manifest = pd.DataFrame(clean_data)

# FIX: Append a single row that is a duplicate of the first row to properly demonstrate duplicates
galactic_manifest.loc[len(galactic_manifest)] = galactic_manifest.iloc[0]
galactic_manifest['Cost in Credits'] = pd.to_numeric(galactic_manifest['Cost in Credits'])


print("--- Dataframe for Aggregation (Before Summaries) ---")
print(galactic_manifest)
print("\n" + "="*50 + "\n")


# --- Tiny Intel Summary 1: Group Stats ---
# Group by 'Planet' and aggregate 'Cost in Credits'
print("--- Total Cost of All Cargo per Planet ---")
planet_cost_summary = galactic_manifest.groupby('Planet').agg(
    Total_Cost=('Cost in Credits', 'sum'),
    Number_of_Items=('Item_Name', 'count')
)
print(planet_cost_summary)
print("\n" + "="*50 + "\n")


# --- Tiny Intel Summary 2: Mini Pivot Teaser ---
# Create a pivot table to see total cost per planet and ship class.
print("--- Total Cargo Cost by Planet and Ship Class ---")
pivot_summary = galactic_manifest.pivot_table(
    values='Cost in Credits',
    index='Planet',
    columns='Ship Class',
    aggfunc='sum'
)
print(pivot_summary)




