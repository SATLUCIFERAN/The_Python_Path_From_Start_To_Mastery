
import numpy as np


shields = np.array([[10, 20, 30],
                    [40, 50, 60]])
laser_blast = np.array([5, 5, 5])

remaining_shields = shields - laser_blast
print("Original Shields:\n", shields)
print("\nLaser Blast:\n", laser_blast)
print("\nRemaining Shields:\n", remaining_shields)





