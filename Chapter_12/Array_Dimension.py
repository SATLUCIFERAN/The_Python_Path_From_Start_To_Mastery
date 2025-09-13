
import numpy as np

holocron_cube = np.random.rand(4, 10, 10)
average_per_frame = holocron_cube.mean(axis=(1, 2))
print("Holocron Cube Shape:", holocron_cube.shape)
print("Average per frame:", average_per_frame)




