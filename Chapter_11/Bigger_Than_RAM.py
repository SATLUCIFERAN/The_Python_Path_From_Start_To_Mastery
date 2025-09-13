
import os
from pathlib import Path
import pandas as pd
import numpy as np

# --- 1. Create a large dummy CSV file (The Planetary Manifest) ---
# This simulates a file too big to fit into RAM.

SRC = "huge_manifest.csv"
if not os.path.exists(SRC):
    print("Creating huge_manifest.csv to simulate a large dataset...")
    data = pd.DataFrame({
        "ship": np.random.choice(["X-wing", "Freighter", "Cruiser", "Fighter"], 
                                   size=1_000_000),
        "count": np.random.randint(100, 10000, size=1_000_000),
        "planet": np.random.choice(["Tatooine", "Coruscant", "Alderaan", "Hoth"], 
                                   size=1_000_000),
        "id": range(1_000_000)
    })

    # Add a messy row to test the cleaning parameters    
    data.loc[100, "count"] = "NA"
    data.to_csv(SRC, index=False)
    print("Dummy file created.")
print("\n" + "="*50 + "\n")

# --- 2. Process the file in chunks (The Assembly Line) ---
# The final, uncompressed output file.
OUT = Path("clean_manifest.csv")
# Start with a clean slate.
OUT.unlink(missing_ok=True)

# Keep a running total across all chunks.
running_total = 0

print(f"Processing '{SRC}' in chunks...")
for chunk in pd.read_csv(
        SRC,
        chunksize=100_000,                 # Read in bite-sized pieces
        low_memory=False,                  # A more stable way to read large files
        usecols=["ship", "count", "planet"], # Only import columns we need
        na_values=["NA", "", "N/A", "-"],    # Acknowledge common missing values
        on_bad_lines="skip"                # Skip corrupted rows entirely
    ):
    
    # light cleanup per chunk
    chunk.columns = chunk.columns.str.strip()
    chunk["count"] = pd.to_numeric(chunk["count"], errors="coerce").fillna(0)

    # Add to the running total.
    running_total += int(chunk["count"].sum())

    # keep only useful rows, then append to OUT
    keep = chunk[chunk["count"] > 0]
    
    keep.to_csv(OUT, mode="a", header=not OUT.exists(), index=False)

print(f"\nProcessing complete. Grand total count: {running_total:,}")
print("Final manifest saved to clean_manifest.csv.")
print("\n" + "="*50 + "\n")

# --- 3. Optional: Compress the final file once (The Safe Hyperspace Jump) ---
# This is the safe way to do it for production.
print("Compressing the final manifest...")
import gzip, shutil
with open(OUT, "rb") as src, gzip.open(f"{OUT}.gz", "wb") as dst:
    shutil.copyfileobj(src, dst)
print(f"Final compressed manifest saved to '{OUT}.gz'.")