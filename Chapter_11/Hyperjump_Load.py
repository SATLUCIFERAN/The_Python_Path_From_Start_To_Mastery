import pandas as pd
import io
import os

# --- The Messy Data String ---
data_messy = """ship, cargo_class, count, launch_date, crew
Millennium Falcon, Light Freighter, 1, 1977-05-25, 2.500
T-70 X-wing, Starfighter, NA, 2015-12-18, 1,000
Slave I, Bounty Hunter, 1, 1980-05-21, 2.500
Jedi Starfighter, , 2, 2005-05-19, 1.000
This line is bad and will be skipped
"""

# Reusable options 
opts = dict(
    encoding='utf-8',
    header=0,
    usecols=['ship', 'count', 'launch_date', 'crew'],
    dtype={'count': 'Int64'},            
    na_values=['NA', '', 'N/A', 'null', 'None', '-'],
    parse_dates=['launch_date'],
    thousands=',',
    decimal='.',
    on_bad_lines='skip',              
    skipinitialspace=True,
    engine='python'                  
)

print("Attempting to load messy data with a single command...")
try:
    # Single-pass load
    df = pd.read_csv(io.StringIO(data_messy), **opts)

    # --- Post-Load Sanity Checks ---
    print("\nRunning quick sanity checks...")
    print(f"Initial dtypes:\n{df.dtypes}\n")
    assert df['count'].ge(0).all(), "Error: Negative counts found!"
    print("✓ All counts are non-negative.")
    print(f"\nCrew column summary:\n{df['crew'].describe()}\n")

    # --- Final Export ---
    output_file = 'clean_manifest.csv.gz'
    print(f"Exporting clean data to '{output_file}'...")
    df.to_csv(output_file, index=False, compression='gzip')
    print("✓ Export successful.")

    # --- Performance Teaser (now using the SAME options) ---
    
    print("\nFor truly massive files, consider processing in chunks:")
    for chunk in pd.read_csv(io.StringIO(data_messy), chunksize=2, **opts):
        print(f"- Processed chunk of size {len(chunk)}")
        # process chunk here...

    if os.path.exists(output_file):
        os.remove(output_file)

except Exception as e:
    print(f"An error occurred: {e}")