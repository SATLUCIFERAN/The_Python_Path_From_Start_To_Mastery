
import numpy as np



# Double the acceleration for all ships in one operation
acceleration = np.array([10, 15, 20])
new_acceleration = acceleration * 2
print("Original Acceleration:", acceleration)
print("New Acceleration:", new_acceleration)

# Add two arrays together, element-wise


acceleration = np.array([10, 15, 20])
initial_speed = np.array([100, 150, 200])
final_speed = initial_speed + acceleration
print("\nFinal Speed:", final_speed)