import pandas as pd
import numpy as np

# A heavily damaged reconnaissance report from a mission in the Outer Rim
# The data includes missing Pilot, Cargo, and a sensor reading

damaged_recon_report = pd.DataFrame({
    'Flight ID': ['X-1', 'X-2', 'Y-1', 'Y-2', 'Z-1', 'Z-2'],
    'Pilot': ['Luke', 'Wedge', 'Biggs', None, 'Han', 'Lando'],
    'Cargo': ['Fuel', 'Fuel', None, 'Ammo', 'Ammo', 'Ammo'],
    'Mission Time': [10, 20, 30, 40, 50, 60],
    'Sensor Reading': [1500.5, 1550.8, None, 1650.4, 1700.1, 1750.0]
})
print("--- Original Damaged Reconnaissance Report ---")
print(damaged_recon_report)

# --- Step 1: Identify Missing Data ---
# Find where the NaN values are and get a count per column.
missing_values_count = damaged_recon_report.isnull().sum()
print("\n--- Missing Value Count per Column ---")
print(missing_values_count)

# --- Step 2: Drop Critically Damaged Records ---
# We decide that a missing Pilot record is too corrupted to be fixed.
# We create a new, clean DataFrame by dropping the row and then taking a full copy.
cleaned_report = damaged_recon_report.dropna(subset=['Pilot']).copy()
print("\n--- After Dropping Records with Missing Pilots ---")
print(cleaned_report)

# --- Step 3: Impute Remaining Missing Data ---
# We take the result of our last step and work on it.
# First, we fill the missing 'Cargo' value with the one that came before it.
# This is a safe assumption for sequential flights.
cleaned_report['Cargo'] = cleaned_report['Cargo'].ffill()
print("\n--- After Fill 'Cargo' ---")
print(cleaned_report)

# Next, we use interpolation to fill the missing 'Sensor Reading'.
# This is ideal for continuous data, as it estimates a value between two points.
cleaned_report['Sensor Reading'] = \
cleaned_report['Sensor Reading'].interpolate(method='linear')
print("\n--- The Final Cleaned and Repaired Report ---")
print(cleaned_report)