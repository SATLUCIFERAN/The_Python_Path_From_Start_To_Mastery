# You receive a ship's serial number as a string
ship_serial_number_str = "13579"

# The protocol droid (int()) translates it into a number
ship_serial_number_int = int(ship_serial_number_str)

# Now you can use it in a calculation!
next_ship_number = ship_serial_number_int + 1
print(next_ship_number)
print(type(next_ship_number))
# Output: 13580
# <class 'int'>

# You can also translate numbers back into strings
next_ship_number_str = str(next_ship_number)
print(next_ship_number_str)
print(type(next_ship_number_str))
# Output: 13580 (as a string)
# <class 'str'>