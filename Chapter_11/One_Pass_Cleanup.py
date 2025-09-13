
import pandas as pd


raw_data = {
    ' Item_Name ': ['Hyperdrive Coil  ', 'Plasma Generator ', '  Energy Cell'],
    ' Cost in Credits ': ['2500', '9000', 'N/A'],
    ' Weight (kg) ': [150.5, 950.2, '800'],
    ' Planet ': [' Tatooine', ' Coruscant ', ' Tatooine '],
    ' Ship Class ': ['Freighter', 'Freighter', 'Fighter']
}

# Load the messy data into a DataFrame.
galactic_manifest = pd.DataFrame(raw_data)

print("--- The Untamed Galactic Manifest (Before Cleanup) ---")
print(galactic_manifest)
print("\n" + "="*50 + "\n")


# --- The One-Pass Cleanup ---
# Here we perform a single, elegant chain of commands to polish the data.

# First, polish the headers.
galactic_manifest.columns = galactic_manifest.columns.str.strip()

# Next, clean the text in the 'Item_Name' column.
galactic_manifest['Item_Name'] = galactic_manifest['Item_Name'].str.strip().str.replace(r'\s+', ' ', regex=True)

# Heal the corrupted numerical columns.
galactic_manifest['Cost in Credits'] = pd.to_numeric(galactic_manifest['Cost in Credits'], errors='coerce').fillna(0)
galactic_manifest['Weight (kg)'] = pd.to_numeric(galactic_manifest['Weight (kg)'], errors='coerce')

# Optimize memory.
galactic_manifest['Planet'] = galactic_manifest['Planet'].astype('category')
galactic_manifest['Ship Class'] = galactic_manifest['Ship Class'].astype('category')


# --- The Polished Jedi Dataframe ---

print("--- The Polished Jedi Dataframe (After Cleanup) ---")
print(galactic_manifest)
print("\n" + "="*50 + "\n")

print("--- Dataframe Information (for memory check) ---")
print(galactic_manifest.info())

print("\n--- Summary of the 'Planet' column ---")
print(galactic_manifest['Planet'].value_counts())


print("\n--- Summary of the 'Ship Class' column ---")
print(galactic_manifest['Ship Class'].value_counts())