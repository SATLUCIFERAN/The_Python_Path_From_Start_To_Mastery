# Fancy indexing on a 2D array
# fleet_roster = np.array([
#     [10, 20, 30],  # Squad A
#     [40, 50, 60],  # Squad B
#     [70, 80, 90]   # Squad C
# ])

# # Select the second and third squads (rows at index 1 and 2)
# selected_squads = fleet_roster[[1, 2]]
# print("\nSelected Squads:\n", selected_squads)

# # Select specific ships from different squads:
# # The ships at (row 0, col 0), (row 1, col 2), and (row 2, col 1)
# specific_ships = fleet_roster[[0, 1, 2], [0, 2, 1]]
# print("\nSpecific Ships:", specific_ships)

# # Fancy indexing on a 3D array
# holocron_cube = np.arange(27).reshape(3, 3, 3)

# # Select three specific data points (voxels) from the cube
# # The points are at (frame 0, row 1, col 2), (frame 1, row 0, col 0), and (frame 2, row 2, col 2)
# specific_voxels = holocron_cube[[0, 1, 2], [1, 0, 2], [2, 0, 2]]
# print("\nHolocron Cube:\n", holocron_cube)
# print("\nSpecific Voxels:", specific_voxels)