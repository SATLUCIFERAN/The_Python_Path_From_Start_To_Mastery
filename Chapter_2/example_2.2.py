
# Our Kyber crystal, a perfect integer
kyber_crystal = 7

# We try to change it
kyber_crystal = kyber_crystal + 1 # This looks like we're changing it...
# But in reality, Python creates a new variable 'kyber_crystal'
# and stores the new value '8' in it. The old '7' is gone.


##########################################################################

# A simple message
secret_message = "Hello"

# This will fail! You can't change a single letter.
# secret_message[0] = "J" 
# TypeError: 'str' object does not support item assignment


##########################################################################

# Creating a new message by adding to the old one.
secret_message = "Hello"
secret_message = "J" + secret_message[1:]
print(secret_message)
# Output: Jello