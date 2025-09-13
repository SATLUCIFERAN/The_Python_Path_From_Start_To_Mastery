
import numpy as np

# Reshaping a 1D array to a 2D matrix

flat_list = np.arange(9)
matrix = flat_list.reshape(3, 3)
print("Original 1D array:\n", flat_list)
print("\nReshaped 3x3 matrix:\n", matrix)

print('---------------------------------------')

# Stacking two 2D arrays to form a 3D cube
slice1 = np.ones((2, 2))
slice2 = np.zeros((2, 2))
cube = np.stack([slice1, slice2])
print(slice1)
print(slice2)
print("\nStacked 3D cube:\n", cube)
print("Cube shape:", cube.shape)


print('---------------------------------------')

# Adding a new dimension with np.expand_dims

jedi_force_level_1d = np.array([100, 200, 300])
jedi_force_level_2d = np.expand_dims(jedi_force_level_1d, axis=0)

print("\nOriginal 1D array:", jedi_force_level_1d)
print("Original shape:", jedi_force_level_1d.shape)
print("\nExpanded 2D array:\n", jedi_force_level_2d)
print("New shape:", jedi_force_level_2d.shape)