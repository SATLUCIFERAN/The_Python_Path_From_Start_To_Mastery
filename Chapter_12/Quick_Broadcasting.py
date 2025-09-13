import numpy as np

# A 1D array of starship repair droids
droids = np.array([1, 2, 3, 4])
print("Original Droids Array:", droids)
print("Original Shape:", droids.shape)

# Add a new dimension at the beginning with np.newaxis
# The `np.newaxis` (or `None`) creates a new dimension of size 1
# This is like saying "create a new dimension here"
droids_2d_v1 = droids[np.newaxis, :]
print("\nShape with newaxis:", droids_2d_v1.shape)
print("Expanded array:\n", droids_2d_v1)

# Add a new dimension at the beginning with None
# `None` is a direct alias for `np.newaxis`
droids_2d_v2 = droids[None, :]
print("\nShape with None:", droids_2d_v2.shape)
print("Expanded array:\n", droids_2d_v2)

# Now let's use this for broadcasting
# A 2D grid of asteroid fields
asteroid_grid = np.random.rand(5, 4)

# We want to subtract the droid count from each column
# We use the expanded droids array (with shape (1, 4))
result = asteroid_grid - droids[None, :]

print("\nAsteroid Grid Shape:", asteroid_grid.shape)
print("Droids Shape (before expansion):", droids.shape)
print("Result Shape:", result.shape)
print("\nFinal Result:\n", result)