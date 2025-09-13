
# # Our message is just one single rocket emoji.
# # To a human, it's a single "thing."
# message = "🚀"

# # How many characters does Python think this message is?
# # To a human, it's 1. But remember the courier service!
# length_in_characters = len(message)
# print(f"The length of the string is {length_in_characters} characters.")
# # Output: The length of the string is 1 characters.


##################################################################

# A Jedi looking at the raw byte data of the string

message_bytes = "🚀".encode("utf-8")

# Let's see how many bytes the courier service actually used.

number_of_bytes = len(message_bytes)
print(f"The number of bytes used to store the string is {number_of_bytes}.")

# Output: The number of bytes used to store the string is 4.