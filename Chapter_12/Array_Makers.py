
import numpy as np

# Create an array of zeros for an empty sector scan
empty_sector_scan = np.zeros(shape=(3, 3))
print("Empty Sector Scan (Zeros):\n", empty_sector_scan)

# Create an array of ones for a unified shield squadron
shield_squadron = np.ones(shape=(2, 4))
print("\nShield Squadron (Ones):\n", shield_squadron)

# Create an array of speeds from 100 to 500, in steps of 50
speed_range = np.arange(100, 501, 50)
print("\nSpeed Range Array (arange):", speed_range)

# Create an array of 5 evenly spaced coordinates between 0 and 1
evenly_spaced_points = np.linspace(0, 1, 5)
print("\nEvenly Spaced Points (linspace):", evenly_spaced_points)

# Create a random array for simulating ship speeds
random_speeds = np.random.rand(2, 2)
print("\nRandom Speeds (random.rand):\n", random_speeds)