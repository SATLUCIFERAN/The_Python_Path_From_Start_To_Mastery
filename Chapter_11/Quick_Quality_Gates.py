# Chapter 12.7.3: Quick Quality Gates
#
# The goal is to perform final checks on our data using quick quality gates.

import pandas as pd
import numpy as np

# --- Our Cleaned Data Manifest ---
# This DataFrame is the result of our One-Pass Cleanup.
# We've added some duplicates and missing values to demonstrate the checks.

clean_data = {
    'Item_Name': ['Hyperdrive Coil', 'Plasma Generator', 'Energy Cell', 
                  'Hyperdrive Coil', 'Shield Emitter'],
    'Cost in Credits': [2500, 9000, 800, 2500, 1500],
    'Weight (kg)': [150.5, 950.2, 800.0, 150.5, 200.0],
    'Planet': ['Tatooine', 'Coruscant', 'Tatooine', 'Tatooine', np.nan],
    'Ship Class': ['Freighter', 'Freighter', 'Fighter', 'Freighter', 'Fighter']
}

galactic_manifest = pd.DataFrame(clean_data)

# --- FIX: Append a single row that is a duplicate of the first row. ---
# This avoids creating a row of lists, which causes the TypeError.
galactic_manifest.loc[len(galactic_manifest)] = galactic_manifest.iloc[0]
print("--- Dataframe for Quality Gates (Before Checks) ---")
print(galactic_manifest)
print("\n" + "="*50 + "\n")

# --- Quality Gate 1: The Holo-Scan ---

print("--- Holo-Scan Report: Dimensions and Data Types ---")
print("Dataframe Shape:", galactic_manifest.shape)
print("\nDataFrame Info:")
galactic_manifest.info()
print("\nDataFrame Head (First 5 Rows):")
print(galactic_manifest.head())
print("\n" + "="*50 + "\n")

# --- Quality Gate 2: The Force Sense ---
print("--- Force Sense Report: Sanity Checks ---")
# Check the distribution of values in 'Planet'
print("Unique Planet Counts:")
print(galactic_manifest['Planet'].value_counts(dropna=False))

# --- FIX: Convert 'Cost in Credits' to a numeric type before the query ---
galactic_manifest['Cost in Credits'] = pd.to_numeric(galactic_manifest['Cost in Credits'])

# Check for illogical values (e.g., negative cost)
print("\nQuery for Negative Costs:")
negative_costs = galactic_manifest.query('`Cost in Credits` < 0')
if not negative_costs.empty:
    print(negative_costs)
else:
    print("No negative costs detected. All systems nominal.")
print("\n" + "="*50 + "\n")

# --- Quality Gate 3: The Clone Patrol ---
print("--- Clone Patrol: Duplicate and Missing Value Check ---")
# Identify and drop exact duplicate rows
print("DataFrame with Duplicates Dropped:")
deduplicated_manifest = galactic_manifest.drop_duplicates()
print(deduplicated_manifest)

# Identify rows with missing 'Planet' data
print("\nDropping rows with missing data in 'Planet':")
manifest_no_missing_planet = galactic_manifest.dropna(subset=['Planet'])
print(manifest_no_missing_planet)