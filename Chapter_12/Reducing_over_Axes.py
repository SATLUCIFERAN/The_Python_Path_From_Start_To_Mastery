
import numpy as np

# A 2D array of damage taken by two squads
damage_matrix = np.array([[100, 250, 50],
                          [150, 50, 200]])

# Calculate the total damage for each column (each type of damage)
# We sum along axis 0 (down the rows)
total_damage_per_type = damage_matrix.sum(axis=0)
print("Total damage per type:", total_damage_per_type)

# A 3D holocron cube with shape (time, height, width)
holocron_cube = np.random.rand(4, 10, 10)

# Calculate the average value for each time slice (frame)
# We reduce the data along axis 1 (height) and axis 2 (width)
# The result will be a 1D array of averages for each of the four frames
average_per_frame = holocron_cube.mean(axis=(1, 2))
print("\nHolocron Cube Shape:", holocron_cube.shape)
print("Average per frame:", average_per_frame)