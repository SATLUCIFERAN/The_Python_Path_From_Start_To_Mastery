
import numpy as np

holocron_cube = np.random.rand(10, 20, 20)
print(holocron_cube.shape)


# Select a single frame at time index 5
# The result is a 2D array of shape (20, 20)
frame_5 = holocron_cube[5, :, :]
print("Shape of Frame 5:", frame_5.shape)

# A simplified way to do the same thing:
frame_5_simple = holocron_cube[5]
print("Shape of Frame 5 (simplified):", frame_5_simple.shape)

# Get a slice from the first 5 frames
first_5_frames = holocron_cube[:5, :, :]
print("Shape of first 5 frames:", first_5_frames.shape)

# Get a horizontal "slice" through all frames, from height 10 to 20
horizontal_slice = holocron_cube[:, 10:20, :]
print("Shape of horizontal slice:", horizontal_slice.shape)

# Use the ellipsis (...) to represent all preceding axes
# Get every other frame from the cube
every_other_frame = holocron_cube[..., ::2]
print("Shape of every other frame:", every_other_frame.shape)