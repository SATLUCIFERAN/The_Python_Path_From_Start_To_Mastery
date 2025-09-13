
import pandas as pd
import numpy as np

# Sensor log from the first transmission: Fuel levels
fuel_log = pd.Series([120, 150, 95], index=['TIE Fighter', 'Star Destroyer', 'Imperial Shuttle'])
print("--- Imperial Fuel Log ---")
print(fuel_log)

# Sensor log from the second transmission: Shield integrity
shield_log = pd.Series([88, 72, 90], index=['TIE Fighter', 'Imperial Shuttle', 'Death Star'])
print("\n--- Imperial Shield Log ---")
print(shield_log)

# The Force of Pandas aligns them perfectly by ship type.
combined_log = fuel_log + shield_log
print("\n--- Combined Tactical Report (note the NaN for missing data) ---")
print(combined_log)