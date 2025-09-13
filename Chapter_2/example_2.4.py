# Get a string of the pilot's mission number
mission_number_str = input("Enter your mission number: ")

# Try to translate it into a number (an integer)
mission_number_int = int(mission_number_str)

# Use it in a calculation
next_mission = mission_number_int + 1
print("Your next mission number is", next_mission)