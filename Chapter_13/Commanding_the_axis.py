
import pandas as pd
import numpy as np

# Create a DataFrame to track an entire squadron of X-Wings
squadron_report = pd.DataFrame(np.random.randint(50, 100, size=(3, 2)),
                             columns=['Proton Torpedoes', 'Shields'],
                             index=['Red 5', 'Red 2', 'Red 1'])

print("--- Rebel Squadron Report ---")
print(squadron_report)

# Calculate the average of each resource across the squadron (down the columns)
# This is the default behavior, so axis=0 is optional
squadron_average = squadron_report.mean(axis=0)
print("\n--- Squadron Average by Resource (axis=0) ---")
print(squadron_average)

# Calculate the total readiness score for each pilot (across the rows)
pilot_readiness = squadron_report.sum(axis=1)
print("\n--- Pilot Total Readiness Score (axis=1) ---")
print(pilot_readiness)

# Recalibrate the report to include 'Red 3' and 'Red 4'
new_squadron_roster = ['Red 5', 'Red 3', 'Red 2', 'Red 4', 'Red 1']
recalibrated_report = squadron_report.reindex(new_squadron_roster)
print("\n--- Recalibrated Squadron Report with .reindex() ---")
print(recalibrated_report)