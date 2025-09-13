
import pandas as pd
import numpy as np

# Create a DataFrame to track an entire squadron of X-Wings

squadron_report = pd.DataFrame(np.random.randint(50, 100, size=(3, 2)),
                             columns=['Proton Torpedoes', 'Shields'],
                             index=['Red 5', 'Red 2', 'Red 1'])
print("--- Rebel Squadron Report ---")
print(squadron_report)

# Filter with .loc: Locate 'Red 5' and 'Red 1' by their labels
filtered_loc = squadron_report.loc[['Red 5', 'Red 1']]
print("\n--- Filtering with .loc ---")
print(filtered_loc)


# Filter with .iloc: Select the first two rows by their integer position
filtered_iloc = squadron_report.iloc[0:2]
print("\n--- Filtering with .iloc ---")
print(filtered_iloc)

# Filter with .query: Find ships with a high torpedo count and low shields
filtered_query = squadron_report.query('`Proton Torpedoes` > 50 and Shields < 70')
print("\n--- Filtering with .query ---")
print(filtered_query)