
import numpy as np

# A 2D array representing a starship fleet
fleet_matrix = np.array([[10, 20, 30],
                        [40, 50, 60]])

# Get the starship specs
print("Fleet Matrix:\n", fleet_matrix)
print("Shape (Dimensions):", fleet_matrix.shape)
print("Size (Total Elements):", fleet_matrix.size)
print("Number of Dimensions:", fleet_matrix.ndim)
print("Data Type:", fleet_matrix.dtype)