
from pathlib import Path
import os # For setting up our test directories 

# Creating some dummy files and directories to simulate a ship's system
os.makedirs("ship_core/logs/engine_room", exist_ok=True)
os.makedirs("ship_core/logs/life_support", exist_ok=True)
Path("ship_core/logs/engine_room/log_01.dat").touch()
Path("ship_core/logs/engine_room/maintenance.log").touch()
Path("ship_core/logs/life_support/oxygen_levels.dat").touch()
Path("ship_core/logs/life_support/log_02.dat").touch()

# Find all `.dat` files in the 'engine_room' directory only.
print("Scanning engine room for .dat files:")
for file in Path("ship_core/logs/engine_room").glob("*.dat"):
    print(f"- Found: {file}")

# WOW! Now, scan the entire `logs` directory and all subdirectories for all `.dat` files.
print("\nScanning the entire logs system for .dat files:")
for file in Path("ship_core/logs").rglob("*.dat"):
    print(f"- Found: {file}")