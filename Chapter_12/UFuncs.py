
import numpy as np

# A list of sensor readings for a Jedi's Force-sensitivity
force_readings = np.array([16, 25, 49])

# Calculate the square root of each reading
force_power = np.sqrt(force_readings)
print("Original Readings:", force_readings)
print("Calculated Force Power:", force_power)


# Model a cyclical energy wave
energy_wave_phase = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
energy_wave_signal = np.sin(energy_wave_phase)
print("\nEnergy Wave Phase:", energy_wave_phase)
print("Energy Wave Signal (sin):", energy_wave_signal)


# Model the exponential growth of a force field
initial_field_strength = np.array([1, 2, 3])
field_strength_after_time = np.exp(initial_field_strength)
print("\nInitial Field Strength:", initial_field_strength)
print("Field Strength (exp):", field_strength_after_time)



# A special UFunc: np.where
# It acts as a vectorized if/else statement
ship_status = np.array([1, 0, 1, 1, 0]) # 1=online, 0=offline

# If the value is 1, return "Online", otherwise return "Offline"
status_text = np.where(ship_status == 1, "Online", "Offline")
print("\nShip Status:", ship_status)
print("Formatted Status:", status_text)