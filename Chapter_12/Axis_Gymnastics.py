
import numpy as np

# A 3D holocron cube with shape (time, height, width)
holocron_cube = np.random.rand(4, 10, 10)
print("Original Shape:", holocron_cube.shape)

# Transpose the cube (flips axes, not recommended for 3D)
# The axes are reversed: (0, 1, 2) becomes (2, 1, 0)

transposed_cube = holocron_cube.T
print("Transposed Cube Shape:", transposed_cube.shape)

# Swap the time (axis 0) and height (axis 1) axes
swapped_cube = np.swapaxes(holocron_cube, 0, 1)
print("Swapped Cube Shape:", swapped_cube.shape)

# Move the time axis (0) to the last position
moved_cube = np.moveaxis(holocron_cube, 0, -1)
print("Moved Cube Shape:", moved_cube.shape)