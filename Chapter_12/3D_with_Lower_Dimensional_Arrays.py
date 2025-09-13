
import numpy as np

# A 3D holocron cube with shape (4 frames, 5 height, 6 width)
holocron_cube = np.ones((4, 5, 6))

# A 1D array of biases, shape (4,)
biases = np.array([1, 2, 3, 4])

# We need to reshape the biases array to be (4, 1, 1)
# This allows it to broadcast correctly
# The shape will align from the right: (1, 1) and (5, 6) are compatible,
# and (4) and (4) are also compatible.
bias_per_frame = biases.reshape(4, 1, 1)

result = holocron_cube + bias_per_frame
print("Original cube shape:", holocron_cube.shape)
print("Bias array shape:", bias_per_frame.shape)
print("Result cube shape:", result.shape)

# Let's inspect the first frame to see the result
print("\nResult of first frame:\n", result[0, :, :])