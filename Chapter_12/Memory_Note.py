
import numpy as np

# A 2D array representing a starship fleet
fleet_matrix = np.array([[10, 20, 30],
                        [40, 50, 60]])

# This method "flattens" the array into a single 1D array
# It shows how the data is stored in memory, row by row
flattened_array = fleet_matrix.ravel()

print("Original 2D Array:\n", fleet_matrix)
print("\nFlattened 1D View (Data in Memory):", flattened_array)