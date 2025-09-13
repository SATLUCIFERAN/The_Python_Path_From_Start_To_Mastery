
import numpy as np

jedi_ages = np.array([900, 750, 40, 280])
fleet_formation = np.array([[10, 20, 30],
                           [40, 50, 60],
                           [70, 80, 90]])

print("Third Jedi's Age (Index 2):", jedi_ages[2])
print("\nShip at Row 1, Column 2:", fleet_formation[1, 2])




fleet_formation = np.array([[10, 20, 30],
                           [40, 50, 60],
                           [70, 80, 90]])

first_squadron = fleet_formation[0, :]
print("\nFirst Squadron (Row 0):", first_squadron)

third_column_ships = fleet_formation[:, 2]
print("Third Column Ships:", third_column_ships)

sub_fleet = fleet_formation[0:2, 0:2]
print("Sub-Fleet (Top-Left 2x2):\n", sub_fleet)