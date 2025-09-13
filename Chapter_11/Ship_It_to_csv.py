
# The goal is to export our cleaned DataFrame to a file.

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

# FIX: Ensure 'Cost in Credits' is a numeric type for calculations
galactic_manifest['Cost in Credits'] = pd.to_numeric(galactic_manifest['Cost in Credits'])


print("--- Final Manifest (Ready for Export) ---")
print(galactic_manifest)
print("\n" + "="*50 + "\n")


# --- The Ship It Command ---
# Export the DataFrame with the final polish and compression.
galactic_manifest.to_csv(
    'galactic_manifest.csv.gz',
    index=False,
    compression='gzip',
    float_format='%.2f',
    na_rep=''
)

print("Manifest successfully exported to 'galactic_manifest.csv.gz'.")

# For verification, you can read the compressed file back in.
compressed_df = pd.read_csv('galactic_manifest.csv.gz', compression='gzip')
print("\n--- Verification: Read back in from the compressed file ---")
print(compressed_df)